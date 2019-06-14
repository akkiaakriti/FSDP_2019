# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:44:54 2019

@author: Aakriti
"""

str="the quick brown fox jumps over the lazy dog"
def pangram(str):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if not char in str.lower():
            return True
    return False
if (pangram(str)==True):
    print("yes pangram")
else:
    print("no")
    
