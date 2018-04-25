#!/usr/bin/env python  
# encoding: utf-8  

"""
@version: v1.0
@author: gaok 
@contact: 542385331@qq.com 
@site: https://blog.csdn.net/qq_27258799 
@file: open_url.py - 使用终端快速打开目标网页
使用方法：
1. 把工程路径添加到系统环境变量
2. 修改open.bat中绝对路径
3. win + R --> open zz 打开<正则表达式学习网页>
@time: 2018/4/25 11:58 
"""

import sys
import webbrowser

URLS = {
    'zz': 'http://deerchao.net/tutorials/regex/regex.htm',  # 正则表达式学习网页
    # 添加自定义网址
}

if len(sys.argv) < 2:
    print('Usage: python open.py [url_key]')
    sys.exit()

url_key = sys.argv[1]

if url_key in URLS:
    print('[URL] = ' + URLS[url_key])
    webbrowser.open(URLS[url_key])
else:
    print('There is no url matched' + url_key)
