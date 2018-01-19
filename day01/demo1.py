#coding=utf8
#引入需要的模块
import urllib2
hader = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
}
url = "https://image.baidu.com"
res = urllib2.Request(url,headers=hader)
response = urllib2.urlopen(res)
print response.read()