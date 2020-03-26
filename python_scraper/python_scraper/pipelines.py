# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy_djangoitem import DjangoItem

from company.models import Company
from python_scraper.items import CompanyItem


class PythonScraperPipeline(object):

    # Item - The item scraped
    # Spider - The spider that scraped the item
    def process_item(self, item, spider):
        # Commit if:
        #   Item is a Django Item
        #   Item is not currently in the database
        #       - series_lei and rep_pd_date act as primary keys
        item.save(
            commit=
                  isinstance(item, DjangoItem) and
                  not (
                      isinstance(item, CompanyItem) and
                      Company.objects.filter(
                          series_lei=item.instance.series_lei,
                          rep_pd_date=item.instance.rep_pd_date
                      ).exists()
                  )
        )
        return item
