import requests
from bs4 import BeautifulSoup

# 멜론 차트 페이지 URL
url = 'https://www.melon.com/chart/index.htm'

# 요청 헤더에 User-Agent 추가
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 웹 페이지 요청
response = requests.get(url, headers=headers)
response.raise_for_status()  # 요청이 성공하지 않으면 예외를 발생시킵니다.

# BeautifulSoup 객체 생성
soup = BeautifulSoup(response.text, 'html.parser')

# 차트 항목 찾기 (lst50과 lst100 클래스를 한 번에 찾기)
chart_rows = soup.find_all('tr', class_=['lst50', 'lst100'])

# 결과를 저장할 리스트
chart_data = []

# 각 차트 항목에서 정보를 추출
for row in chart_rows:
    rank = row.find('span', class_='rank').text
    title = row.find('div', class_='ellipsis rank01').text.strip()
    artist = row.find('div', class_='ellipsis rank02').text.strip()
    album = row.find('div', class_='ellipsis rank03').text.strip()
    
    chart_data.append({
        '순위': rank,
        '제목': title,
        '가수': artist,
        '앨범': album
    })

# 결과 출력
for item in chart_data:
    print(f"순위: {item['순위']}")
    print(f"제목: {item['제목']}")
    print(f"가수: {item['가수']}")
    print(f"앨범: {item['앨범']}")
    print('---')
