import scrapy
from ..items import AmazonItem
class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon"
    page_no = 2
    start_urls = [
        "https://www.amazon.in/s?bbn=1389401031&rh=n%3A1389401031%2Cp_36%3A1318507031&dc&qid=1696588365&rnid=1318502031&ref=lp_1389401031_nr_p_36_4"
        ]

    def parse(self, response):
        items = AmazonItem()
        all_div = response.css('div.s-card-border')
        for data in all_div:
            product_name = data.css('.a-color-base.a-text-normal::text').extract()
            price = data.css('.a-price-whole::text').extract()
            image_link = data.css('.s-image::attr(src)').extract()

            items['product_name'] = product_name
            items['price'] = price
            items['image_link'] = image_link

            yield items
        next_page ='https://www.amazon.in/s?i=electronics&bbn=1389401031&rh=n%3A1389401031%2Cp_36%3A1318507031&dc&page='+ str(AmazonSpiderSpider.page_no) +'&qid=1696839758&rnid=1318502031&ref=sr_pg_37'

        if AmazonSpiderSpider.page_no<=10:
            AmazonSpiderSpider.page_no += 1
            yield response.follow(next_page, callback = self.parse)