# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:39:05 2019

@author: Aakriti
"""

"""n=int(input("enter no.of items purchase in a day >"))
dict={}
for i in range(n):
    keys=input("enter key")
    values=int(input("enter value"))
    dict[keys]=values
print(dict)
dict1={}
dict1[keys]=set(dict)
"""
dict1={}
n=int(input("enter no. of "))
for i in range(n):
    string=input(">>>").split()
    if not string:
        break
    dict1[" ".join(string[:-1])]=string[-1]
    
print(dict1)
   
     
