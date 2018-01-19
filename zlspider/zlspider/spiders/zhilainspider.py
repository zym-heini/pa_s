#coding=utf8

import scrapy
from .. import items

class ZhilianSpider(scrapy.Spider):
    '''
    数据采集爬取程序
    '''
    name = "zhilian"
    #定义域名
    allowed_domanis = ["zhaopin.com"]
    start_urls = [ "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC%2b%E4%B8%8A%E6%B5%B7%2b%E5%B9%BF%E5%B7%9E%2b%E6%B7%B1%E5%9C%B3&kw=python&isadv=0&sg=7cd76e75888443e6b906df8f5cf121c1&p=1"]



    def parse(self, response):
        '''
        采集到数据之后自动执行的函数，主要进行如下功能
        数据筛选，封装成item对象，传递给pipelines进行数据存储
        :param response:
        :return:
        '''
        #再次从响应中获取要进行下一次爬取的url地址
        url = response.urljoin(self.start_urls[0])
        yield scrapy.Request(url,callback = self.parse_response)

    def parse_response(self,response):
        #筛选得到的工具列表
        job_list = response.xpath("//div[@id='newlist_list_content_table']/table[position()>1]/tr[1]")
        #循环获取采集的字段信息
        for job in job_list:
            job_name = job.xpath("td[@class='zwmc']/div/a").xpath("string(.)").extract_first()
            # 公司名称
            company = job.xpath("td[@class='gsmc']/a").xpath("string(.)").extract_first()
            # 薪水
            salary = job.xpath("td[@class='zwyx']").xpath("string(.)").extract_first()

            #封装成Item对象
            item = items.ZhilianItem()
            item["job_name"] = job_name
            item["company"] = company
            item["salary"] = salary

            yield item
        #再次从响应中获取下一次进行爬取的url地址
        next_page = response.xpath("//div[@class='pagesDown']/ul/li/a/@href").extract()
        #循环处理请求
        for page in next_page:
            page = response.urljoin(page)
            #重新发起请求采集下一组url地址的数据
            yield scrapy.Request(page, callback=self.parse_response)