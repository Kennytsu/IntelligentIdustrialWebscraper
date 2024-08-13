from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys
import time


option = webdriver.ChromeOptions()
option.add_argument("--no-sandbox")
option.add_argument("--disable-dev-shm-usage")
option.add_argument("--remote-debugging-port=9222")
option.add_argument("--headless")
driver = webdriver.Chrome(options=option)

driver.get('https://www.alibaba.com/trade/search?spm=a2700.product_home_newuser.home_new_user_first_screen_fy23_pc_search_bar.associationItem_pos_0&tab=all&SearchText=elektro+scooter')
driver.save_screenshot('screenshot.png')


items = driver.find_elements(By.CLASS_NAME, "card-info")
print(len(items))

# Extract and send data to the backend

driver.save_screenshot('screenshot.png')
driver.quit()




