from selenium import webdriver
from bs4 import BeautifulSoup
import os
import requests
from PIL import Image
import tld


#toonkor 크롤링 먼저 것은 이미지 저장 후 pdf로 변환 했다
def crawl_webtoon(episode_url):
    driver = webdriver.Chrome('D:/PycharmProjects/chromedriver')

    domain = tld.get_tld(episode_url)

    # 크롬드라이버를 통해 크롬을 킨다.
    # driver.implicitly_wait(3)
    # 데이터 불러오는 시간 3초로 정한다.
    ## url에 접근한다.a
    driver.get(episode_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    re = soup.find("div", id="toon_img")
    ep_title = ' '.join(soup.select('div.view-wrap h1')[0].text.split())

    for img_tag in re.select('img'):
        image_file_url = 'https://toonkor.'+domain + img_tag['src']
        image_dir_path = os.path.join(os.path.dirname(__file__), ep_title)
        image_file_path = os.path.join(image_dir_path, os.path.basename(image_file_url))
        # if not os.path.exists(image_dir_path):
        #     os.makedirs(image_dir_path)
        #예외 처리 파일 생성

        print(image_file_path, image_file_url)

        headers = {'Referer': episode_url}
        image_file_data = requests.get(image_file_url, headers=headers).content
                #byte 타입
        pil_image = Image.frombytes('RGB', (719, 3004 ), image_file_data)
        #bytes 형태일때 이미지 크기 값을 찾는 법을 알아보자.
        
        open_img_list = []

        open_img_list.append(pil_image)
        print('Completed !')

    open_img_list[0].save(ep_title + '.pdf', "PDF", resolution=100.0, save_all=True, append_images=open_img_list[1:])


if __name__ == '__main__':
    episode_url = 'https://toonkor.link/%EB%82%98_%ED%98%BC%EC%9E%90%EB%A7%8C_%EB%A0%88%EB%B2%A8%EC%97%85_50%ED%99%94.html'
    crawl_webtoon(episode_url)