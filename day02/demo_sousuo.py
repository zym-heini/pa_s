#coding=utf8
from selenium import webdriver
#启动Phantomjs无浏览器界面
driver = webdriver.PhantomJS("./phantomjs-2.1.1-windows/bin/phantomjs")

#访问百度首页
driver.get("http://www.baidu.com")

#获取百度的搜索框
keyword = driver.find_element_by_id("kw")

#向输入框中输入一个要搜索的词语
keyword.send_keys(u"火车票")

#点击百度搜索按钮
btn = driver.find_element_by_id("su").click()


# 查看搜索页面
import time
time.sleep(3)
driver.save_screenshot("wenjian/baidu3.png")