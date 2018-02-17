import scrapy
import csv


class IotaSpidy(scrapy.Spider):
    name = "spidy"
    u=[]
    with open('users/usernames.csv') as csvfile:
        readCSV= csv.reader(csvfile,delimiter=',')
        for row in readCSV:
            if(row[1]!='Username'):
                u.append('https://www.codechef.com/users/'+row[1])

    start_urls = u

    def parse(self, response):
        
        yield {
            'prob':  response.xpath('//main').xpath('div').xpath('div/div/div/div/section/div/article/p/span/a/text()').extract(),
        }