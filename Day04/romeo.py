# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:29:27 2019

@author: Aakriti
"""

with open("romeo2.txt","rt") as file:
    lines=file.readlines()
    print(lines)

with open("romeo2.txt","rt") as file:
    words=file.read().split()
    print(words)
    
count={}
for i in words:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
    