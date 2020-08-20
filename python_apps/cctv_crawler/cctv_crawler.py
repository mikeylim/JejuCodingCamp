from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import parse

import time

id = input()
url = f"http://www.jejuits.go.kr/mobile/SCctvPop.do?id={id}"

options = webdriver.ChromeOptions()

options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')

driver = webdriver.Chrome('chromedriver', options=options)


driver.get(url)
time.sleep(3)

video = driver.find_element_by_css_selector('video source')

source = video.get_attribute('src')

print(source)
driver.close()