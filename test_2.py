# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import requests
import re
from bs4 import BeautifulSoup


def crawl_webtoon(episode_url):
    html = requests.get(episode_url).text
    soup = BeautifulSoup(html, 'html.parser')

    ep_title = ' '.join(soup.select('.view-wrap h1')[0].text.split())

    # toon_img
    for img_tag in soup.select('.view-wrap img'):
        image_file_url = img_tag['src']
        image_dir_path = os.path.join(os.path.dirname(__file__), ep_title)
        image_file_path = os.path.join(image_dir_path, os.path.basename(image_file_url))

        if not os.path.exists(image_dir_path):
            os.makedirs(image_dir_path)

        print(image_file_path)
        if re.match('.*jpg', image_file_url):
            headers = {'Referer': episode_url}
            image_file_data = requests.get(image_file_url, headers=headers).content
            open(image_file_path, 'wb').write(image_file_data)

    print('Completed !')


if __name__ == '__main__':
    episode_url = 'https://toonkor.pw/4컷용사_특별_원작_2화.html'
    crawl_webtoon(episode_url)
