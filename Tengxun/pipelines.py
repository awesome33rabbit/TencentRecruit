# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TengxunPipeline(object):
    def process_item(self, item, spider):
        # print('*' * 30)
        # print(item['position_name'])
        # print(item['position_link'])
        # print(item['position_type'])
        # print(item['position_number'])
        # print(item['position_address'])
        # print(item['position_date'])
        return item
