#coding=utf8
import requests

url = "http://news.sina.com.cn/china/"

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
}

reponse = requests.get(url,headers=header)

repons = reponse.text
print repons