import scrapy
import lxml.etree
from maoyan.items import MaoyanItem
from scrapy.selector import Selector


class MoivesSpider(scrapy.Spider):
    name = 'moives'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #    pass
    def parse(self, response):
        prefix_url = 'https://maoyan.com'
        tags = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')[:10]
        for tag in tags:
            url = prefix_url + tag.xpath('./a/@href').extract_first()
            #print(url) 
            yield scrapy.Request(url=url, callback=self.parse2)

    def parse2(self, response):
        item = MaoyanItem()
        movie_brief = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        film_name = movie_brief.xpath('./h1/text()').extract()
        #all_list = Selector(response=response).xpath('//li[@class="ellipsis"][1]')
        #film_types_tag = all_list.xpath('./a[@class="text-link"]')
        #film_types = ''
        # for tag in film_types_tag:
        #     film_type = tag.xpath('text()').extract_first().strip()
        #     film_types = film_types + film_type + '/'
        # film_types = film_types[:-1]
        film_types = movie_brief.xpath('./ul/li/a/text()').extract()
        plan_date = movie_brief.xpath('./ul/li[last()]/text()').extract()

        #plan_date = Selector(response=response).xpath('//li[@class="ellipsis"][3]/text()').extract_first()[:10]

        item['film_name'] = film_name
        item['film_types'] =  [film_type.strip() for film_type in film_types]
        item['plan_date'] = plan_date

        yield item
