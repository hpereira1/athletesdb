import scrapy
from shotputdb.items import ShotputdbItem


class OGmen12Spider(scrapy.Spider):
    name = 'OGmen12'
    start_urls = ['https://worldathletics.org/competitions/olympic-games/the-xxx-olympic-games-6999193/results/men/shot-put/final/result']

    def parse(self, response):
        for athletes in response.css('tr.TableCollapsible_row__3Rxm4'):
            item = ShotputdbItem()
            item['name'] = athletes.css('a.ProfileLinks_main__1b_tF::text').get(),
            item['position'] = athletes.css('span.ResultsLOC_top3Val__2Dxi-::text').get(),
            item['country'] = athletes.css('span.Flags_name__28uFw::text').get(),
            item['mark'] = athletes.css('span.ResultsLOC_top3Val__2Dxi- > span::text').get(),
            item['competition'] = "The XXX Olympic Games",    
            item['link'] = 'https://www.worldathletics.org' + athletes.css('a.ProfileLinks_main__1b_tF').attrib['href'],
            item['sport'] = response.css('div.ResultsLOC_unitName__2Wlrh::text')[1].getall(),
            yield item