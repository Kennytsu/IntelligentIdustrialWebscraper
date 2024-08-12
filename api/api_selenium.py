from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

proxy_address = 'http://89.145.162.81'
proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': proxy_address,
    'ftpProxy': proxy_address,
    'sslProxy': proxy_address,
    'noProxy': ''
})

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.add_argument('--incognito')

chrome_options.proxy = proxy

chromedriver_path = '/usr/bin/chromium-browser'
service = Service(chromedriver_path)

driver = webdriver.Chrome(service=chromedriver_path, options=chrome_options)

url = 'https://german.alibaba.com/trade/search?spm=a2700.product_home_newuser.home_new_user_first_screen_fy23_pc_search_bar.associationItem_pos_0&tab=all&SearchText=elektro+scooter'

driver.get(url)

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ip-address"))
    )
    ip_element = driver.find_element(By.ID, "ip-address")
    print(ip_element.text)
except Exception as e:
    print(e)
        



