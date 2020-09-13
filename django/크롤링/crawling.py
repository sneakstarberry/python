import requests
from bs4 import BeautifulSoup

# response = requests.get('https://www.acmicpc.net/problem/tags').text

# soup = BeautifulSoup(response, 'html.parser')

# tags = soup.select('.table-responsive tbody tr a[href*=problem]')

response = requests.get('https://www.daum.net').text

soup = BeautifulSoup(response, 'html.parser')

tags = soup.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin.hide > div.realtime_part > ol > li')
#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin.hide > div.realtime_part > ol > li:nth-child(1) > div > div:nth-child(1) > span.txt_issue
for x in tags:
    print(x.text)