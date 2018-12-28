# -*- coding: utf-8 -*-
import scrapy


class WenzhengSpider(scrapy.Spider):
    name = 'wenzheng'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/']

    def parse(self, response):
        pass
