from selenium import webdriver
import time
from bs4 import BeautifulSoup
from idpw import naver_id, naver_pw

executable_path = 'C:/chromedriver_win32/chromedriver.exe'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path = executable_path, options = options)

url = 'https://class.likelion.org/accounts/login/'
driver.get(url)
time.sleep(3)

driver.find_element_by_xpath('//*[@id="id_username"]').send_keys(naver_id)
driver.find_element_by_xpath('//*[@id="id_password"]').send_keys(naver_pw)

driver.find_element_by_xpath('//*[@id="form-login"]/button').click()
