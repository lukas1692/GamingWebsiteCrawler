'''
Created on 04.06.2017

@author: Lukas
'''

import scrapy
import re
import urllib.request
from twisted.python.util import println

api_endpoint = 'http://selectpdf.com/api2/convert/'
key = '!insert your key here!'
# Get Key: http://selectpdf.com/api/RequestKey.aspx
write_pdf = False

followed_domains = {}

class PcGamerSpider(scrapy.Spider):
    name = 'pcgamerspider'
    start_urls = ['http://www.pcgamer.com/']
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
               
            #if re.match('datetime="2017', str(x)):
            #    print("found") 
                
                filename = 'pcgamer//%s.html' % page
                with open(filename, 'wb') as f:
                    f.write(response.body)
                    
            
                if not write_pdf:
                    continue
            
                try:
                    request = urllib.request.Request(api_endpoint)
                    request.add_header('Content-Type', 'application/json')
                    
                    print("open")
                    result = urllib.request.urlopen('http://selectpdf.com/api2/convert/?key='+ key + '&url=' + response.url + '')
                    localFile = open("pcgamer_pdf/"+page+".pdf", 'wb')
                    localFile.write(result.read())
                    localFile.close()
                    print("Test pdf document generated successfully!")
                except:
                    print("An error occurred!")
            
             
            
            
        for next_page in response.xpath('//a'):
            link = next_page.xpath('@href').extract()
            
            if re.match("http://www.pcgamer.com.*", link[0]) is not None:   
                yield response.follow(link[0], callback=self.parse)
                
                link_name = str(link[0])
                
                
                if(link_name not in followed_domains):
                    #println("follow: " + link_name)
                    followed_domains[link_name] = 1
                    yield scrapy.Request(link[0], callback=self.parse)
            
                    
        #print(len(followed_domains))
                
                
                
                
                

        
        