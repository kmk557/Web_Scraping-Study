from selenium import webdriver
from bs4 import BeautifulSoup
import os


def crawl_webtoon(episode_url):
    driver = webdriver.Chrome('D:/PycharmProjects/chromedriver')
    # 크롬드라이버를 통해 크롬을 킨다.
    # driver.implicitly_wait(3)
    # 데이터 불러오는 시간 3초로 정한다.
    ## url에 접근한다.
    driver.get(episode_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    re = soup.find("div", id="toon_img")
    ep_title = ' '.join(soup.select('div.view-wrap h1')[0].text.split())

    for img_tag in re.select('img'):
        image_file_url = 'https://toonkor.pw' + img_tag['src']
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
    episode_url = 'https://toonkor.land/4%EC%BB%B7%EC%9A%A9%EC%82%AC_%ED%8A%B9%EB%B3%84_%EC%9B%90%EC%9E%91_2%ED%99%94.html'
    crawl_naver_webtoon(episode_url)