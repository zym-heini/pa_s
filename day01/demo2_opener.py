#coding=utf8
import urllib2

url = "https://www.taobao.com"
request = urllib2.Request(url)

#重写opener
#创建一个自定义的Hander对象
http_handler = urllib2.HTTPHandler()
#构建一个opener对象
http_opener = urllib2.build_opener(http_handler)
reponse = http_opener.open(request)

print reponse.read()
