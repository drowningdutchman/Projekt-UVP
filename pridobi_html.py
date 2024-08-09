import requests
import os

def pridobi_html(url, directory, filename):
    #pridobimo html in nastavimo parametre
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    vsebina = requests.get(url).text
    
    #sedaj shranimo v datoteko
    with open(path, 'w', encoding='utf-8') as izhodna:
        izhodna.write(vsebina)
    return None

def pridobi_htmlje(st_strani):
    for i in range(1, st_strani):
        mojurl = f"https://mangafire.to/filter?keyword=&type%5B0%5D=manga&status%5B0%5D=completed&year%5B0%5D=2024&year%5B1%5D=2023&year%5B2%5D=2022&year%5B3%5D=2021&year%5B4%5D=2020&sort=recently_updated&page={i}"
        mojdir = 'HTML-ji'
        mojime = f"mangafire{i}.html"

        pridobi_html(mojurl, mojdir, mojime)
    return None

pridobi_htmlje(95)
