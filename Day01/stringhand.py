# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 13:41:24 2019

@author: Aakriti
"""

str= input("enter full name>")
#help (str.find)
str1=str.find(" ")
str2=str[:str1]
str3=str[str1:]
print(str3,str2)