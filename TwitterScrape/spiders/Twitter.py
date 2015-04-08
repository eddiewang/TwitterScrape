import scrapy
import html2text
from scrapy.selector import Selector
from scrapy.http import Request
from TwitterScrape.items import TwitterScrapeItem
import time
#selenium
from selenium import webdriver


class TwitterScraper(scrapy.Spider):
	name = "twitter"
	allowed_domains = ["twitter.com"]
	start_urls = ["https://twitter.com/search?q=Nike&src=typd"]
	def __init__(self):
		self.driver = webdriver.Firefox()


	def parse(self, response):
		self.driver.get(response.url)
		time.sleep(2)
		i = 0
		while i < 50:
			self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(2)
			i += 1
		hxs = Selector(text = self.driver.page_source)

		h = html2text.HTML2Text()
		content = hxs.xpath("//div[@class='content']")
		item = TwitterScrapeItem()
		for stuff in content:
			item['tweet'] = stuff.xpath("p[@class='js-tweet-text tweet-text']/text()").extract()
			item['name'] = stuff.xpath("div[@class='stream-item-header']/a/span[@class='username js-action-profile-name']/b/text()").extract()
			yield item
			
#next_steps: NLTK for sentiment analysis (or use API) || Machine Learning might be cool to explore