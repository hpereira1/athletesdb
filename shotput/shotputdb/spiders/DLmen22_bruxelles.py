import scrapy
from shotputdb.items import ShotputdbItem

class DLmenSpider22_bruxelles(scrapy.Spider):
    name = 'dlmen22_bruxelles'
    start_urls = ['https://www.worldathletics.org/competitions/diamond-league/calendar-results/7153974/result?eventId=10229619&gender=M']

    def parse(self, response):
        N = 0
        for athletes in response.css('table.styles_table__yjrQa > tbody > tr'):
            item = ShotputdbItem()
            item['name'] = athletes.css('td.EventResults_name__3UzJp> a::text').get(),
            aux = athletes.css('span.ResultsLOC_top3Val__2Dxi-::text').get()
            item['position'] = N + 1
            item['country'] = athletes.css("span.Flags_name__28uFw::text").get(),
            item['mark'] = str(response.css("tbody tr td:nth-child(5)::text")[N].getall()),
            item['competition'] = "Memorial Van Damme - 01–02 SEP 2022",
            item['sport'] = "Shot Put",
            item['gender'] = "M"
            yield item
            N+=1