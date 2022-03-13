import scrapy
from expytb.items import PropertiesItem


class MaratonaMascGeral(scrapy.Spider):
	name = 'maratonamascgeral'
	start_urls = [
		'https://www.worldathletics.org/competitions/olympic-games/27th-olympic-games-6951910/results/men/marathon/final/result', 
		'https://www.worldathletics.org/competitions/olympic-games/28th-olympic-games-6913163/results/men/marathon/final/result',
        'https://www.worldathletics.org/competitions/olympic-games/the-xxix-olympic-games-6977748/results/men/marathon/final/result',
        'https://www.worldathletics.org/competitions/olympic-games/the-xxx-olympic-games-6999193/results/men/marathon/final/result',
        'https://www.worldathletics.org/competitions/olympic-games/the-xxxi-olympic-games-7093747/results/men/marathon/final/result',
        'https://www.worldathletics.org/competitions/olympic-games/the-xxxii-olympic-games-athletics-7132391/results/men/marathon/final/result'
    ]

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
		print()