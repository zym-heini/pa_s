#coding=utf8
import scrapy

class GetSpider(scrapy.Spider):
    name = "getspider"
    allowed_domains = ["baidu.com"]
    start_url = [
        "http://www.baidu.com"
    ]
    def parse(self, response):
        '''
        起始请求的数据采集工作，由scrapy框架自动完成

        :param response:
        :return:
        '''