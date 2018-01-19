#coding=utf8
#python通过lxml模块进行Xpath操作
from lxml import etree
#etree手机进行DOM操作转换的模块
html = etree.parse("index.html")
#爬虫~直接获取到的数据
print html

#获取数据直接操作标签
ele_h1 = html.xpath("//h1")
print ele_h1
print ele_h1[0].text
#获取其中的子节点数据
print ele_h1[0].xpath("string(.)")

#获取数据~操作标签的属性
ele_h2 = html.xpath("//h2[@id='title2']")
print ele_h2[0].text

ele_h2_zgl = html.xpath("//h2[@id='intro_title']")
print(ele_h2_zgl)
print(ele_h2_zgl[0].text)
print(ele_h2_zgl[0].xpath("string(.)"))


#通过属性执行获取标签
ele_h3 = html.xpath("//body/p[@class='content']")
print ele_h3
for ele in ele_h3:
    print ele.text
