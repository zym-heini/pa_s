#coding=utf8
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"),"lxml")

#根据标签名称查询

h2_e = soup.find_all("h2")

print h2_e

#根据名称的正则表达式进行查询

import re
h2_r = soup.find_all(re.compile("p+"))
print h2_r

#一次查询多个标签
h2_k = soup.find_all(["div","h2","h1"])
print h2_k

#内容查询
h2_t = soup.find_all(text = "登黄鹤楼")
print h2_t

#关键字参数：通过attrs将标签的属性和属性值作为字典数据进行查询操作
h2_kw = soup.find_all(attrs = {"class":"content"})
print h2_kw

#CSS操作  核心函数操作select()
#标签选择器

span_e = soup.select("span")
print span_e

#ID选择器
soup_id = soup.select("#title")
print soup_id

#class选择器
soup_class = soup.select(".content")
print soup_class

#包含选择器
soup_e = soup.select("#container p")
print soup_e[0].text

#子类选择器
soup_e = soup.select("#container > p")
print soup_e[0].text

#属性选择器
div_attr = soup.select("div[class]")
print div_attr[0].text

div_attr2 = soup.select("div[id='intro']")
print div_attr2[0].text