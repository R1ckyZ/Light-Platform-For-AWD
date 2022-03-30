# Light platform for AWD

> 较为轻便的AWD防御和攻击模块

构建

```
├─burpPlugin
│      burp-requests-new.jar
│
├─simpleAttack
│  │  exploit.py
│  │  ipwrite.py
│  │  sshCmd.py
│  │  sshRSACmd.py
│  │  upload.py
│  │
│  └─conf
│  │    poc.py
│  │    settings.py
│  │    __init__.py
│  │            
│  ├─files
│  └─key         
│
├─vuldocker
│      docker-compose.yml
│      Makefile
│      README.md
│
└─waf
     index.php
     waf.php
```

## burpsuite插件

burpsuite插件用于快速生成可以利用的 POC, 在[原始插件](ttps://github.com/silentsignal/burp-requests)上进行的改进, 共有三种复制方法

```
Copy as requests
Copy as requests with session object
Copy as requests with batch attack
```

前两种直接生成可以运行的python request脚本, 后一种则生成poc利用函数, 调用可自行配置

## simpleAttack

利用顺序:

```
settings.py 设置 > ipwrite.py 设置执行 > upload.py 批量上传不死马 > poc.py 设置复制好的模板 > exploit.py 执行POC并提交flag
```

SSH连接方式支持密码连接和RSA公私钥连接(key文件夹用于存储RSA私钥), 提供远程执行命令下载源码至files目录下或上传文件等功能。

## vuldocker

simpleAttack效果的简单测试环境

## waf

将该waf.php置于/tmp文件, 在web服务处在目录下批量添加waf.php

```
find . -type f -name "*.php"|xargs sed -i "s/<?php/<?php\nrequire_once('\/tmp\/waf.php');\n/g"
```

