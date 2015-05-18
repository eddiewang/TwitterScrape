import scrapy
import html2text
from scrapy.selector import Selector
from scrapy.http import Request
from TwitterScrape.items import TwitterScrapeItem
import time
#selenium macro headless driver
from selenium import webdriver


class TwitterScraper(scrapy.Spider):
	name = "twitter"
	allowed_domains = ["twitter.com"]
	start_urls = ["https://twitter.com/search?q=nike&src=typd&vertical=default"] #paste in twitter stream URL
	def __init__(self):
		self.driver = webdriver.PhantomJS()
		self.driver.set_window_size(1120, 550)


	def parse(self, response):
		self.driver.get(response.url)
		time.sleep(2)
		i = 0
		count = 2
		while i < count:
			self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(2)
			i += 1
			print("aggregating tweets! step: " + str(i) + " of " + str(count))
		hxs = Selector(text = self.driver.page_source)
		h = html2text.HTML2Text()
		item = TwitterScrapeItem()
		raw_tweets = hxs.xpath("//p[contains(@class,'tweet-text')]").extract()
		raw_names = hxs.xpath("//span[contains(@class, 'username')]/b/text()").extract()
		#test
		# for tweets in raw_tweets:
		# 	print tweets
		counter = 0
		for tweets in raw_tweets:
			#print raw_tweets[number]
			item['tweet'] = h.handle(raw_tweets[counter])
			item['name'] = raw_names[counter]
			counter += 1
			yield item
		self.driver.quit()

class IMDBScraper(scrapy.Spider):
	name = "imdb"
	allowed_domains = ["imdb.com"]
	start_urls = ["http://www.imdb.com/title/tt0377092/reviews"]
	
			
#next_steps: NLTK for sentiment analysis (or use API) || Machine Learning might be cool to explore