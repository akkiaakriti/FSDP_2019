# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:28:03 2019

@author: Aakriti
"""
days=('Monday', 'Wednesday', 'Thursday', 'Saturday')
missing_days= ( 'Tuesday', 'Friday', 'Sunday')
list1=list(days)
list2=list(missing_days)

list3=[list1[0],list2[0],list1[1],list1[2],list2[1],list1[3],list2[2]]
print(tuple(list3))


    