import requests
from bs4 import BeautifulSoup

url = 'https://tekno.kompas.com/read/2019/04/25/19030047/xiaomi-dan-lg-siapkan-ponsel-dengan-tiga-kamera-selfie-'
s = requests.Session()
req = s.get(url)
soup = BeautifulSoup(req.text,'lxml')

yt = soup.find_all('iframe')
for link in yt: 
    if 'youtube' in link['src']:
        link_yt = 'https://www.youtube.com/watch?v='+link['src'].split('/')[-1]

print(link_yt)