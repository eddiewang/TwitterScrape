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
	start_urls = ["https://twitter.com/search?q=nike&src=typd"]
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
			print("aggregating tweets! step: " + str(i) + " of " + str(count))
			i += 1
		hxs = Selector(text = self.driver.page_source)

		h = html2text.HTML2Text()
		content = hxs.xpath("//div[@class='content']")
		item = TwitterScrapeItem()
		raw_tweets = content.xpath("p[@class='js-tweet-text tweet-text']").extract()
		number = -1
		for stuff in content:
			number += 1
			#print raw_tweets[number]
			item['tweet'] = h.handle(raw_tweets[number])
			item['name'] = stuff.xpath("div[@class='stream-item-header']/a/span[@class='username js-action-profile-name']/b/text()").extract()
			yield item
		page.close()
			
#next_steps: NLTK for sentiment analysis (or use API) || Machine Learning might be cool to explore