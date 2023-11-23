import scrapy
from tokyo.items import PropertiesItem

class ChicagoSpider(scrapy.Spider):
    name = 'chicago'
    start_urls = ['https://worldathletics.org/competition/calendar-results/results/7176619?eventId=10229534&gender=W']
	
    def parse(self, response):
        N = 0
        item = PropertiesItem()
        for tr in response.css('table.styles_table__yjrQa tbody > tr'):
            item['name'] = tr.css('td.EventResults_name__3UzJp > a::text').get(),
            item['position'] = N + 1
            item['country'] = tr.css("span.Flags_name__28uFw::text").get(),
            item['mark'] = tr.css('td:nth-child(5)::text').get(),
            item['competition'] = "Bank of America Chicago Marathon - 09 OCT 2022",
            item['sport'] = "Marathon",
            item['gender'] = "F"
            yield item
            N+=1