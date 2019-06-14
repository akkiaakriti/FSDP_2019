# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 13:16:26 2019

@author: Aakriti
"""



import csv

with open("population.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        print ( row )
        
