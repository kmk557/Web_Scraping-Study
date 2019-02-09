from selenium import webdriver

driver = webdriver.Chrome('D:/PycharmProjects/chromedriver')
#크롬드라이버를 통해 크롬을 킨다.
driver.implicitly_wait(3)
#데이터 불러오는 시간 3초로 정한다.
## url에 접근한다.
driver.get('https://naver.com')