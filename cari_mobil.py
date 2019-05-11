import requests
from bs4 import BeautifulSoup
import pandas as pd 


link = 'https://www.olx.co.id/all-results/q-mobil/?page={}'

req = requests.get(link.format(1))
soup = BeautifulSoup(req.text,'lxml')
kumpulan_page = soup.find_all('span',class_='item inline-block')
page_terakhir = kumpulan_page[-1].a['href'].split('=')
page_terakhir = page_terakhir[-1]

kumpulan_link=[]
hasil = []
for i in range(1,int(page_terakhir)+1):
    kumpulan_link.append(link.format(i))

print(kumpulan_link)



for link in kumpulan_link[:2]:
    

    req_mobil = requests.get(link)
    soup_mobil = BeautifulSoup(req_mobil.text, 'lxml')
    seluruh_judul_page = soup_mobil.find_all('a', {'class':'marginright5 link linkWithHash detailsLink'})
    seluruh_harga_page = soup_mobil.find_all('strong', class_='c000')
    seluruh_kota_page = soup_mobil.find_all('p', class_='color-9 lheight14 margintop3')
    seluruh_tanggal_page = soup_mobil.find_all('td',class_='rel tcenter')


    for judul, harga, kota, tanggal in zip(seluruh_judul_page, seluruh_harga_page, seluruh_kota_page,seluruh_tanggal_page): 
        item = {}
        # print(judul.text.strip())
        # print(harga.text.strip())
        # print(tanggal.text.strip())
        # print(kota.find('span').text.strip())
        item['judul']=judul.text.strip()
        item['harga'] = harga.text.strip()
        item['tanggal'] = tanggal.text.strip()
        item['kota'] = kota.find('span').text.strip()
        item['link']=judul['href']
        hasil.append(item)



from pprint import pprint
pprint(hasil)
df = pd.DataFrame(hasil)
df.to_csv('olx-hal12.csv')