# -*- coding: utf-8 -*-
import scrapy

from WZ.items import WzItem


class WenzhengSpider(scrapy.Spider):
    name = 'wenzheng'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        # 取出每个页面里面帖子链接列表
        links = response.xpath('//*[@id="morelist"]/div/table[2]/tbody/tr/td/table/tbody/tr/td[2]/a[2]/@href').extract()

        # 迭代发送每个帖子的请求, 调用parse_item方法处理
        for link in links:
            yield scrapy.Request(link, callback=self.parse_item)
        # 设置页码终止条件, 并且每次发送的新页面请求调用parse方法处理
        if self.offset <= 71130:
            self.offset += 30
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    def parse_item(self, response):
        """
        解析源码
        :param response:
        :return:
        """
        item = WzItem()


