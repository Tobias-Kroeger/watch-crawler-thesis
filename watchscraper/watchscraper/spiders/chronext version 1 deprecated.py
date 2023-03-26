import scrapy
from ..items import WatchscraperItem



# das scrapy.Spider ist Vererbung

class WatchSpiderChronext(scrapy.Spider):
    name = "test1"

    start_urls = {
        "https://www.chronext.de/kaufen"
    }

    def parse(self, response):
        items = WatchscraperItem()

        all_div_watches = response.css(".product-tile")


        for watch in all_div_watches:
            # for watch in watch_div:
            brand = watch.css(".product-tile__brand::text").extract()
            reference = watch.css(".product-tile__reference::text").extract()
            model = watch.css(".product-tile__model::text").extract()
            # price = watch.css(".product-tile__reference::text").extract()

            items["brand"] = brand
            items["reference"] = reference
            items["model"] = model
            # items["price"] = price

            yield items

        next_page = response.css("li.pagination__item.pagination__item--next a::attr(href)").get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)