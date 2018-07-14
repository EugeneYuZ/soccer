import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from soccer_reference.items import SoccerReferenceItem


class Myspider(scrapy.Spider):
    name = 'soccer_reference'
    url = 'https://fbref.com/en/squads/country/ENG/index.html'
    domain = 'https://fbref.com/'
    barshurl = 'index.html'

    def start_requests(self):
        yield Request(Myspider.url, self.parse)

    def parse(self, response):
        item = SoccerReferenceItem()
        ths = BeautifulSoup(response.text, 'lxml').find_all('th', {"data-stat": "squad"})
        for i in ths:
            if i.find('a') is not None:
                item['squad_name'] = i.find('a').get_text()
                y = i.find('a')['href']
                item['squad_url'] = self.domain + str(y) + '/' + self.barshurl
                yield item
