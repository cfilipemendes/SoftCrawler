# -*- coding: utf-8 -*-
import scrapy
from scrapy import selector
from ..items import Job

# -----------------------------------------------------------
# A spider for software developer jobs at www.indeed.pt
# -----------------------------------------------------------

class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    allowed_domains = ['indeed.pt']
    start_urls = ['https://www.indeed.pt/jobs?q=software+developer']
   

    def __init__(self, debug=0, *args, **kwargs):
        super(IndeedSpider, self).__init__(*args, **kwargs)
        self.runType = (int(debug) == 1)
        self.initial_depth = 40
        self.currentVisited = 0
        self.base_url = 'https://www.indeed.pt/jobs?q=software+developer'

    def parse(self, response):
        if(self.currentVisited >= self.initial_depth):
            print("Stopping")
            return

        if(self.runType):
            scrapy.shell.open_in_browser(response)
        allJobs = response.xpath("//*[@id='resultsCol']/div[contains(@class,'jobsearch-SerpJobCard')]")
        for jobCard in allJobs: 
            yield self.processJobCard(jobCard)

        self.currentVisited+=1
        print("NEXT PAGE")
        nextPage = self.base_url + "&start=" + str((self.currentVisited+1)*10)
        print(nextPage)
        yield scrapy.Request(nextPage, callback=self.parse)


    def processJobCard(self, jobCard):
        title = (''.join(jobCard.xpath("div[@class='title']/a//text()").getall())).replace('\n',''),
        company =  (''.join(jobCard.xpath("div[@class='sjcl']/div/span[@class='company']//text()").getall())).replace('\n',''),
        location = (''.join(jobCard.xpath("div[@class='sjcl']/*[contains(@class,'location')]//text()").getall())).replace('\n','')
        job = Job(name=title,company=company,location=location)
        return job

"""     def parse(self, response):
         """
            

