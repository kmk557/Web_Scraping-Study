from PIL import Image
import requests

Img = Image.open('D:\PycharmProjects\Web_Scraping-Study\톡탁.png')
headers = {'Referer': 'https://www.askcompany.kr/vod/crawling/'}
image_file_data = requests.get('https://askcompanyjpe.blob.core.windows.net/media/askdjango/course/2017/02/28/47/47747b3562fb4a57b9b8b413f291096e.jpg',
                               headers=headers).content
open('D:/PycharmProjects/Web_Scraping-Study/a.jpg', 'wb').write(image_file_data)