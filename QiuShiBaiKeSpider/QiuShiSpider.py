# _*_ coding: utf-8 _*_
# @Time    : 2017/8/17 16:01
# @Author  : GanZiB
# @Site    : 
# @File    : QiuShiSpider.py
# @Software: PyCharm

import re
import urllib.error
import urllib.request


def getContent(url, page):
	headers = ('User-Agent',
			   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36')
	opener = urllib.request.build_opener()
	opener.addheaders = [headers]
	# 将opener 折设置为全局
	urllib.request.install_opener(opener)
	# 开始采集页面
	data = urllib.request.urlopen(url).read().decode("utf-8")
	# 构建用户提取的正则表达式
	userpat = '<h2>(.*?)</h2>'
	# 构建段子内容提取的正则表达式
	contentpat = '<div class="content">(.*?)</div>'
	# 获取当前页面所有的用户名称
	userList = re.compile(userpat, re.S).findall(data)
	# 获取当前页面所有的段子内容
	contentList = re.compile(contentpat, re.S).findall(data)
	# x=1
	# #通过for循环遍历段子内容斌分别赋值给对应变量
	# for content in contentList:
	# 	content = content.replace("\n","")
	# 	name = "content"+str(x)
	# 	exec (name+'=content')
	# 	x+=1
	#
	# y=1
	# for user in userList:
	# 	name = 'content'+str(y)
	# 	user = user.replace("\n","")
	# 	print('用户'+str(page)+'页第'+str(y)+"位是:" +user)
	# 	print('内容是:')
	# 	exec("print("+name+")")
	# 	print("\n")

	# 将两个列表合成字典
	result = dict(zip(userList, contentList))
	# 循环字典
	for key in result:
		userName = str(key).replace("\n", "")
		content = str(result[key]).replace("\n", "").replace("<span>", "").replace("</span>", "").replace("<br/>",
																										  "").replace(
			"。", "。\n")
		print("用户---" + userName)
		print("内容:---\n	" + content)
		print("\n\n")


if __name__ == '__main__':
	for i in range(1, 30):
		url = 'https://www.qiushibaike.com/text/page/' + str(i) + '/'
		getContent(url, i)
	print("29页循环完毕")
