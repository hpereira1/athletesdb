import scrapy
from shotputdb.items import ShotputdbItem

class DLWomenSpider17_paris(scrapy.Spider):
    name = 'dlwomen17_paris'
    start_urls = ['https://www.worldathletics.org/competitions/diamond-league/calendar-results/7104779/result?eventId=10229530&gender=W']

    def parse(self, response):
        N = 0
        for athletes in response.css('table.styles_table__yjrQa > tbody > tr'):
            item = ShotputdbItem()
            item['name'] = athletes.css('td.EventResults_name__3UzJp> a::text').get(),
            aux = athletes.css('span.ResultsLOC_top3Val__2Dxi-::text').get()
            item['position'] = N + 1
            item['country'] = athletes.css("span.Flags_name__28uFw::text").get(),
            item['mark'] = str(response.css("tbody tr td:nth-child(5)::text")[N].getall()),
            item['competition'] = "Meeting de Paris - 01 JUL 2017",
            item['sport'] = "Shot Put",
            item['gender'] = "F"
            yield item
            N+=1