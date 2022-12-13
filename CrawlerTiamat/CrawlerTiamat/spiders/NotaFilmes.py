import scrapy


class NotafilmesSpider(scrapy.Spider):
    name = 'NotaFilmes'
    allowed_domains = ['raw.githubusercontent.com']
    start_urls = ['http://raw.githubusercontent.com/']

    def parse(self, response):
        pass
