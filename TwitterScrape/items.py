# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

## MOVIE SCRAPER
#IMDB
#RottenTomatoes - Scrape Reviews
#FB - Brand Webpage Scrape
#Twitter - Talking
#LinkedIn - 
#Sentiment Analysis

class TwitterScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    tweet = scrapy.Field()
    name = scrapy.Field()
    # name = scrapy.Field()