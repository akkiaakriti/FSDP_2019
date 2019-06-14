# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 12:24:00 2019

@author: Aakriti
"""


people = [{'name': 'Mary', 'height': 160},
                {'name': 'Isla', 'height': 80},
                {'name': 'Sam'}]

def add(height):
    height_total = 0
    height_count = 0
    for person in people:
        if height in person:
            height_total += person['height']
            height_count += 1
    return height


my_filter_list = filter ( add, people)
print(list(my_filter_list))

    
            