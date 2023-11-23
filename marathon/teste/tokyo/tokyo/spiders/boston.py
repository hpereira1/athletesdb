import scrapy
from tokyo.items import PropertiesItem

class BostonSpider(scrapy.Spider):
    name = 'boston'
    start_urls = ['https://worldathletics.org/competition/calendar-results/results/7192122?eventId=10229534&gender=W']
	
    def parse(self, response):
        N = 0
        item = PropertiesItem()
        for tr in response.css('table.styles_table__yjrQa tbody > tr'):
            item['name'] = tr.css('td.EventResults_name__3UzJp > a::text').get(),
            item['position'] = N + 1
            item['country'] = tr.css("span.Flags_name__28uFw::text").get(),
            item['mark'] = tr.css('td:nth-child(5)::text').get(),
            item['competition'] = "Boston Marathon - 17 APR 2023",
            item['sport'] = "Marathon",
            item['gender'] = "F"
            yield item
            N+=1