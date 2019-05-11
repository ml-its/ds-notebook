import requests, os
from bs4 import BeautifulSoup
import pandas as pd 

seluruh_halaman = []
directory=os.getcwd()
url = 'https://indeks.kompas.com/tekno/2019-04-{}'


def cari_paragraf(soup): 
    return soup.find('div',class_='read__content').text.strip()  


total_url = []
for i in range(1,30): 
    total_url.append(url.format(i))

for url in total_url:
    req_url = requests.get(url)
    soup_url = BeautifulSoup(req_url.text,'lxml')
    a = soup_url.find_all('a', class_='article__link')
    for judul in a: 
        print(f'mengambil {judul.text} sekarang')
        link = judul['href']
        req = requests.get(link)
        soup = BeautifulSoup(req.text,'lxml')

        paragraf = cari_paragraf(soup)
        
        judul = soup.find('h1').text
        gambar= soup.find('div', class_='photo')
        gambar = gambar.img['src']
        nama_gambar = gambar.split('/')[-1]
        req_gambar = requests.get(gambar)
        with open(directory+'//gambar//'+nama_gambar, 'wb') as f: 
            print(f'berhasil mengambil gambar {nama_gambar}')
            f.write(req_gambar.content)
        print(paragraf)

