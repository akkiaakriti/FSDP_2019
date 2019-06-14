# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:04:31 2019

@author: Aakriti
"""
file=open("absentee.txt","wt")
while True:
    absents=input("enter name of students max 25>>")
    if not absents:
        break
    file.write(absents+"\n")
    
with open("absentee.txt","rt") as file:
    file_contents=file.read()
    print(file_contents)
 
        
    
    

    
  
    
    