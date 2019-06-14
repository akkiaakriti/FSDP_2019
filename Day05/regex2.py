# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:20:39 2019

@author: Aakriti
"""
string=[]
n=int(input("enter the no.of emails>>"))

for i in range(n):
    st=input("enter the email address\n")
    string.append(st)
print(string)

str1=[]
import re
for item in string:
    if re.search(r'^[a-z0-9-_]+\@\w+\.[a-z]{2,4}$',item):
        str1.append(item)
print(str1)
print(sorted(str1))