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

driver.get('http://alibaba.com')
driver.save_screenshot('screenshot.png')


items = driver.find_elements(By.CLASS_NAME, "card-info")
print(len(items))


driver.save_screenshot('screenshot.png')
driver.quit()


