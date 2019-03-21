# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import ShiyanlouItem 

class GithubsSpider(scrapy.Spider):
    name = 'githubs'
    start_urls = ['']
    @property
    def start_urls(self):
        return(['https://github.com/shiyanlou?tab=repositories','https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoyMToxNiswODowMM4FkpXb&tab=repositories','https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoyMToxNiswODowMM4FkpXb&tab=repositories','https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoyMToxNiswODowMM4FkpXb&tab=repositories'])

    def parse(self, response):
        for r in response.css('li.public'):
            yield ShiyanlouItem({
                'name':r.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first(r'\n\s*(.*)'),
                'update_time': r.xpath('.//relative-time/@datetime').extract_first()
            })
