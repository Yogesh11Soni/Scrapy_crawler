from typing import Iterable
import scrapy
from scrapy.http import Request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from ..items import FlipkartItem
import re


class FlipkartSpiderSpider(scrapy.Spider):
    name = "flipkart_spider"

    def start_requests(self):
        service = Service()
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  #runs without opening browser
        driver = webdriver.Chrome(service=service, options=options)

        driver.get("https://www.flipkart.com/search?q=novels&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

        xpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "s1Q9rs", " " ))]'
        link_elements = driver.find_elements(By.XPATH, xpath)

        for link in link_elements:
            href = link.get_attribute("href")
            yield scrapy.Request(href)
        len(link, '*'*50)
        len(link_elements, '*'*50)
        driver.quit()
        
    def parse(self, response):
        items = FlipkartItem()
        items['book_name'] = response.css('.B_NuCI::text').extract()
        items['price'] = response.css('._16Jk6d::text').extract()
        text = response.xpath('//*[contains(text(), "Pages:")]').get()
        items['pages'] = re.search(r'\d+', text).group()


        yield items 
