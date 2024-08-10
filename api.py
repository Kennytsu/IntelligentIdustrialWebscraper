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
  price_elements = soup.find_all('span', class_='search-card-e-price')
  print(price_elements)
  
  for idx, price_element in enumerate(price_elements):
    price = price_element.text.strip().replace('\xa0', ' ')
    print(f"Price {idx + 1}: {price}")
elif ~debug:
  print(f"Failed to retrieve data. Status code: {response.status_code}")
else:
  # Prints the result
  soup = BeautifulSoup(response.content,'html.parser')
  print(soup)

