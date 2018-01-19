#coding=utf8
import urllib2

url = "https://www.taobao.com"

request = urllib2.Request(url)

#构建一个可以操作代理服务器的Handler对象

proxy_handler = urllib2.ProxyHandler({"http":"110.73.8.153:8123"})

#构建一个opener对象

porxy_opener = urllib2.build_opener(proxy_handler)

reponse = porxy_opener.open(request)

print reponse.read()