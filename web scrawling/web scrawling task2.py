from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 사용자 에이전트를 설정하여 모바일 사이트의 뷰를 시뮬레이션합니다.
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"

options = Options()
options.add_argument(f"user-agent={user_agent}")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# ChromeDriver 설치 및 설정
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Melon 모바일 차트 페이지로 접속
url = "https://m2.melon.com/index.htm"
driver.get(url)

# 페이지 로드 대기
time.sleep(5)  # 페이지가 로드될 때까지 충분한 시간 대기

# 현재 URL 확인
print("현재 URL:", driver.current_url)

# 차트 페이지로 이동하기 위한 클릭 (이벤트 페이지가 노출될 경우)
try:
    driver.find_element(By.CSS_SELECTOR, ".link-logo").click()
    time.sleep(2)
except Exception as e:
    print(f"Error occurred: {e}")

# 차트 페이지로 이동
top100_chart = driver.find_element(By.LINK_TEXT, "멜론차트")
top100_chart.click()
time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# Melon Top100 차트 목록 가져오기
top100 = soup.select("#_chartList .list_item")

for i in top100:
    # 순위
    rank = i.select_one(".ranking_num").text.strip()
    # 노래 제목
    title = i.select_one(".title.ellipsis").text.strip()
    #가수 이름
    artist = i.select_one(".name.ellipsis").text.strip()

    print("-" * 40)
    print(f"순위: {rank}")
    print(f"노래 제목: {title}")
    print(f"아티스트: {artist}")

print("-"*40)
driver.quit()