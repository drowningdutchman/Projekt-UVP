import requests
import os

mojurl = f"https://mangafire.to/filter?keyword=&type%5B0%5D=manga&type%5B1%5D=one_shot&type%5B2%5D=doujinshi&type%5B3%5D=novel&type%5B4%5D=manhwa&type%5B5%5D=manhua&year%5B0%5D=2024&year%5B1%5D=2023&year%5B2%5D=2022&year%5B3%5D=2021&year%5B4%5D=2020&year%5B5%5D=2019&year%5B6%5D=2018&year%5B7%5D=2017&year%5B8%5D=2016&year%5B9%5D=2015&sort=recently_updated&page="
mojdir = 'HTML-ji'

def pridobi_html(url, directory, filename):
    #pridobimo html in nastavimo parametre
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    vsebina = requests.get(url).text
    
    #sedaj shranimo v datoteko
    with open(path, 'w', encoding='utf-8') as izhodna:
        izhodna.write(vsebina)
    return None

for i in range(1,806):
    url = mojurl + f"{i}"
    ime = "mangafire" + f"{i}" + ".html"
    pridobi_html(url, mojdir, ime)
    
