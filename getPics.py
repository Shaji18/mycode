# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 16:00:13 2019

@author: fang
"""

import socket
import urllib.request
import re
from lxml import etree
import requests
from pathlib import Path
import threading

# 设置超时, 4s
socket.setdefaulttimeout(4)


# =============================================================================
# 获取首页的所有链接
# =============================================================================
def getArticleLinks(url):
    html = requests.get(url)
    #    print(html.text)
    #    print('===============================')
    selector = etree.HTML(html.text)
    #    print(selector)
    url_list = selector.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
    for i in range(len(url_list)):
        url_list[i] = 'http://tieba.baidu.com' + url_list[i]
    return url_list


# =============================================================================
# 获取链接内的所有图片
# =============================================================================
def getImgs(url, folder):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    img_url_list = selector.xpath('//*[@class="BDE_Image"]/@src')
    global pic_num
    for i in img_url_list:
        pathname = folder / 'pics_{num}.jpg'.format(num=pic_num)
        urllib.request.urlretrieve(i, pathname)
        pic_num = pic_num + 1


def get_html(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    return html


# 主程序
def f1(kywds):
    p = Path.cwd()  # 获取当前工作目录
    kywd = kywds
    front = 'https://tieba.baidu.com/f?kw='
    pathway = '爬虫爬取贴吧5/'
    p_mid = pathway + kywd
    p_new = p / p_mid  # 连接目录名
    p_new.mkdir(parents=True)  # 创建文件夹
    lists = getArticleLinks(front + kywd)
    for i in lists:
        print(i)
        try:
            getImgs(i, p_new)
        except:
            print('Failed downloading')


pic_num = 0
name1 = '壁纸'
name2 = '手机壁纸'
name3 = '桥本环奈'
thread1 = threading.Thread(target=f1, args=(name1,))  # 多线程
thread2 = threading.Thread(target=f1, args=(name2,))
thread3 = threading.Thread(target=f1, args=(name3,))
thread1.start()  # 线程开始
thread2.start()
thread3.start()

# reg = r'src="(.+?\.jpg)"'
# reg_img = re.compile(reg)
# imglist = reg_img.findall(get_html('http://tieba.baidu.com/p/6221802112'))
# x = 0
# for img in imglist:
#    print(img)
#    urllib.request.urlretrieve(img,'%s.jpg' %x)
#    x = x + 2
