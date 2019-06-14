# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:48:44 2019

@author: Aakriti
"""

'''
import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

for i in range(len(names)):
    names[i] = random.choice(code_names)

print (names)
'''
import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

names=list(map(lambda i: random.choice(code_names),range(len(names))))
print(names)