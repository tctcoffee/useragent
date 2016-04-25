#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
# File Name: useragent/spiders/useragent_spider.py
# Author: YourName
# mail: YourEmail
# Created Time: 2016-04-25

import random
#from scrapy import log
#from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class RotateUserAgentMiddleware(object):
    def __init__(self,filename):
	with open(filename) as f:
		self.user_agents = [
			line.strip()
			for line in f.readlines()
		]
    
    @classmethod
    def from_crawler(cls,crawler):
	return cls(
		crawler.settings.get('USER_AGENT_LIST_FILE','user-agents.txt')
	)
    def process_request(self,request,spider):
        ua = random.choice(self.user_agents)
        if ua:
            print "*******Current UserAgent:%s************" %ua
            request.headers.setdefault('User-Agent',ua)
    

