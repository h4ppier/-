#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 爬取必应每日背景并设置为桌面壁纸
import requests
import os
import datetime
import win32api, win32con, win32gui
from bs4 import BeautifulSoup

def get_pic():

	url = "https://cn.bing.com"
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
	}
	# 获取必应背景图片的源地址
	res = requests.get(url, headers=headers)
	soup = BeautifulSoup(res.text, 'lxml')
	pic_url = url + soup.find_all(id='bgImgProgLoad')[0].get('data-ultra-definition-src')
	# 图片路径信息，图片名称为当天日期
	today = datetime.date.today()
	pic_path = "E:\\code\\Python\\picture\\" + str(today) + '.bmp'

	with open(pic_path, 'wb') as pic:
		pic_res = requests.get(pic_url)
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
	set_pic(get_pic())

