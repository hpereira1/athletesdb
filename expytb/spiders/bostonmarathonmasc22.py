import scrapy
from expytb.items  import PropertiesItem


class BostonMarathonMasc22(scrapy.Spider):
    name = 'bostonmarathonmasc22'
    start_urls = ['https://registration.baa.org/2022/cf/Media/iframe_ResultsSearch.cfm?mode=detail']

    def parse(self, response):
        item = PropertiesItem()
        for athletes in response.css('td.tablegrid_list_item'):
            item['generalinfo'] = athletes.css('tr.tr_header').get()
            item['generalinfo2'] = athletes.css('table.table_infogrid').get()
            item['competition'] = 'bostonmarathonmasc22'
            yield item