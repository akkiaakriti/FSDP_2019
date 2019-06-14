# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:44:21 2019

@author: Aakriti
"""


import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Udaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)


response = requests.get(url)
# requests.get(url,params={"q":"Jaipur", "appid"="e9185b28e9969fb7a300801eb026de9c"})
response.content
jsondata = response.json()

for key, value in jsondata.items():
    print (key, ":" ,value , "\n")
    

print(jsondata["coord"]["lon"])
print(jsondata["coord"]["lat"])
print(jsondata["wind"]["speed"])
print(jsondata["sys"]["sunrise"])
print(jsondata["sys"]["sunset"])
print(jsondata["weather"])