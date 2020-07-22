from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def initDriver():
    CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                            chrome_options=chrome_options
                            )
    return driver

driver=initDriver()
#driver.get("http://nghiahsgs.com/vps")
#text=driver.find_element_by_css_selector('body').text
#print(text)

driver.get('http://nghiahsgs.com')

driver.get_screenshot_as_file('test2.png')
driver.close()


