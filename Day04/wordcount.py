# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:24:53 2019

@author: Aakriti
"""
    
with open("romeo2.txt","rt") as file:
    words=file.read().split()   

count_char={}
for i in words:
    if i in count_char:
        count_char[i]+=1
    else:
        count_char[i]=1
print("no.of words\n"+str(count_char))

with open("romeo2.txt","rt") as file:
    lines=file.readlines()
    print(lines)  

with open("romeo2.txt","rt") as file:
    words=file.read()
    print(words) 

count_words={}
for j in lines:
    if j in count_words:
        count_words[j]+=1
    else:
        count_words[j]=1
print("no.of words\n"+str(count_words))        
        
    