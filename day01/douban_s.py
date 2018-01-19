#coding=utf8
#引入需要的模块
import urllib2

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action="

hader = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
}

reponse = urllib2.Request(url,headers=hader)
json = urllib2.urlopen(reponse).read()
print json