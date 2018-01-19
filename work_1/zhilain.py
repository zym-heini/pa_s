#coding=utf8
import requests
import urllib
from lxml import etree



def spadir(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    }
    response = requests.get(url,headers = header)
    html = response.text
    htmls = etree.HTML(html)
    zhiwei = htmls.xpath("//td[@class='zwmc']/div/a[1]")
    for zw in zhiwei:

        box = htmls.xpath("//td[@class='gsmc']/a[1]")
        for gs in box:
            xinzi = htmls.xpath("//td[@class='zwyx']")
            for xz in xinzi:
                # htmls1 = html.replace("\n", "").replace("\t", "").replace("\r", "")
                # urls = re.findall(r'<a style="font-weight:(.*?)href="(.*?)" target=(.*?)"fk_lv">',htmls1)
                # for ur in urls:

                xzs = xz.xpath("string(.)").strip()
                zws = zw.xpath("string(.)").strip()
                gss = gs.xpath("string(.)").strip()
                    # wo = spadir1(ur[1])
                print xzs,zws,gss
                    # write(zws,xzs,gss,wo)
    # htmls = html.replace("\n","").replace("\t","").replace("\r","")
    # content = re.findall(r'<a style="font-weight: bold"(.*?)>(.*?)<a href=(.*?)_blank">(.*?)</a> <a (.*?)"zwyx">(.*?)</td> (.*?)_last"> (.*?)</li></li>(.*?)class="newlist">',htmls)
    # print content
    # for con in content:
    #     print con[1]
    #     print con[3]
    #     print con[5]
    #     print con[7]

def spadir1(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    }
    response = requests.get(url,headers = header)
    html = response.text
    htmls = etree.HTML(html)
    work = htmls.xpath("//div[@class='tab-inner-cont'][1]")
    for wo in work:
        return wo.xpath("string(.)").strip()

def engine():
    city = raw_input("请输入职位城市：")
    work = raw_input("请输入职位名称：")
    url = "http://sou.zhaopin.com/jobs/searchresult.ashx?isadv=0"
    jl = urllib.urlencode({"jl": city})
    kw = urllib.urlencode({"kw": work})
    urls = url +"&" + jl +"&" + kw
    spadir(urls)

def write(zhiwei,xinzi,gongsi,work):
    with open("docxs/zhilain.text","a")as f:
        f.write(zhiwei.encode("utf-8"))
        f.write(xinzi.encode("utf-8"))
        f.write(gongsi.encode("utf-8"))
        f.write(work.encode("utf-8"))


if __name__ == '__main__':

    engine()
