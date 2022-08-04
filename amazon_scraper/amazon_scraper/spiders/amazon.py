import scrapy
from quickscraper_sdk import QuickScraper


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def start_requests(self):
        client = QuickScraper('API_KEY')
        yield scrapy.Request(client.scrapyGet('https://www.amazon.com/dp/B08QMB94YW'), self.parse)

    def parse(self, response):
        yield {
            'name': response.css('span#productTitle::text').get(),
            'price': response.css('#corePriceDisplay_desktop_feature_div .a-offscreen::text').get(),
            'image': response.css('#imgTagWrapperId > img::attr(src)').get(),
            'asin': response.css('#productDetails_detailBullets_sections1 .prodDetAttrValue::text').get(),
            'brand': response.css('.po-brand > .a-span9 > span::text').get()
        }
