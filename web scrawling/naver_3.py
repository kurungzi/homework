import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?sm=tab_hty.top&ssc=tab.blog.all&query=%EA%B9%80%EC%98%88%EC%A7%80&oquery=%EC%95%88%EC%84%B8%EC%98%81&tqi=ir73Tlqo1LwsslmFL%2FGssssssyC-350609"
keyword = input("검색어를 하나만 입력해주세요")

url = base_url + keyword

req = requests.get(url, header_user) 
html = req.text


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