import scrapy
from scrapy.crawler import CrawlerProcess
import os
import logging
import pandas as pd


df_booking = pd.read_csv('booking_scraping_df.csv')

# we store the urls to in an empty list
urls = []

for url in (df_booking['url']):
    urls.append(url)

urls

#now we are going to scrap the last bit of information we need, the latitude and longitude of each hotels.

class LatLonBookingHotels(scrapy.Spider):
    name = 'booking_hotels_spider_latlon'

    def start_requests(self):
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        results = response.css('#hotel_address')
        for i in results:
            yield{'lat_lon': i.css('::attr(data-atlas-latlng)').get()}

filename = 'booking_hotel_scraping_2.json'

# we check if the file already exist, in that case we delete it
if filename in os.listdir('src/'):
    os.remove ('src/' + filename)

# we define our process
process = CrawlerProcess(settings = {
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'LOG_LEVEL': logging.INFO,
    'FEEDS': {
        'src/' + filename : {'format': 'json'},
    }
})

process.crawl(LatLonBookingHotels)
process.start()