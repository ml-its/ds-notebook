import requests 
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://indeks.kompas.com/all/2019-05-26/{}' # 1-15
hasil = []
for i in range(1,16):
    print(i)
    kumpul = {}
    link_kompas = url.format(i)
    req = requests.get(link_kompas)
    soup = BeautifulSoup(req.text, 'lxml')
    title = soup.find_all('h3', class_='article__title article__title--medium')
    link = soup.find_all('a', class_='article__link')
    for tit, lin in zip(title, link): 
        kumpul['judul']=tit.text
        kumpul['link'] = lin['href']
        req_par = requests.get(lin['href'])
        soup_par = BeautifulSoup(req_par.text, 'lxml')
        try:
            par = soup_par.find('div', 'read__content')
            kumpul['paragraf']=par.text.strip()
        except AttributeError:
            print('\n\n\n\n\n\n')
            print('hehe ga ada attribute read__contentnya bray')
            print('\n\n\n\n\n\n')
        print(tit.text)
        print('-'*10)
        hasil.append(kumpul)

df = pd.DataFrame(hasil)
df.to_csv('kompas.csv')
print(hasil)