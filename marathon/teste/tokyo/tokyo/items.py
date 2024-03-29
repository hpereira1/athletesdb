# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field


class PropertiesItem(Item):
    name = Field()
    position = Field()
    country = Field()
    mark = Field()
    competition = Field()
    sport = Field()
    link = Field()
    gender = Field()