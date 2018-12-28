# -*- coding: utf-8 -*-
import scrapy


class WenzhengSpider(scrapy.Spider):
    name = 'wenzheng'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        pass
