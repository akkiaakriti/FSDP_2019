# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:56:16 2019

@author: Aakriti
"""


def hash1(name):
    name = hash(name)
    return name

names = ['Mary', 'Isla', 'Sam']
names=list(map(hash1,names))
print(names)

