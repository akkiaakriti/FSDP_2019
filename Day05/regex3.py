# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 13:21:14 2019

@author: Aakriti
"""


card=[]
n=int(input("enter the no.of credit cards>>"))

for i in range(n):
    st=input("enter the credit card no. \n")
    card.append(st)
print(card)
import re
#check whether valid or not card
for num in card:
    if re.search(r'^[456]+[0-9]{15}$',num):
        print(True)
    else:
        print(False)
        
        
