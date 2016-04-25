#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
# File Name: useragent/spiders/useragent_spider.py
# Author: YourName
# mail: YourEmail
# Created Time: 2016-04-25

from scrapy.spider import Spider
from scrapy.selector import Selector
from useragent.items import UseragentItem
from scrapy.http import Request

class UseragentSpider(Spider):
    name = "useragent"
    allow_domains = ["httpbin.org"]
    start_urls = ["http://httpbin.org/headers"]

    def parse(self,response):
        print response.body
