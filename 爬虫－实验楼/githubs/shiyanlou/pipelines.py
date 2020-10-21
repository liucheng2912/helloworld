# -*- coding: utf-8 -*-
from datetime import datetime
from others.shiyanlou import engine,Repository
from sqlalchemy.orm import sessionmaker
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ShiyanlouPipeline(object):
    def process_item(self, item, spider):
        item['update_time'] = datetime.strptime(item['update_time'],'%Y-%m-%dT%H:%M:%SZ')
        return self.session.add(Repository(**item))
    def open_spider(self,spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()
    def close_spider(self,spider):
        self.session.commit()
        self.session.close()
