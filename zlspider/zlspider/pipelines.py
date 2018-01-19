# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class ZlspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class ZhilianPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient("localhost",27017)
        self.client = client['local']['zhilian']

    def process_item(self,item,spider):
        data = {
            "job_name":item["job_name"],
            "company":item["company"],
            "salary":item["salary"],

        }
        print ">>>>>>>>>>>>>>>>  neihan pipelines iswoking....."
        self.client.insert(data)

