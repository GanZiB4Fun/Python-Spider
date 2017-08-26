# _*_ coding: utf-8 _*_
# @Time    : 2017/8/22 10:55
# @Author  : GanZiB
# @Site    : 
# @File    : JieBaDemo.py
# @Software: PyCharm

import jieba

titles = []
titles.append('中印边界纠纷会影响12天后召开的金砖厦门峰会吗？')
titles.append('历史上最著名的三个“女流氓”，连上海皇帝杜月笙都对她敬畏三分')
titles.append('美国海底发现巨大断层，科学家：与日本大地震构造一样，无法预防')
titles.append('带案督办：成吨鸡蛋壳去了哪里 省案件督办组组长、副组长到蒲江督办环境问题')
titles.append('新提的汉兰达，上牌却被喷字，车主：为何连SUV都要喷？')
titles.append('郭敬明事件公关太给力，朱梓骁当炮灰，陈学冬删评论拉黑网友！')
for title in titles:
	seg_list = jieba.cut(title, cut_all=False)
	print(title + "\n")  # 精确模式
	print(",".join(seg_list))
	print("\n")
