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

class MysqlPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            db='scrapy',
            user='root',
            passwd='********',
            port=3306,
            charset='utf8'
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("""
            insert into tengxun(address, date, link, name, number, type)
            values (%s, %s, %s, %s, %s, %s)""",
                                (item['position_address'],
                                 item['position_date'],
                                 item['position_link'],
                                 item['position_name'],
                                 item['position_number'],
                                 item['position_type'],
                                 ))
            self.connect.commit()
        except Exception as error:
            print(error)
        return item
