'''
Created on 04.06.2017

@author: Lukas
'''

import scrapy
import re

from twisted.python.util import println

followed_domains = {}

class PcGamerSpider(scrapy.Spider):
    name = 'polygonspider'
    start_urls = ['https://www.polygon.com/games/reviewed']
    #start_urls = ['http://www.pcgamer.com/stories-untold-review/']
    #allowed_domains = ['http://www.pcgamer.com/']
    

    def parse(self, response):
        
        
        for x in response.xpath('//body//p//text()').extract():
            
            if not re.match(".*[R|r]eview.*", response.url):
                break
            
            if re.match(".*[P|p]review.*", response.url):
                break
                
            if re.match(".*[A|a]tmosphere.*", str(x)) is not None: 
                page = response.url.split("/")[-2]
                
                
                filename = 'polygon//%s.html' % page
                with open(filename, 'wb') as f:
                    f.write(response.body)
                break
            
             
            
            
        for next_page in response.xpath('//a'):
            link = next_page.xpath('@href').extract()
            
            if re.match("https://www.polygon.com.*", link[0]) is not None:   
                yield response.follow(link[0], callback=self.parse)
                
                link_name = str(link[0])
                
                
                if(link_name not in followed_domains):
                    #println("follow: " + link_name)
                    followed_domains[link_name] = 1
                    yield scrapy.Request(link[0], callback=self.parse)
            
                    
        print(len(followed_domains))