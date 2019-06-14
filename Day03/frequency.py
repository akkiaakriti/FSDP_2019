# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:44:45 2019

@author: Aakriti
"""

freq={}
string=input("enter string")
for i in string:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)