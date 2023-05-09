import scrapy
from scrapy.crawler import CrawlerProcess
import os
import logging
import pandas as pd

# the list of cities we want the information for
destinations_to_scrape = ["Mont Saint Michel", "St Malo", "Bayeux", "Le Havre", "Rouen", "Paris", "Amiens", "Lille", "Strasbourg",\
"Chateau du Haut Koenigsbourg", "Colmar", "Eguisheim", "Besancon", "Dijon", "Annecy", "Grenoble", "Lyon", "Gorges du Verdon",\
"Bormes les Mimosas", "Cassis", "Marseille", "Aix en Provence", "Avignon", "Uzes", "Nimes", "Aigues Mortes", "Saintes Maries de la mer",\
"Collioure", "Carcassonne", "Ariege", "Toulouse", "Montauban", "Biarritz", "Bayonne", "La Rochelle"] 

class BookingHotels(scrapy.Spider):
    # the name of our spider
    name = 'booking_hotels_spider'
    
    # the domains it can it will be allowed to go on
    allowed_domains = ['booking.com']
    
    # our list of cities
    cities = destinations_to_scrape

    def start_requests(self):
        for city in self.cities:
            url = f'https://www.booking.com/searchresults.fr.html?ss={city}'
            yield scrapy.Request(url=url, callback=self.parse, meta={'city': city})

    def parse(self, response):
        city = response.meta['city']

        # to make sure we get the information for a specific hotel each time, we start
        # from the property card, that contains the name, description and so on. 
        hotels = response.xpath('//*[@data-testid="property-card"]')

        # then we loop for each hotels
        for hotel in hotels:
            yield{
            'city': city,
            'name': hotel.xpath('.//*[@class="fcab3ed991 a23c043802"]/text()').get(),
            'description': hotel.xpath('.//*[@class="a1b3f50dcd ef8295f3e6 f7c6687c3d"]/div[@class="d8eab2cf7f"]/text()').get(),
            'rating': hotel.xpath('.//*[@class="b5cd09854e d10a6220b4"]/text()').get(),
            'location': hotel.xpath('.//*[@class="f4bd0794db b4273d69aa" and contains (@data-testid, "address")]/text()').get(),
            'url': hotel.xpath('.//*[@class= "fc63351294 a168c6f285 e0e11a8307 a25b1d9e47"]/@href').get()
            }
            
# this is file that will hold the information we scraped
filename = 'booking_hotel_scraping_1.json'

# we check if the file already exist, in that case we delete it
if filename in os.listdir('src/'):
    os.remove ('src/' + filename)

# we define our process
process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    'FEEDS': {
        'src/' + filename : {'format': 'json'},
    }
})

process.crawl(BookingHotels)
process.start()