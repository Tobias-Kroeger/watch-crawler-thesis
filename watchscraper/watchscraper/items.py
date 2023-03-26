# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class WatchscraperItem(Item):
    # define the fields for your item here like:
    brand = Field()
    model = Field()
    reference = Field()
    movement_type = Field()
    size = Field()
    gender = Field()
    SKU = Field()
    # price_discounted = scrapy.Field()
    price = Field()
    time = Field()
    source = Field()
    scope_of_delivery = Field()
    production_date = Field()
    availability = Field()
    location = Field()
    condition = Field()
    case_material = Field()
    strap_material = Field()
    strap_colour = Field()
    bezel_material = Field()
    glas = Field()
    dial = Field()
    clasp = Field()
    clasp_material = Field()
    movement = Field()
    extra = Field()
    features = Field()
    delivery_cost = Field()
    seller_type = Field()



