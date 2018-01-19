#coding=utf8

import scrapy
from .. import items

class ZhilianSpider(scrapy.Spider):
    print '****************8'
    '''
    智联数据采集爬虫程序
    '''
    #定义爬虫名称，用于命令调用
    name = "zlspider"
    #定义域名限制，只能爬取zhaopin.com下的所有数据
    allowed_domains = ["zhaopin.com"]
    #定义url地址
    start_urls = (
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=1",
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=2",
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=3",
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=4",
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=5",
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=6",
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=7",
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=8",
    )
    def parse(self, response):
        '''
        采集到数据之后，自动执行的函数，主要进行如下功能
            数据筛选->封装Item对象->传递数据给Pipelines>>>模拟~保存数据到文件
        :param response:
        :return:
        '''

        job_list = response.xpath("//div[@id='newlist_list_content_table']/table[position()>1]/tr[1]")
        for select in job_list:

            print '************************'
            job = select.xpath("td[@class='zwmc']/div/a/text()").extract_first()
            company = select.xpath("td[@class='gsmc']//a/text()").extract_first()
            salary = select.xpath("td[@class='zwyx']/text()").extract_first()

            #封装成Item对象
            item = items.ZhilianItem()
            item["job"] = job
            item["company"] = company
            item["salary"] = salary

            #将本次生成的item队形交给pipline进行处理
            yield item



