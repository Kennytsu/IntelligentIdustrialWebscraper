# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.proxy import Proxy, ProxyType
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service

# proxy_address = 'http://89.145.162.81'
# proxy = Proxy({
#     'proxyType': ProxyType.MANUAL,
#     'httpProxy': proxy_address,
#     'ftpProxy': proxy_address,
#     'sslProxy': proxy_address,
#     'noProxy': ''
# })

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument('--disable-dev-shm-usage')
# #chrome_options.add_argument('--incognito')

# chrome_options.proxy = proxy

# chromedriver_path = '/usr/bin/chromium-browser'
# service = Service(chromedriver_path)

# driver = webdriver.ChromiumEdge(service=chromedriver_path, options=chrome_options)

# url = 'https://german.alibaba.com/trade/search?spm=a2700.product_home_newuser.home_new_user_first_screen_fy23_pc_search_bar.associationItem_pos_0&tab=all&SearchText=elektro+scooter'

# driver.get(url)

# try:
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "ip-address"))
#     )
#     ip_element = driver.find_element(By.ID, "ip-address")
#     print(ip_element.text)
# except Exception as e:
#     print(e)
        



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode
chrome_options.add_argument('--disable-gpu')  # Disables GPU acceleration
chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
chrome_options.add_argument('--remote-debugging-port=9222')  # Set remote debugging port


# Correct way to create the Service object with the path to the ChromeDriver
chromedriver_path = '/usr/bin/chromium-browser'  # Use the correct path to your Chromium binary
service = Service(ChromeDriverManager().install())

# Initialize the WebDriver with the Service object and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Test navigation
driver.get('https://www.google.com')
# print(driver.title)

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ip-address"))
    )
    ip_element = driver.find_element(By.ID, "ip-address")
    print(ip_element.text)
except Exception as e:
    print(e)

# Cleanup
driver.quit()





