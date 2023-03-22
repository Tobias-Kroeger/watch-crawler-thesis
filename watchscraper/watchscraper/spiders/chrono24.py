import scrapy
from ..items import WatchscraperItem



# das scrapy.Spider ist Vererbung

class WatchSpiderChrono24(scrapy.Spider):
    name = 'chrono24'
    start_urls = [
        'https://www.chrono24.com/watches/pre-owned-watches--64.htm?SETLANG=en_US&SETCURR=EUR&goal_change_domain=1'
    ]

    def _parse(self, response):

        watches = response.css("js-article-item-list article-item-list article-list block")
        # response.css('div.article-item-container.wt-search-result a::attr(href)')
        for watch in watches:

            print("test")
            # yield response.follow(url, callback=self.parse_categories)

    # def parse_categories(self, response):
    #     print(response.url)