import datetime

import scrapy
from ..items import WatchscraperItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


# das scrapy.Spider ist Vererbung
#Todo Dies ist die funktionierende Lösung
#Todo implementiert werden sollte noch, dass bereits gecrawlte Seiten beim Neustart nicht erneut gecrawlt werden
class WatchSpiderChronext3(CrawlSpider):
    custom_settings = {
        'CONCURRENT_REQUESTS': 64
    }
    name = "watch"
    allowed_domains = ["chronext.de"]
    start_urls = {
        "https://www.chronext.de/kaufen?s%5Bef5bfee0-c7d4-470e-82e2-39d397cb3750%5D%5Boffset%5D=0"
    }
    custom_settings = {
        'DUPEFILTER_CLASS': 'scrapy.dupefilters.RFPDupeFilter'
    }

    # https://www.chronext.de/kaufen

    # erstellt durch: response.css(".o-cell--3 a::attr(href)").extract()
    # response.css(".o-cell--3 a::text").extract()  für die Namen
    uhrenmarken = ('/a-lange+soehne', '/arnold+son', '/audemars-piguet', 'bell+ross', '/blancpain', '/boucheron',
                   '/breguet', '/breitling', '/bremont', '/bulgari', '/cartier', '/chanel', '/chopard', '/chronoswiss',
                   '/cvstos', '/fortis', '/franck-muller', 'girard-perregaux', '/glashuette-original', '/graham',
                   '/grand-seiko', '/h-moser+cie', '/hanhart', '/hermes', '/heuer', '/hublot', '/iwc',
                   '/jaeger-lecoultre', '/linde-werdelin', '/longines', '/maurice-lacroix', '/montblanc', '/morgenwerk',
                   '/nomos', '/omega', '/oris', '/panerai', '/patek-philippe', '/piaget', '/porsche-design',
                   '/roger-dubuis', '/rolex', '/sinn', '/tag-heuer', '/tudor', '/u-boat', '/ulysse-nardin',
                   '/vacheron-constantin', '/zenith')

    rules = (
        Rule(LinkExtractor(allow=r"kaufen", deny=uhrenmarken)),
        Rule(LinkExtractor(allow=uhrenmarken), callback="parse_item", follow=True)
    )

    def parse_item(self, response):
        items = WatchscraperItem()

        # marker = response.css(".specification__title::text").extract()
        # values = response.css(".specification__value::text").extract()
        values = response.css(".specification__wrapper div::text").extract()

        print(values)
        if len(values) > 0:
            try:
                brand = values[values.index("Marke") + 1]
            except:
                brand = None
            try:
                model = values[values.index("Modell") + 1]
            except:
                model = None
            try:
                reference = values[values.index("Referenz") + 1]
            except:
                reference = None
            try:
                movement = values[values.index("Werk") + 1]
            except:
                movement = None
            try:
                size = values[values.index("Abmessungen") + 1]
            except:
                size = None
            try:
                gender = values[values.index("Geschlecht") + 1]
            except:
                gender = None
            try:
                SKU = values[values.index("SKU") + 1]
            except:
                SKU = None

            # price_discounted = response.css(".price--discounted::text").extract()
            #
            # price = response.css(".price::text").extract()
            # if price is None:
            #     price = response.css(".price--strike::text").extract()
            # items["price"] = price
            #
            # if price_discounted is not None:
            #     items["price_discounted"] = price_discounted
            # else:
            #     items["price_discounted"] = None
            price = response.css(".product-stage__price-wrapper div::text").extract()
            items["price"] = price

            items["brand"] = brand
            items["model"] = model
            items["reference"] = reference
            items["movement"] = movement
            items["size"] = size
            items["gender"] = gender
            items["SKU"] = SKU
            items["time"] = datetime.datetime.now()
            items["source"] = "chronext"

            if brand is not None:
                yield items
