# -*- coding: utf-8 -*-

import scrapy

class Job(scrapy.Item):
    name = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()

    def __str__(self):
        return  "Open position for {} at {} located at {}".format(self['name'], self['company'], self['location'])  

def main():
    myJ = Job()
    myJ['name'] = "SwDev"
    myJ['company'] = "Premium"
    myJ['location'] = "LX"
    print(myJ)

if __name__ == "__main__":
    main()
