# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from WZ.items import WzItem


class WenzhengSpider(CrawlSpider):
    name = 'wenzheng'
    allowed_domains = ['wz.sun0769.com/']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0
    start_urls = [url + str(offset)]

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse(self, response):
        # 取出每个页面里帖子链接列表
        links = response.xpath("//div[@class='greyframe']/table//td/a[@class='news14']/@href").extract()
        # 迭代发送每个帖子的请求，调用parse_item方法处理
        for link in links:
            yield scrapy.Request(link, callback=self.parse_item)
        # 设置页码终止条件，并且每次发送新的页面请求调用parse方法处理
        if self.offset <= 71130:
            self.offset += 30
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
