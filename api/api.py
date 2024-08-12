import requests
from bs4 import BeautifulSoup
import json
import os
from pprint import pprint

debug = 0

# Standard Amazon Webpage
url = 'https://german.alibaba.com/trade/search?spm=a2700.product_home_newuser.home_new_user_first_screen_fy23_pc_search_bar.associationItem_pos_0&tab=all&SearchText=elektro+scooter'

# Simple header for request (Needs to be fixed to excape bot detection)
headers = {
    "User-Agent": "Mozilla/5.0"
}

# This proxie should prevent IP locking
proxies = {
  'http': '89.145.162.81',
}

# Sending request to webpage
response = requests.get(url, proxies=proxies)

if response.status_code == 200:
  print("Successful connection \n")

  soup = BeautifulSoup(response.text, 'html.parser')
    
  # Find the span element with the class 'search-card-e-price__original'
  name_elements = soup.find_all('a',href=True)
  name_text = []
  
  for name in name_elements:
    if name.find('span'):
      name_text.append(name.find('span').text.strip())
      
  with open('response.txt','w') as text_write:
    for idx,name in enumerate(name_text):
      if idx > 18:
        break
      text_write.write(f'{idx}:{name}')
      text_write.write('\n')
      text_write.write('\n')
  
  name_text.clear()
  
  name_elements = soup.find_all('card-info list-card-layout__info')
  print(len(name_elements))
  
  price_elements = soup.find_all('div', class_="search-card-e-price-main")
  print(len(price_elements))
  for idx,name in enumerate(name_elements):
    if name.find('span'):
      name_text.append(name.find('span').text.strip())
    
    
    if price_elements[idx]:
      name_text.append(price_elements[idx].text.strip().replace('\xa0', ' '))

  with open('response.txt','a') as text_write:
    for idx,name in enumerate(name_text):
      if idx > 18:
        break
      text_write.write(f'{idx}:{name}')
      text_write.write('\n')
      text_write.write('\n')
        
      
      
  
  
  # with open('response.txt','w') as text_write:
  #   for idx, name in enumerate(name_elements):
  #     name_2 = name.text.strip().replace('\xa0', ' ')
  #     price_2 = price_elements[idx].text.strip().replace('\xa0', ' ')
  #     text_write.write(name_2)
  #     text_write.write('\n')
  #     text_write.write(price_2)
  #     text_write.write('\n')
  #     text_write.write('\n')
  #     text_write.write('\n')
      
  
elif ~debug:
  print(f"Failed to retrieve data. Status code: {response.status_code}")
else:
  # Prints the result
  soup = BeautifulSoup(response.content,'html.parser')
  print(soup)

