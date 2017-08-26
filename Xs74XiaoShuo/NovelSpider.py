# _*_ coding: utf-8 _*_
# @Time    : 2017/8/18 21:51
# @Author  : GanZiB
# @Site    : 
# @File    : NovelSpider.py
# @Software: PyCharm

import re
import urllib.error
import urllib.parse
import urllib.request

import pymysql.cursors

config = {
	'host': '127.0.0.1',
	'port': 3306,
	'user': 'root',
	'password': 'root',
	'db': 'novel',
	'charset': 'utf8',
	'cursorclass': pymysql.cursors.DictCursor,
}


# 开始连接
# connection = pymysql.connect(**config)
# try:
# 	with connection.cursor() as  cursor:
# 		sql = "INSERT INTO novel_base (novel_id,novel_title,novel_summary,novel_author) VALUES (%s, %s, %s, %s)"
# 		cursor.execute(sql,('sdasda','测试2','测试2测试2','GanZiB'))
# 		connection.commit()
# finally:
# 	connection.close()

def downloadNovel(url):
	req = urllib.request.Request(url)
	req.add_header('User-Agent',
				   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36')
	data = urllib.request.urlopen(req, timeout=30000).read().decode('GBK')
	divpat = '<div id="hotcontent">(.*?)<div id="newscontent">'
	print(re.compile(divpat).findall(data))
	print(data)


def getCategoryUrl():
	# print(urllib.request.quote(novelName))
	url = "http://www.xs74.com/list/wuxia.html"
	req = urllib.request.Request(url)
	req.add_header('User-Agent',
				   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36')
	data = urllib.request.urlopen(req, timeout=30000).read().decode('GBK')
	wuxiapat = '<li><a href="(.*?)">武侠修真</a></li>'
	kehuanpat = '<li><a href="(.*?)">科幻灵异</a></li>'
	xuanhuanpat = '<li><a href="(.*?)">玄幻奇幻</a></li>'
	categoryUrls = []
	categoryUrls.append(re.search(wuxiapat, data).group())
	categoryUrls.append(re.search(kehuanpat, data).group())
	categoryUrls.append(re.search(xuanhuanpat, data).group())
	for li in categoryUrls:
		urlpat = 'http:.*?html'
		categoryUrl = re.compile(urlpat).search(li).group()
		downloadNovel(categoryUrl)


if __name__ == '__main__':
	# print("请输入您想看的小说名")
	# novelName = input("小说名\n")
	getCategoryUrl()
