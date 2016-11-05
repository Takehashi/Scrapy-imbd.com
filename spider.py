# -*- coding: utf-8 -*-
import scrapy
import sys
from imbd.items import ImbdItem
class ImbdSpiderSpider(scrapy.Spider):
    name = "imbd_spider"
    allowed_domains = ["imdb.com"]
    start_urls = ()

    def parse(self, response):
    	
    	print response.url
    	title_movie= response.xpath('//td[@class="overview-top"]/h4/a/text()').extract()
    	length_title = len(title_movie)

    	if(length_title == 0):
			return  
      	# $x()
      	# read block
      	
      	
      	
      	#print block[0].xpath('//*[@id="main"]/div/div[2]/div[4]/table/tbody/tr[1]/td[2]/h4/a').extract() 
      	
      	#print block[1]
      	#print block[1].xpath('//td[@class="overview-top"]/h4/a/text()').extract()
      	tree = response.xpath('//td[@class="overview-top"]')
      	i = 0
      	for block in tree:
      		#print table	
      		title = block.xpath('.//h4[@itemprop="name"]/a/text()').extract()
      		author = block.xpath('.//span[@itemprop="director"]/span/a/text()')[i].extract()
      		rate = block.xpath('.//div[@class="metascore no_ratings"]/strong/text()')[i].extract()
      		time = block.xpath('.//time[@itemprop="duration"]/text()')[i].extract()
      		tag = block.xpath('.//span[@itemprop="genre"]/text()').extract()
      		des = block.xpath('.//div[@class="outline"]/text()')[i].extract()
		
		item = ScrapyIdbm(scrapy.item)
		item('title') = title
		item('author') = author
		item('rate') = rate
		item('time') = time
		item('tag') = tag
		item('des') = des
		yield item
      		# print title
      		# print author
      		# print rate
      		# print time
      		# print tag
      		# print des
      		#i = i + 1
      
       page = response.xpath('//div[@class="sort"]/a')
       page2 = page.xpath('//a[text()="Next"]/@href')
       nextpage = "http://www.imdb.com" + page2[0].extract() # /movie-coming-soon.
       yield scrapy.Request(nextpage, self.parse)

    def start_requests(self):
    	start = "http://www.imdb.com/movies-coming-soon/2017-12/"
    	yield self.make_requests_from_url(start)
