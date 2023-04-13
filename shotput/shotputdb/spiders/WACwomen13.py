import scrapy
from shotputdb.items import ShotputdbItem


class WACwomen13Spider(scrapy.Spider):
    name = 'WACwomen13'
    start_urls = ['https://worldathletics.org/competitions/world-athletics-championships/14th-iaaf-world-championships-7003368/results/women/shot-put/final/result']

    def parse(self, response):
        for athletes in response.css('tr.TableCollapsible_row__3Rxm4'):
            item = ShotputdbItem()
            item['name'] = athletes.css('a.ProfileLinks_main__1b_tF::text').get(),
            item['position'] = athletes.css('span.ResultsLOC_top3Val__2Dxi-::text').get(),
            item['country'] = athletes.css('span.Flags_name__28uFw::text').get(),
            item['mark'] = athletes.css('span.ResultsLOC_top3Val__2Dxi- > span::text').get(),
            item['competition'] = "14th IAAF World Championships",    
            item['link'] = 'https://www.worldathletics.org' + athletes.css('a.ProfileLinks_main__1b_tF').attrib['href'],
            item['sport'] = "Shot Put",
            item['gender'] = "F"
            yield item