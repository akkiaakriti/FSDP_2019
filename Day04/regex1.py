# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:36:41 2019

@author: Aakriti
"""

import re
string=[]
string1=[]
while True:
    user=input("enter the string (number)>>")
    string.append(user)
    if not user:
        break
string1=string[:-1]
print(string1)

#check
for i in string1:
    if re.findall(r'^[+-.]?[0-9]*\.[0-9]+$',i):
        print(True)
    else:
        print(False)


