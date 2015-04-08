import scrapy
import html2text
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from TwitterScrape.items import TwitterscrapeItem
from scrapy.selector import 
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

		while True:
			next = self.driver.
		n = 10
		h = html2text.HTML2Text()
		hxs = HtmlXPathSelector(response)
		names = hxs.select("//span[@class='username js-action-profile-name']")
		tweets = hxs.select("//p[@class='js-tweet-text tweet-text']")
		for name in names:
			username = name.select("b/text()").extract()
			print username
		for tweet in tweets:
			content = tweet.extract()
			print h.handle(content)

