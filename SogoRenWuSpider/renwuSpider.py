# _*_ coding: utf-8 _*_
# @Time    : 2017/8/25 17:38
# @Author  : GanZiB
# @Site    : 
# @File    : renwuSpider.py
# @Software: PyCharm
import re
import socket
import time
import urllib.error
import urllib.request

from bs4 import BeautifulSoup

socket.setdefaulttimeout(60)


def get_time_stamp():
	ct = time.time()
	local_time = time.localtime(ct)
	data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
	data_secs = (ct - int(ct)) * 1000
	time_stamp = "%s.%03d" % (data_head, data_secs)
	return time_stamp


def start(url):
	men = []
	try:
		page = urllib.request.urlopen(url, timeout=30000).read().decode('utf-8')
		time.sleep(4)
		names = re.compile(';">.*?</a></h2>').findall(page)
		for name in names:
			name = re.sub('(;">)|(</a></h2>)', '', name)
			if '(' in name:
				name = name[0:name.index('(')]
			men.append(name)
	except Exception as e:
		print("连接错误")
	except WindowsError as e:
		print("连接错误")
	except BaseException as e:
		print("连接错误")
	return men


def find_string(tag):
	res = re.search('.*?家|.*?星|.*?人才|.*?员|.*?人物.*?|.*?演员|.*?歌手|.*?者|.*?人', tag)
	if res != None:
		return True
	else:
		return False


def getTags(url):
	tags = []
	page = urllib.request.urlopen(url, timeout=30000).read().decode('utf-8')
	time.sleep(3)
	info_url_str = re.compile('<h2><a href=".*?" target=').findall(page)
	info_urls = []
	for url_str in info_url_str:
		url_str = re.sub('(<h2><a href=")|(" target=)', '', url_str)
		info_urls.append('http://baike.sogou.com/' + url_str)
	for info_url in info_urls:
		try:
			infoPage = urllib.request.urlopen(info_url, timeout=30000).read().decode('utf-8')
			time.sleep(3)
			soup = BeautifulSoup(infoPage)
			a_str = soup.find_all('a', 'lemma_tag')
			for a in a_str:
				tag = a.contents[0]
				tag = re.sub('(\[\')|(\t)|(\r)|(\t)|(\n)|( )', '', tag)
				print(tag)
				if tag:
					if find_string(tag):
						tags.append(tag)
		except urllib.error as e:
			print("连接错误")
		except WindowsError as e:
			print("连接错误")
		except BaseException as e:
			print("连接错误")
	return tags


if __name__ == '__main__':
	print(str(get_time_stamp()) + '采集开始')
	firstUrl = 'http://baike.sogou.com/Search.e?sp=S%E4%BA%BA%E7%89%A9&sp=1&pg='
	tags = []
	men = []
	for pageNum in range(50):
		print(str(get_time_stamp()) + '正在采集第--' + str(pageNum) + '--页')
		tags_url = firstUrl + str(pageNum)
		tags.extend(getTags(tags_url))
	file = open('人物相关标签.txt', 'w', encoding='utf-8')
	file.write(str(tags))
	file.close()
	men = []
	f = open('人物相关标签.txt', 'r', encoding='utf-8')
	tags = set(eval(f.read()))

	for tag in tags:
		for pg in range(50):
			print(str(get_time_stamp()) + '正在采集标签--' + tag + '---分类下的人物第' + str(pg) + '页')
			secondUrl = 'http://baike.sogou.com/Search.e?sp=S' + urllib.request.quote('明星') + '&sp=1&pg=' + str(pg)
			men.extend(start(secondUrl))
	file = open('人物.txt', 'w', encoding='utf-8')
	file.write(str(men))
	file.close()
	print(str(get_time_stamp()) + '采集完毕')
