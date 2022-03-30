#!/usr/bin/env python3
import paramiko
import random
import string
from loguru import logger


class SSHRSAServer:

    def __init__(self, ip, port, username, keyfile, password):
        self.ip = ip
        self.port = port
        self.username = username
        if password != "":
            self.password = paramiko.RSAKey.from_private_key_file(keyfile, password=password)
        else:
            self.password = paramiko.RSAKey.from_private_key_file(keyfile)
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=self.ip, port=self.port, username=self.username, pkey=self.password, timeout=3)
        self.transport = paramiko.Transport(self.ip, int(self.port))
        self.transport.connect(username=self.username, pkey=self.password)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

    def ssh_exec_cmd(self, command):
        try:
            stderr = ""
            stdout = ""
            try:
                stdin, stdout, stderr = self.ssh.exec_command(command, timeout=3)
                # stdin.write(new_password + '\n' + new_password + '\n')
                result = stdout.read()
                logger.success(f"执行命令成功")
                return result
            except:
                logger.success(f"似乎执行命令成功")
        except paramiko.ssh_exception.AuthenticationException as e:
            logger.warning(f"账号密码错误{e}")
        except:
            # traceback.print_exc()
            logger.error(f"连接失败")

    def down_file(self, server_file, localhost_file):
        """
        将服务器文件下载至本地
        :param localhost_file: 本地文件路径
        :param server_file: 服务器保存路径
        :return:
        """
        self.sftp.get(server_file, localhost_file)
        logger.success(f"下载成功，储存在{localhost_file}")

    def up_file(self, localhost_file, server_file):
        """
        将本地文件上传至服务器
        :param localhost_file: 本地文件路径
        :param server_file: 服务器保存路径
        :return:
        """
        self.sftp.put(localhost_file, server_file)
        logger.success(f"上传成功，储存在{server_file}")


if __name__ == "__main__":
    # 服务器ip
    ip = '0.0.0.0'
    # 一般为统一固定端口
    port = 22
    # RSA私钥对应的用户
    username = 'user'
    # 填写自己私钥的名称
    keyfile = './key/privatekey.pem'
    # RSA私钥的密码, 没有则置空
    password = 'pass'
    # 跳转至web服务下的目录存储
    cmd = "cd /var/www/html;tar -czvf /tmp/web.tgz ./"

    ssh = SSHRSAServer(ip=ip, port=port, username=username, keyfile=keyfile, password=password)
    ssh.ssh_exec_cmd(cmd)
    savename = "web-" + "".join(random.sample(string.ascii_lowercase + string.digits, 8)) + ".tgz"
    ssh.down_file('/tmp/web.tgz', f'./files/{savename}')
