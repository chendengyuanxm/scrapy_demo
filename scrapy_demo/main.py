from scrapy import cmdline

cmdline.execute('scrapy crawl douban'.split())
cmdline.execute('scrapy crawl douban -o items.json'.split())