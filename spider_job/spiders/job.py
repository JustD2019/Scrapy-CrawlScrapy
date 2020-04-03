# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy import cmdline
from spider_job.items import SpiderJobItem


class JobSpider(CrawlSpider):
    name = 'job'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/140000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF,'
                  '2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&'
                  'companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromTy'
                  'pe=&dibiaoid=0''&address=&line=&specialarea=00&from=&welfare=']

    #获取页面中所有符合条件的链接
    rules=(Rule(LinkExtractor(restrict_xpaths="//div[@class='p_in']/ul/li"),follow=True),
        Rule(LinkExtractor(allow=r'.+51job.com/.+/\d+.html'),follow=False,callback='parse_details'),)

    def parse_details(self, response):
        item = SpiderJobItem()

        try:
            job_info = response.xpath("//div[@class='cn']")
            #匹配信息
            item['job'] = job_info.xpath("./h1/text()").get()
            item['job_salary'] = job_info.xpath("./strong/text()").get()
            item['company'] = job_info.xpath("./p[@class='cname']/a[@class='catn']/text()").get()
            item['work_address'] = job_info.xpath("./p[@class='msg ltype']/text()[1]").get().strip()
            job_requirements = job_info.xpath("//div[@class='bmsg job_msg inbox']//p//text()").getall()
            item['job_requirements'] = "".join(job_requirements).strip()
            yield item

        except Exception as e:
            print(e)

#运行爬虫
if __name__ == '__main__':
    cmdline.execute("scrapy crawl job".split())