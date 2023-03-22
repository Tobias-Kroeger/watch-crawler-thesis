# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WatchscraperItem(scrapy.Item):
    # define the fields for your item here like:
    brand = scrapy.Field()
    model = scrapy.Field()
    reference = scrapy.Field()
    movement = scrapy.Field()
    size = scrapy.Field()
    gender = scrapy.Field()
    SKU = scrapy.Field()
    # price_discounted = scrapy.Field()
    price = scrapy.Field()
    time = scrapy.Field()
    source = scrapy.Field()



