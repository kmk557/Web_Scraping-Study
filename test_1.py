# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import requests
from bs4 import BeautifulSoup


def crawl_naver_webtoon(episode_url):
    html = requests.get(episode_url).text
    soup = BeautifulSoup(html, 'html.parser')
        #html 파일 불러오기

    comic_title = ' '.join(soup.select('.comicinfo h2')[0].text.split())
    ep_title = ' '.join(soup.select('.tit_area h3')[0].text.split())
        #만화 제목 밑 만화 속 개별 제목 불러오기

    for img_tag in soup.select('#comic_view_area img'):
        image_file_url = img_tag['src']
        image_dir_path = os.path.join(os.path.dirname(__file__), comic_title, ep_title)
        image_file_path = os.path.join(image_dir_path, os.path.basename(image_file_url))
    #이미지 주소와 컴퓨터에 저장할 위치 선정
        if not os.path.exists(image_dir_path):
            os.makedirs(image_dir_path)
    #예외 처리 파일 생성

        print(image_file_path)

        headers = {'Referer': episode_url}
        image_file_data = requests.get(image_file_url, headers=headers).content
        #byte 타입

        open(image_file_path, 'wb').write(image_file_data)
        #이미지 저장

    #print(image_file_url, type(image_file_url))
    print('Completed !')

if __name__ == '__main__':
    episode_url = 'http://comic.naver.com/webtoon/detail.nhn?titleId=20853&no=1048&weekday=tue'
    crawl_naver_webtoon(episode_url)