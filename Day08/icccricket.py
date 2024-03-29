# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:09:16 2019

@author: Aakriti
"""


from bs4 import BeautifulSoup
import requests

cricket="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source=requests.get(cricket).text

soup=BeautifulSoup(source,"lxml")
print(soup.prettify())

right_table=soup.find("table",class_="table")
print(right_table.prettify())


A=[]
B=[]
C=[]
D=[]
E=[]
for row in right_table.findAll('tr'):
    cells = row.findAll('td') 

    if len(cells) == 5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        
from collections import OrderedDict

col_name=["pos","team","weighted_matches","points","rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))


# If you want to store the data in a csv file
import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("icc.csv")

        
        
        
        
        
        
        
        