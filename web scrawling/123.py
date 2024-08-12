from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

# 사용자 에이전트를 설정합니다.
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"
options = Options()
options.add_argument(f"user-agent={user_agent}")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Chrome 드라이버를 설정합니다.
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 멜론 모바일 메인 페이지에 접속합니다.
url = "https://m2.melon.com/index.htm"
driver.get(url)

# 페이지가 완전히 로드될 때까지 잠시 대기합니다.
time.sleep(5)

# 상단 메뉴에서 "차트"를 선택하여 차트 페이지로 이동합니다.
try:
    # 차트 메뉴로 이동하기 위한 코드 (변경될 수 있음)
    chart_menu = driver.find_element(By.XPATH, '//a[@href="/chart/index.htm"]')
    chart_menu.click()
    time.sleep(5)
    
    # 차트 페이지에서 Top100을 선택합니다.
    top100_menu = driver.find_element(By.XPATH, '//a[@href="/chart/index.htm?classCd=DM0000"]')
    top100_menu.click()
    time.sleep(5)

    # 페이지 소스를 가져옵니다.
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    # Top100 정보를 추출합니다.
    songs = soup.select('table > tbody > tr')
    
    for song in songs:
        rank = song.select_one('span.rank').text
        title = song.select_one('div.ellipsis.rank01 > span > a').text
        artist = song.select_one('div.ellipsis.rank02 > a').text
        
        print(f"순위: {rank}")
        print(f"노래 제목: {title}")
        print(f"가수 이름: {artist}")
        print()

finally:
    # 드라이버를 종료합니다.
    driver.quit()
