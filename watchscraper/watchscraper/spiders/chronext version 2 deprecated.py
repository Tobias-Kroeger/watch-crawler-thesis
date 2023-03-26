import scrapy
from ..items import WatchscraperItem


# das scrapy.Spider ist Vererbung

class WatchSpiderChronext2(scrapy.Spider):
    name = "test2"
    offset = 24
    start_urls = {
        "https://www.chronext.de/kaufen?s%5Bef5bfee0-c7d4-470e-82e2-39d397cb3750%5D%5Boffset%5D=0"
    }

    def parse(self, response):
        items = WatchscraperItem()

        all_div_watches = response.css(".product-tile")
        # all_div_watches = response.css("div.product-tile")

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

        next_page = "https://www.chronext.de/kaufen?s%5Bef5bfee0-c7d4-470e-82e2-39d397cb3750%5D%5Boffset%5D="+str(WatchSpider.offset)

        if response.css("li.pagination__item.pagination__item--next a::attr(href)").get() is not None:
            WatchSpider.offset += 24
            yield response.follow(next_page, callback=self.parse)



