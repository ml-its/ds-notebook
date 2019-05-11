import requests
from bs4 import BeautifulSoup
import pandas as pd 
link = 'https://www.olx.co.id/all-results/q-{}/?page=1}'


def cari_atribut(barang):
    link_ = cari_barang(barang)


def cari_barang(barang):
    global link
    link = link.format(barang)
    return link
    


    df = pd.DataFrame(hasil)

def cari_last_page(link):
    req = requests.get(link.format(1))
    soup = BeautifulSoup(req.text,'lxml')
    kumpulan_page = soup.find_all('span',class_='item inline-block')
    page_terakhir = kumpulan_page[-1].a['href'].split('=')
    page_terakhir = int(page_terakhir[-1])

    return page_terakhir



def cari_judul(): 
    pass
def cari_tanggal(): 
    pass
def cari_harga(): 
    pass
def cari_lokasi(): 
    pass

kaos_kaki = cari_last_page(link.format('kaos-kaki'))

if __name__ == "__main__":
    cari_atribut('htc')