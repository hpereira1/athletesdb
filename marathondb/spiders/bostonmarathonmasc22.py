import scrapy
from marathondb.items  import PropertiesItem


class BostonMarathonMasc22(scrapy.Spider):
    name = 'bostonmarathonmasc22'
    start_urls = ['https://registration.baa.org/2022/cf/Media/iframe_ResultsSearch.cfm?mode=detail']

    def parse(self, response):
        item = PropertiesItem()
        item['generalinfo'] = response.css('table.tablegrid_table').get()
        yield item