from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import parse

import time

keyword = input()

url = "https://www.instagram.com/explore/tags/{}/".format(keyword)

# 인코딩 이슈 발생시
# parsed = parse.quote_plus(keyword)
# url = f'http://www.instagram.com/explore/tags/{parsed}/'

options = webdriver.ChromeOptions()

options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')

driver = webdriver.Chrome('chromedriver', options=options)


driver.get(url)
time.sleep(3)

posts = []
images = driver.find_elements_by_css_selector('.Nnq7C img')

for img in images:
    if len(posts) > 15:
        break
    post = img.get_attribute('src')
    posts.append(post)
    
print(len(posts))
posts = posts[10:len(posts)]
# for n in range(10, len(posts)):
#     posts[n-10] = posts[n]

print(posts)

driver.close()