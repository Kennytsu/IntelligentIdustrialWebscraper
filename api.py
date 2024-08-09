import requests
from bs4 import BeautifulSoup
import json
import os


# Standard Amazon Webpage
url = 'https://www.amazon.com'

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

# Standard process to improve the response from the request
soup = BeautifulSoup(response.content, 'html.parser')

# Prints the result
print(soup)

