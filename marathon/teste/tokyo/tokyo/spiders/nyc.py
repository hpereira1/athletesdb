import scrapy
from tokyo.items import PropertiesItem

class NycSpider(scrapy.Spider):
    name = 'nyc'
    start_urls = ['https://worldathletics.org/competition/calendar-results/results/7123902?eventId=10229634&gender=M']
	
    def parse(self, response):
        N = 0
        item = PropertiesItem()
        for tr in response.css('table.styles_table__yjrQa tbody > tr'):
            item['name'] = tr.css('td.EventResults_name__3UzJp > a::text').get(),
            item['position'] = N + 1
            item['country'] = tr.css("span.Flags_name__28uFw::text").get(),
            item['mark'] = tr.css('td:nth-child(5)::text').get(),
            item['competition'] = "New York Marathon - 04 NOV 2018",
            item['sport'] = "Marathon",
            item['gender'] = "M"
            yield item
            N+=1