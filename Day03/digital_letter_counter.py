# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:55:34 2019

@author: Aakriti
"""
dict1={'letters':0,'digits':0}


string=input("enter string>>")
for item in string:
    if item in "qwertyuioplkjhgfdsazxcvbnm":
        dict1['letters']+=1
    elif item in "0123456789":
        dict1['digits']+=1
    else:
        continue
print(dict1)
    
        
        
    