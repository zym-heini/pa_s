# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZlspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ZhilianItem(scrapy.Item):
    '''
    定义采取数据的类型，该类型中，会封装到采集的数据
    继承scrapy.Item类，scrapy才会调用內建函数继续自动化操作
    '''
    #通过scrapy.Field()定义属性字段，每个字段都是采集数据的一部分
    job_name = scrapy.Field()
    company = scrapy.Field()
    salary = scrapy.Field()
