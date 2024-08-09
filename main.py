#main datoteka, ki pozene projektno nalogo
from pridobi_html import pridobi_html
from izlusci_podatke import izlusci

mojurl = f"https://mangafire.to/filter?keyword=&type%5B0%5D=manga&type%5B1%5D=one_shot&type%5B2%5D=doujinshi&type%5B3%5D=novel&type%5B4%5D=manhwa&type%5B5%5D=manhua&year%5B0%5D=2024&year%5B1%5D=2023&year%5B2%5D=2022&year%5B3%5D=2021&year%5B4%5D=2020&year%5B5%5D=2019&year%5B6%5D=2018&year%5B7%5D=2017&year%5B8%5D=2016&year%5B9%5D=2015&sort=recently_updated&page="
mojdir = 'HTML-ji'
vsi_podatki = []

for i in range(1,806):
    url = mojurl + f"{i}"
    ime = "mangafire" + f"{i}" + ".html"
    #pridobi_html(url, mojdir, ime)
    vsi_podatki += izlusci(mojdir, i)
print(vsi_podatki)
    
