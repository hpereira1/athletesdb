import scrapy
from expytb.items import PropertiesItem


class MaratonaFemSpider2004(scrapy.Spider):
	name = 'maratonafem2004'
	start_urls = ['https://www.worldathletics.org/competitions/olympic-games/28th-olympic-games-6913163/results/women/marathon/final/result']
	
	def parse(self, response):
		item = PropertiesItem()
		for athletes in response.css('tr.TableCollapsible_row__3Rxm4'):
			item['name'] = athletes.css('a.ProfileLinks_main__1b_tF::text').get(),
			item['position'] = athletes.css('span.ResultsLOC_top3Val__2Dxi-::text').get(),
			item['country'] = athletes.css('span.Flags_container__3W63l > span::text').get(),
			item['mark'] = athletes.css('span.ResultsLOC_top3Val__2Dxi- > span::text').get(),
			item['BIB'] = athletes.css('div.ResultsLOC_centerText__1dIwe::text').get(),
			item['link'] = 'https://www.worldathletics.org' + athletes.css('a.ProfileLinks_main__1b_tF').attrib['href'],
			yield item