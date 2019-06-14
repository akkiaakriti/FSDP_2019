# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 13:50:50 2019

@author: Aakriti
"""


with open('simpsons_phone_book.txt', mode='rt') as file :
   file_contents = file.readlines()
   print (file_contents)
   
str1=[]
str2=list(file_contents)
print(str2)
import re
for item in str2:
    if re.findall(r'^J[a-z]*\sNeu\s\d*',item):
        str1.append(item)
print(str1)