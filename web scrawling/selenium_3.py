from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어를 하나만 입력해주세요")

url = base_url + keyword

#req = requests.get(url, header_user) 
#html = req.text

driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

for i in range(6) :
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
# print(soup)

title = soup.select (".title_link")
name = soup.select(".name")
print(len(title), len(name))

for i in zip(title, name):
    print(f"제목 : {i[0].text}")
    print(f"작성자 : {i[1].text}")
    print(f"링크 : {i[0]['href']}")
    print()
