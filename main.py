'''
Created on 04.06.2017

@author: Lukas
'''

import scrapy.cmdline

def main():
    #scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'quotes'])
    #scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'blogspider'])
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'pcgamerspider'])
    #scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'ignspider'])
    #scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'polygonspider'])

if  __name__ =='__main__':
    main()
