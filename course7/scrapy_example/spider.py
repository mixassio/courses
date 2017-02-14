# -*- coding: utf-8 -*-

import scrapy
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst

__author__ = 'sobolevn'


class CustomPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, BlogCategory):
            item['name'] = 'URL: ' + item['name']
        return item


class BlogCategory(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst())
    posts = scrapy.Field()


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com', ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'spider.CustomPipeline': 1
        }
    }

    def parse(self, response):
        for url in response.css('ul li a::attr("href")').re('.*/category/.*'):
            print('---------------------------------')
            print(url)

            yield scrapy.Request(
                response.urljoin(url),
                lambda r: self.parse_titles(r, url)
            )

    def parse_titles(self, response, hub):
        loader = ItemLoader(item=BlogCategory(), response=response)
        loader.add_value('name', hub)
        loader.add_css('posts', 'main > article h2.entry-title > a::text')
        yield loader.load_item()
