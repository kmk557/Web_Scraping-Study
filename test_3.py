import os
import re
from PIL import Image

webtoon_route = "D:\PycharmProjects\Web_Scraping-Study\화산전생 1화"
list = webtoon_route.split('\\')

img_list = [i for i in os.listdir(webtoon_route) if i.endswith(".jpg")]
open_img_list = []
pdf_name = list[-1]+".pdf"

print(img_list)

for img in img_list:
    path = webtoon_route + "\\" + img
    im = Image.open(path)
    open_img_list.append(im)

# open_img_list[0].save(pdf_name, "PDF", resolution = 100.0, save_all = True, append_images = open_img_list)
