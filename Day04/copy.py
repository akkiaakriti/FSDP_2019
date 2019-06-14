# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:42:52 2019

@author: Aakriti
"""


with open ("words.txt", "rt") as rf:
  with open ("yadav.txt", "wt") as wf :
    for line in rf :
      wf.write ( line)

with open("yadav.txt","rt") as file:
    for line in file:
        print(line)
        
    

    