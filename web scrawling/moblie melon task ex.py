from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"
options = Options()
options.add_argument(f"user-agent={user_agent}")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
url = "https://m2.melon.com/index.htm"
driver.get(url)

try:
    # 이벤트 화면이나 팝업이 있을 경우 닫기
    try:
        # 이벤트 화면을 닫는 버튼을 찾고 클릭 (버튼의 ID나 클래스는 실제 페이지 구조에 따라 달라질 수 있음)
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_close"))  # 실제 닫기 버튼의 선택자를 넣으세요
        )
        close_button.click()
        time.sleep(1)  # 버튼 클릭 후 잠시 대기
    except:
        # 이벤트 화면이나 팝업이 없으면 예외 처리
        print("이벤트 화면이나 팝업이 없습니다.")

    # TOP 100 차트 페이지로 이동
    chart_url = "https://m2.melon.com/chart/index.htm"  # 차트 100 페이지 URL (확인 필요)
    driver.get(chart_url)

    # 웹 페이지 로딩 대기
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "wrap_song_info")))

    # 페이지 소스 가져오기
    soup = BeautifulSoup(driver.page_source, "html.parser")
    rank_list = soup.find_all("div", {"class": "wrap_song_info"})

    for rank in rank_list:
        rank_num = rank.find("span", {"class": "rank"}).text
        song_title = rank.find("div", {"class": "ellipsis rank01"}).find("a").text
        artist_name = rank.find("div", {"class": "ellipsis rank02"}).find("a").text
        print(f"순위: {rank_num}")
        print(f"노래 제목: {song_title}")
        print(f"가수 이름: {artist_name}")
        print()
finally:
    driver.quit()
