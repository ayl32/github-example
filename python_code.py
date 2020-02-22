import pandas as pd
import numpy as np
import requests

wikipedia='https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
raw_wikipedia_page= requests.get(wikipedia).text

$ pip install beautifulsoup4
from bs4 import BeautifulSoup
soup = BeautifulSoup(raw_wikipedia_page,'xml')
table = soup.find('table')
Postcode = []
Borough = []
Neighbourhood = []

for tr_cell in table.find_all('tr'):
    
    counter = 1
    Postcode_var      = -1
    Borough_var       = -1
    Neighbourhood_var = -1
    
for td_cell in tr_cell.find_all('td'):
    if counter == 1: 
        Postcode_var = td_cell.text
    if counter == 2: 
        Borough_var = td_cell.text
        tag_a_Borough = td_cell.find('a')
            
    if counter == 3: 
        Neighbourhood_var = str(td_cell.text).strip()
        tag_a_Neighbourhood = td_cell.find('a')
            
        counter +=1
        
    if (Postcode_var == 'Not assigned' or Borough_var == 'Not assigned' or Neighbourhood_var == 'Not assigned'):
            continue
               
    try:
        if ((tag_a_Borough is None) or (tag_a_Neighbourhood is None)):
            continue
                    
    except:
            pass
    
    if(Postcode_var == -1 or Borough_var == -1 or Neighbourhood_var == -1):
            continue
        
    Postcode.append(Postcode_var)
    Borough.append(Borough_var)
    Neighbourhood.append(Neighbourhood_var)
