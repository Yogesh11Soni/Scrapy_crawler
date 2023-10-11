from typing import Any
import scrapy
from scrapy.http import Response
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    page_no = 2
    start_urls = [
        'https://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):
        items = QuotetutorialItem()
        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:

            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()
            
            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            yield items
           
            # yield{
            #     'title' : title,
            #     'author' : author,
            #     'tag' : tags
            # }

        # #Using Next button -->
        # next_page = response.css('li.next a::attr(href)').get()

        # if next_page is not None:
            # yield response.follow(next_page, callback = self.parse)
         
        # using pagination -->
        next_page = 'https://quotes.toscrape.com/page/'+str(QuoteSpider.page_no)+'/'
        
        if QuoteSpider.page_no < 11:
            QuoteSpider.page_no += 1
            yield response.follow(next_page, callback = self.parse)
