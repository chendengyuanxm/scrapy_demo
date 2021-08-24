import scrapy

from scrapy_demo.items import DoubanItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    start_urls = [
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        "https://phpkt.com/python/13.html"
    ]

    def parse(self, response, **kwargs):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
        for sel in response.xpath('/html/body/div[3]/div/div[1]/div[3]/ul/li'):
            item = DoubanItem()
            item['book'] = sel.xpath('a/text()').extract()
            yield item