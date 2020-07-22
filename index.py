import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

def initDriver():
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument('--headless')
    chrome_options.add_argument('start-maximized')

    # prefs = {
    # 	"profile.managed_default_content_settings.images": 2
    # }
    # chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
    return driver


driver=initDriver()
driver.get('http://nghiahsgs.com/vps/')
time.sleep(5)

ndung=driver.find_element_by_css_selector('body').text

print('---------')
print(ndung)
print('---------')