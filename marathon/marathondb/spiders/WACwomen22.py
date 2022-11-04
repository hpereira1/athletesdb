import scrapy
from marathondb.items import PropertiesItem


class WACwomen22Spider(scrapy.Spider):
    name = 'WACwomen22'
    start_urls = ['https://worldathletics.org/competitions/world-athletics-championships/world-athletics-championships-oregon-2022-7137279/results/women/marathon/final/result']

    def parse(self, response):
        for athletes in response.css('tr.TableCollapsible_row__3Rxm4'):
            item = PropertiesItem()
            item['name'] = athletes.css('a.ProfileLinks_main__1b_tF::text').get(),
            item['position'] = athletes.css('span.ResultsLOC_top3Val__2Dxi-::text').get(),
            item['country'] = athletes.css('span.Flags_name__28uFw::text').get(),
            item['mark'] = athletes.css('span.ResultsLOC_top3Val__2Dxi- > span::text').get(),
            item['competition'] = "World Athletics Championships, Oregon 2022",    
            item['sport'] = response.css('div.ResultsLOC_unitName__2Wlrh::text')[1].getall(),
            item['link'] = 'https://www.worldathletics.org' + athletes.css('a.ProfileLinks_main__1b_tF').attrib['href'],
            yield item