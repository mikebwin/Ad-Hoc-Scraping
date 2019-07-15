import requests
import re
from bs4 import BeautifulSoup
from lxml.html import fromstring
def get_proxies():
    url = 'http://spys.one/en/'
    response = requests.get(url)
    html = response.text
    print(html)
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.findAll('font', {"class": "spy14"})
    proxies = set()
    # for i in parser.xpath("//tr[contains(@class, 'spy1xx')]/td/font]"):
    # for i in elements:
    #     for item in i.children:
    #         print(item)
            # if re.match("\d*\.\d*", item.string):
            #     # print(item)
            #     proxies.add(item.string)
            # if re.match(":\d*", item.string):
            #     print(item)
    #     if i.xpath('.//td[7][contains(text(),"yes")]'):
    #         #Grabbing IP and corresponding PORT
    #         proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
    #         proxies.add(proxy)
    # return proxies


get_proxies()