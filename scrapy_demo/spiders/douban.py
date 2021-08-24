import scrapy
from scrapy_demo.items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['https://movie.douban.com/top250']
    start_urls = [
        'https://movie.douban.com/top250/',
        'https://movie.douban.com/subject/1292052/'
    ]

    # def start_requests(self):
    #     return [scrapy.FormRequest('https://movie.douban.com/top250/', callback=self.logged_in)]
    #
    # def logged_in(self, response):
    #     # here you would extract links to follow and return Requests for
    #     # each of them, with another callback
    #     pass

    def parse(self, response):
        self.log('parse...')
        items = DoubanItem()
        lists = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for i in lists:
            items['movie'] = i.xpath('./div/div[2]/div[1]/a/span[1]').get()
            items['href'] = i.xpath('./div/div[2]/div[1]/a/@href').get()

            yield items
