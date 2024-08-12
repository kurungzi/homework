import requests
from bs4 import BeautifulSoup

keyword = input ("검색할 상품 :")
base_url = f"https://www.coupang.com/np/search?component=&q= {keyword}"

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
cookie = {"sorry" : "sorry"}

req = requests.get(base_url, headers = header_user, cookies = cookie, timeout = 3)


html = req.text
soup = BeautifulSoup(html, "html.parser")
print(soup)

items = soup.select("[class=search-product  ]")

for rank, item in enumerate(items, 1):
    name = item.select_one(".name").text
    price = item.select_one(".price-value")
    link = item.a["href"]
    img_src = item.select_one(".search-product-wrap-img")
    rocket = item.select_one (".badge.rocket")

    print(f"[{rank}]위")
    print(f"제품명 : {name}")
    print(f"{price.text}원")
    #print(f"이미지 URL : {img_src}")

    if rocket:
        print("로켓 배송 가능")
    else :
        print("로켓 배송 불가능")
    print(f"쿠팡 링크 : https://www.coupang.com{link}")
    if img_src.get("data-img-src"):
        img_url = f"http:{img_src.get('data-img-src')}"
    else :
        img_url = f"http:{img_src.get('src')}"

    print(f"이미지 URL : {img_url}")
    print()

    img_req = requests.get(img_url)
    with open (f"img/{rank}.jpg", "wb") as f :
        f.write(img_req.content)