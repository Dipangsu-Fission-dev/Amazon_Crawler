import scrapy
# from amazon_crawler.items import Items
from gfg.gfg.items import Items

class AmazonSpider(scrapy.Spider):
    name = 'AmazonSpider'
    initial_url = ['https://www.amazon.com/Virtue-Signaling-Essays-Darwinian-Politics/dp/1951555007']
    domain = ['amazon.com']

    def parse(self,response):
        item = Items()
        title = response.xpath('//h1[@id="title"]/span/text()').extract()
        price = response.xpath('//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()').extract()
        available = response.xpath('//div[@id="availability"]//text()').extract()
        category = response.xpath('//a[@class="a-link-normal a-color-tertiary"]/text()').extract()
        item['name'] = ''.join(title).strip()
        item['price'] = ''.join(price).strip()
        item['category'] = ','.join(map(lambda i : i.strip(), category)).strip()
        item['available'] = ''.join(available).strip()
        yield item

