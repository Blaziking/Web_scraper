import scrapy

from downtoearth.items import DowntoearthItem

class downtoearthspider(scrapy.Spider):
		name = "downtoearth"
		allowed_domains = ["downtoearth.org.in"]

		start_urls = ['http://www.downtoearth.org.in/news/use-of-triclosan-in-popular-brand-of-toothpaste-raises-concern-over-usfda-processes-45775']

		def parse(self, response):
			item = DowntoearthItem()
			item['heading']= response.xpath('/html/head/title/text()').extract()
			item['content'] = response.xpath('//div[@id ="main_article_content"]/p/text()').extract()
			yield item

			print(title, content)
			
