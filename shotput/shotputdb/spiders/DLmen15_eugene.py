import scrapy
from shotputdb.items import ShotputdbItem

class DLmenSpider15_eugene(scrapy.Spider):
    name = 'dlmen15_eugene'
    start_urls = ['https://www.worldathletics.org/competitions/diamond-league/calendar-results/7078660/result?eventId=10229619&gender=M']

    def parse(self, response):
        N = 0
        for athletes in response.css('table.styles_table__yjrQa > tbody > tr'):
            item = ShotputdbItem()
            item['name'] = athletes.css('td.EventResults_name__3UzJp> a::text').get(),
            aux = athletes.css('span.ResultsLOC_top3Val__2Dxi-::text').get()
            item['position'] = N + 1
            item['country'] = athletes.css("span.Flags_name__28uFw::text").get(),
            item['mark'] = str(response.css("tbody tr td:nth-child(5)::text")[N].getall()),
            item['competition'] = "Eugene Prefontaine Classic - 29–30 MAY 2015",
            item['sport'] = "Shot Put",
            item['gender'] = "M"
            yield item
            N+=1