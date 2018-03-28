# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a script file for fetching information from E-commerce Website for products.
"""
import sys
import csv
#sys.setdefaultencoding('utf8')

import requests
from bs4 import BeautifulSoup

from urllib.request import urlopen as req

site = "https://urun.gittigidiyor.com/"
userInput = "mobile"
site= site + "?k=mobile" 
uCLient = req(site)
page = uCLient.read()

response = requests.get(site)
page = response.content
soup = BeautifulSoup(page,'html.parser')

items_block = soup.find('ul')

# Declare an empty List of Item attributes
list_of_items = []

# Declare an empty List of Items
Row_List = []

for item in items_block.findAll('li')[0:1]:
    itemurl = item.find_next('div').find_next('p').find_next('a')['href']
    list_of_items.append(itemurl)
    
    itemTitle = item.find_next('div').find_next('p').find_next('a')['title']
    list_of_items.append(itemTitle)
    
    itemprice = item.find('a', attrs  ={'itemprop':'price'})['href']
    list_of_items.append(itemprice)
    
    itemurl = "https:"+itemurl
    itemurlresponse = requests.get(itemurl)
    itempage = itemurlresponse.content
    itemsoup = BeautifulSoup((itempage), 'html.parser')
    ReviewCountDiv  = itemsoup.find('div', attrs = {'class':'counter-container'})
    
    viewedCount = ""
    for counterdiv in ReviewCountDiv.findAll('div',attrs = {'class':'number'}):
        viewedCount = counterdiv.text
        list_of_items.append(viewedCount)
    
    Row_List.append(list_of_items)
        
OutFile = open("./ItemList.csv","wb")
excelwriter= csv.writer(OutFile)
excelwriter.writerows(list_of_items)
    
    
        
        
#
