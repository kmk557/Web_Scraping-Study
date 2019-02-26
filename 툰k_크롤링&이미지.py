from selenium import webdriver
from bs4 import BeautifulSoup
import os
import requests
import tld

def crawl_webtoon(episode_url):
    driver = webdriver.Chrome('D:\PycharmProjects\Web_Scraping-Study\chromedriver')
    # 크롬드라이버를 통해 크롬을 킨다.
    # driver.implicitly_wait(3)
    # 데이터 불러오는 시간 3초로 정한다.
    ## url에 접근한다.
    driver.get(episode_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    domain = tld.get_tld(episode_url)
    #도메인 끝 부분

    re = soup.find("div", id="toon_img")
    ep_title = ' '.join(soup.select('div.view-wrap h1')[0].text.split())

#사이트 도메인이 바뀌었는지 확인하자.
    for img_tag in re.select('img'):
        image_file_url = 'https://toonkor.' + domain + img_tag['src']
        image_dir_path = os.path.join(os.path.dirname(__file__), ep_title)
        image_file_path = os.path.join(image_dir_path, os.path.basename(image_file_url))
        if not os.path.exists(image_dir_path):
            os.makedirs(image_dir_path)
        #예외 처리 파일 생성

        print(image_file_path, image_file_url)

        headers = {'Referer': episode_url}
        image_file_data = requests.get(image_file_url, headers=headers).content
                #byte 타입

        open(image_file_path, 'wb').write(image_file_data)
        #print(image_file_url, type(image_file_url))
        print('Completed !')
        
if __name__ == '__main__':
    episode_url = 'https://toonkor.link/%EB%82%98_%ED%98%BC%EC%9E%90%EB%A7%8C_%EB%A0%88%EB%B2%A8%EC%97%85_50%ED%99%94.html'
    crawl_webtoon(episode_url)