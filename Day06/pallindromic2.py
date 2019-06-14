# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:44:29 2019

@author: Aakriti
"""

user=[int(i) for i in input("enter no.s >>").split(",")]
print(user)

pallindrome=list(map(lambda i:True if str(i)==str(i)[:-1] else False ,user))
positive=(map(lambda i:True if i>0 else False ,user))
#print pallindrome and positive
print(any(pallindrome)or all(positive))