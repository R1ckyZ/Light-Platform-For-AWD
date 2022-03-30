#!/usr/bin/env python3
import paramiko
import random
import string
from loguru import logger

class SSHServer:

    def __init__(self,ip,port,username,password):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=self.ip, port=self.port, username=self.username, password=self.password, timeout=3)
        self.transport = paramiko.Transport(self.ip, int(self.port))
        self.transport.connect(username=self.username, password=self.password)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

    def change_pwd(self, ip, port, login_user, modify_user, old_password, new_password):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(hostname=ip, port=port, username=login_user, password=old_password, timeout=3)
            if login_user == "root":
                command = f"passwd {modify_user}\n"
                stdin, stdout, stderr = self.ssh.exec_command(command)
                stdin.write(new_password + '\n' + new_password + '\n')
            else:
                command = f"passwd \n"
                stdin, stdout, stderr = self.ssh.exec_command(command)
                stdin.write(old_password + '\n' + new_password + '\n' + new_password + '\n')
            out, err = stdout.read(), stderr.read()
            if "successfully" in str(out) or "successfully" in str(err):
                logger.success(f"{ip}:{port}密码修改成功")
            else:
                logger.error(f"{ip}:{port}密码修改失败{str(err)}")
            self.ssh.close()
        except paramiko.ssh_exception.AuthenticationException as e:
            logger.warning(f"{ip}:{port}账号密码错误{e}")
        except:
            # traceback.print_exc()
            logger.error(f"{ip}:{port}连接失败")

    def ssh_exec_cmd(self,command):
        try:
            stderr = ""
            stdout = ""
            try:
                stdin, stdout, stderr = self.ssh.exec_command(command,timeout=3)
                # stdin.write(new_password + '\n' + new_password + '\n')
                result = stdout.read()
                logger.success(f"执行命令成功")
                return result
            except :
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

if __name__ == '__main__':
    # 服务器ip
    ip = '0.0.0.0'
    # 一般为统一固定端口
    port = 22
    username = 'user'
    password = 'pass'
    # 跳转至web服务下的目录存储
    cmd = "cd /var/www/html;tar -czvf /tmp/web.tgz ./"

    ssh = SSHServer(ip=ip, port=port, username=username, password=password)
    ssh.ssh_exec_cmd(cmd)
    savename = "web-"+"".join(random.sample(string.ascii_lowercase+string.digits, 8)) + ".tgz"
    ssh.down_file('/tmp/web.tgz', f'./files/{savename}')




