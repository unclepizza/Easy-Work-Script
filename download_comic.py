#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: gaok 
@contact: 542385331@qq.com 
@site: https://blog.csdn.net/qq_27258799 
@file: download_comic.py - 免手动翻页，自动下载xkcd漫画图片
@time: 2018/4/25 20:28 
"""

import requests, os, bs4


def download_page():
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    return bs4.BeautifulSoup(res.text)


def save_image_from_page(outer_soup):
    comic_elem = outer_soup.select('#comic img')
    if not comic_elem:
        print('Could not find comic image.')
    else:
        comic_url = 'http:' + comic_elem[0].get('src')
        print('Downloading image %s...' % comic_url)
        res = requests.get(comic_url)
        res.raise_for_status()
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()


def get_prev_url(outer_soup):
    prev_link = outer_soup.select('a[rel="prev"]')[0]
    return 'http://xkcd.com' + prev_link.get('href')


if __name__ == '__main__':
    os.makedirs('xkcd', exist_ok=True)
    url = 'https://xkcd.com/'
    while not url.endswith('#'):
        soup = download_page()
        save_image_from_page(soup)
        url = get_prev_url(soup)
    print('Done.')
