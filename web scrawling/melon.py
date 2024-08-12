# 멜론 사이트에서 1위부터 100까지의 정보 가져오기.
# 멜론차트 100 스크래핑

# [순위]
# 제목 : 정보
# 가수 : 정보
# 앨범 : 정보

import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?sm=tab_hty.top&ssc=tab.blog.all&query=%EC%9C%A0%EC%82%B0%EA%B7%A0&oquery=%EA%B9%80%EC%98%88%EC%A7%80&tqi=ir7HtwqVN8Vss7WGC3NssssstOK-100135"
keyword = input("검색어를 하나만 입력해주세요")

url = base_url + keyword

req = requests.get(url, header_user) 
html = req.text


soup = BeautifulSoup(html, "html.parser")
# print(soup)