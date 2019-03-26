# -*- coding: utf-8 -*-
import scrapy
from ..items import TengxunItem

class TengxunSpider(scrapy.Spider):
    name = 'tengxun'
    allowed_domains = ['tencent.com']
    # 定义基准url, 方便下面做拼接,
    url = 'https://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        for i in range(0, 2921, 10):
            yield scrapy.Request(self.url + str(i), callback=self.parseHTML)

    def parseHTML(self, response):
        base_list = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        print(base_list)
        for base in base_list:
            item = TengxunItem()
            item['position_name'] = base.xpath('./td[1]/a/text()').extract()[0]
            item['position_link'] = base.xpath('./td[1]/a/@href').extract()[0]

            item['position_type'] = base.xpath('./td[2]/text()').extract()
            if item['position_type']:
                item['position_type'] = item['position_type'][0]
            else:
                item['position_type'] = ' '
            item['position_number'] = base.xpath('./td[3]/text()').extract()[0]
            item['position_address'] = base.xpath('./td[4]/text()').extract()[0]
            item['position_date'] = base.xpath('./td[5]/text()').extract()[0]
            yield item

# 把308页的URL都给 引擎, 引擎给 调度器去入队列, 在给下载器
