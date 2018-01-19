# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MypaSItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ZhilianItem(scrapy.Item):
    """
    自定义封装智联招聘的Item类型，用于封装采集到的数据
    """
    #定义属性字段
    job = scrapy.Field()
    company = scrapy.Field()
    salary = scrapy.Field()

