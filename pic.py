#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 爬取照片并设置为桌面壁纸
import requests
import os
import time
import win32api, win32con, win32gui
from bs4 import BeautifulSoup

# 必应每日壁纸
biying = "https://api.dujin.org/bing/1920.php"
# 随机图片
lore = "http://lorempixel.com/1920/1080/"
# 随机风景图
view = "https://api.ixiaowai.cn/gqapi/gqapi.php"
# 随机动漫壁纸
acg = "https://img.xjh.me/random_img.php?type=bg&ctype=nature&return=302"

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
}

def get_pic(url):
	# 随机风景图
	pic_url = url
	pic_path = "E:\\code\\Python\\picture\\" + str(int(time.time())) + '.bmp'
	with open(pic_path, 'wb') as pic:
		pic_res = requests.get(pic_url, headers = headers)
		pic.write(pic_res.content)
	return pic_path

def set_pic(pic_path):
	# 定义设置图片的注册表地址
	reg_path = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
	# 参数2表示拉伸, 其他还有 0居中, 6适应, 10填充
	win32api.RegSetValueEx(reg_path, "WallpaperStyle", 0, win32con.REG_SZ, "2")
	# 刷新桌面
	win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, pic_path, win32con.SPIF_SENDWININICHANGE)

if __name__ == '__main__':
	set_pic(get_pic(acg))

