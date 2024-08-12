import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_melon_chart():
    url = "https://www.melon.com/chart/index.htm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    songs = []
    
    for tr in soup.select('table > tbody > tr'):
        rank = tr.select_one('.rank').text.strip()
        title = tr.select_one('.ellipsis.rank01 > span > a').text.strip()
        artist = tr.select_one('.ellipsis.rank02 > a').text.strip()
        album = tr.select_one('.ellipsis.rank03 > a').text.strip()
        
        songs.append({
            '순위': rank,
            '제목': title,
            '가수': artist,
            '앨범': album
        })
    
    return songs

# 멜론 차트 스크래핑 실행
chart_data = scrape_melon_chart()

# DataFrame으로 변환
df = pd.DataFrame(chart_data)

# 결과 출력
print(df)

# CSV 파일로 저장 (선택사항)
# df.to_csv('melon_chart.csv', index=False, encoding='utf-8-sig')