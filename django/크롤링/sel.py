from selenium import webdriver
import time
from bs4 import BeautifulSoup

executable_path = 'C:/chromedriver_win32/chromedriver.exe'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path = executable_path, options = options)

url = 'https://media.daum.net/'
driver.get(url)
time.sleep(3)
text = driver.page_source

soup = BeautifulSoup(text, 'html.parser')

for i in soup.select('#mArticle > div.box_headline > ul > li'):
    title = i.a.text.strip()
    url = i.a['href']
    print(title, url)