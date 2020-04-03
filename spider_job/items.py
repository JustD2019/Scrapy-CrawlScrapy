# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderJobItem(scrapy.Item):
    job = scrapy.Field()
    job_salary = scrapy.Field()
    company = scrapy.Field()
    work_address = scrapy.Field()
    job_requirements = scrapy.Field()

    pass
