import requests
from bs4 import BeautifulSoup as bs 

url = 'https://indeks.kompas.com/tekno/2019-04-25'
req = requests.get(url)
soup = bs(req.text, 'lxml')

links = soup.find_all('a', class_='article__link')

artikel = []
for link in links: 
    artikel.append(link['href'])

for link in artikel: 
    req_artikel = requests.get(link)
    soup_artikel = bs(req_artikel.text,'lxml')
    photo = soup_artikel.find('div', class_='photo')
    judul = soup_artikel.find('h1', class_='read__title')
    tempat_paragraf = soup_artikel.find('div', class_='read__content')
    paragraf = tempat_paragraf.find_all('p')
    paragraf = ' '.join(x.text for x in paragraf)
    yt = soup_artikel.find_all('iframe')
    for link in yt: 
        if 'youtube' in link['src']: 
            link_yt = 'https://www.youtube.com/watch?v='+link['src'].split('/')[-1]


    print(judul.text, '\n\n'+photo.find('img')['src'],'\n'+paragraf,'\n',link_yt)
    print('-'*10)
ya