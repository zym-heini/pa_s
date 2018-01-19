#coding=utf8
from selenium import webdriver

#如果配置了环境变量，直接启动
#driver = webdriver.PhantomJS()
#r如果没有配置。需要指定路径启动
driver = webdriver.PhantomJS("./phantomjs-2.1.1-windows/bin/phantomjs")

driver.get("http://www.baidu.com")

#查看访问结果，保存访问的截图
driver.save_screenshot("wenjian/baidu1.png")
#保存访问的数据的源代码
with open("wenjian/baidu.html","w") as f:
    f.write(driver.page_source.encode("utf-8"))