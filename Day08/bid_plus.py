# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:25:01 2019

@author: Aakriti
"""


from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS
url="https://bidplus.gem.gov.in/bidlists"

browser=webdriver.Chrome("C:/Users/Aakriti/Downloads/chromedriver.exe")
browser.get(url)

sleep(2)
