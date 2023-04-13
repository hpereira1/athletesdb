import scrapy
from marathondb.items import PropertiesItem


class WACmen19Spider(scrapy.Spider):
    name = 'WACmen19'
    start_urls = ['https://worldathletics.org/competitions/world-athletics-championships/iaaf-world-athletics-championships-doha-2019-7125365/results/men/marathon/final/result']

    def parse(self, response):
        for athletes in response.css('tr.TableCollapsible_row__3Rxm4'):
            item = PropertiesItem()
            item['name'] = athletes.css('a.ProfileLinks_main__1b_tF::text').get(),
            item['position'] = athletes.css('span.ResultsLOC_top3Val__2Dxi-::text').get(),
            item['country'] = athletes.css('span.Flags_name__28uFw::text').get(),
            item['mark'] = athletes.css('span.ResultsLOC_top3Val__2Dxi- > span::text').get(),
            item['competition'] = "IAAF World Athletics Championships, DOHA 2019",    
            item['sport'] = response.css('div.ResultsLOC_unitName__2Wlrh::text')[1].getall(),
            item['link'] = 'https://www.worldathletics.org' + athletes.css('a.ProfileLinks_main__1b_tF').attrib['href'],
            item['gender'] = "M"
            yield item