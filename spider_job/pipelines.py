# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
class SpiderJobPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', '123456', 'spider_info' , charset='utf8')
        # 创建游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = "insert into spider_job(工作名称,工资,公司,工作地点,工作要求) VALUES(%s,%s,%s,%s,%s)"
        # 插入数据
        self.cursor.execute(insert_sql, (item['job'], item['job_salary'],item['company'],item['work_address'],item['job_requirements']))
        # 提交
        self.conn.commit()

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()