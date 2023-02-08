import requests
from bs4 import BeautifulSoup
import os

print(__file__)

url = "https://photo.xuite.net/pinoza.tw/19950535-%E6%9E%97%E5%BF%97%E7%8E%B2+-+%E9%83%BD%E5%B8%82%E5%84%B7%E4%BA%BA"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
images = soup.select("div.list_area a img")

path = os.path.dirname(__file__)

for i, image in enumerate(images):
    r = requests.get(image.get('src'))
    with open(path+"/{}.jpg".format(i),"wb") as f:
        f.write(r.content)