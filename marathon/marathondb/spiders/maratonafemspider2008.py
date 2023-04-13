import scrapy
from marathondb.items import PropertiesItem


class MaratonaFemSpider2008(scrapy.Spider):
	name = 'maratonafem2008'
	start_urls = ['https://www.worldathletics.org/competitions/olympic-games/the-xxix-olympic-games-6977748/results/women/marathon/final/result']
	
	def parse(self, response):
		item = PropertiesItem()
		for athletes in response.css('tr.TableCollapsible_row__3Rxm4'):
			item['name'] = athletes.css('a.ProfileLinks_main__1b_tF::text').get(),
			item['position'] = athletes.css('span.ResultsLOC_top3Val__2Dxi-::text').get(),
			item['country'] = athletes.css('span.Flags_container__3W63l > span::text').get(),
			item['mark'] = athletes.css('span.ResultsLOC_top3Val__2Dxi- > span::text').get(),
			item['competition'] = "The XXIX Olympic Games",
			item['sport'] = response.css('div.ResultsLOC_unitName__2Wlrh::text')[1].getall(),
			item['link'] = 'https://www.worldathletics.org' + athletes.css('a.ProfileLinks_main__1b_tF').attrib['href'],
			item['gender'] = "F"
			yield item