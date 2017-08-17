# _*_ coding: utf-8 _*_
# @Time    : 2017/8/17 14:35
# @Author  : GanZiB
# @Site    : 
# @File    : images-spider.py
# @Software: PyCharm

import re
import urllib.error
import urllib.request


def craw(url, page):
	htmlList = urllib.request.urlopen(url).read()
	htmlListStr = str(htmlList)
	divPattern = '<div id="plist" class="goods-list-v2 J-goods-list gl-type-3 ".+? <div class="page clearfix"'
	divResult = re.compile(divPattern).findall(htmlListStr)
	divResult = divResult[0]
	imgPattern = '<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
	imageList = re.compile(imgPattern).findall(divResult)
	x = 1
	for imageUrl in imageList:
		imageName = "D:/JDIMG/" + str(page) + "-" + str(x) + ".jpg"
		imageUrl = "http://" + imageUrl
		try:
			urllib.request.urlretrieve(imageUrl, filename=imageName)
		except urllib.error.URLError as e:
			if hasattr(e, "code"):
				x += 1
			if hasattr(e, "reason"):
				x += 1
		x += 1
		print("保存图片---" + imageUrl + "---成功")


if __name__ == '__main__':
	print('欢迎！请输入采集的页数')
	pageNum = input('--你想采集多少页?\n--')
	for i in range(1, int(pageNum)):
		url = 'https://list.jd.com/list.html?cat=9987,653,655&page=' + str(i)
		craw(url, i)
