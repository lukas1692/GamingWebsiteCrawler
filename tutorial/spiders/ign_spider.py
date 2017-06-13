'''
Created on 04.06.2017

@author: Lukas
'''

import scrapy
import re

from twisted.python.util import println

followed_domains = {}

class PcGamerSpider(scrapy.Spider):
    name = 'ignspider'
    start_urls = ['http://webcache.googleusercontent.com/search?sclient=psy-ab&q=cache%3Aign.com&oq=cache%3Aign.com&gs_l=serp.3...6512.6512.0.7023.1.1.0.0.0.0.0.0..0.0....1...1.1.64.psy-ab..1.0.0.JZqr0lB3bTU&pbx=1']
    #start_urls = ['http://www.pcgamer.com/stories-untold-review/']
    #allowed_domains = ['http://www.pcgamer.com/']
    

    def parse(self, response):
        
        print("a")
        for x in response.xpath('//body//p//text()').extract():
            
            if not re.match(".*[R|r]eview.*", response.url):
                break
            
            if re.match(".*[P|p]review.*", response.url):
                break
                
            if re.match(".*[A|a]tmosphere.*", str(x)) is not None: 
                page = response.url.split("/")[-2]
                
                
                filename = 'ign//%s.html' % page
                with open(filename, 'wb') as f:
                    f.write(response.body)
                break
            
             
            
            
        for next_page in response.xpath('//a'):
            
            
            link = next_page.xpath('@href').extract()
            
            if re.match("http://www.ign.com.*", link[0]) is not None:   
                yield response.follow(link[0], callback=self.parse)
                
                link_name = str(link[0])
                
                
                if(link_name not in followed_domains):
                    #println("follow: " + link_name)
                    followed_domains[link_name] = 1
                    yield scrapy.Request(link[0], callback=self.parse)
            
                    
        print(len(followed_domains))