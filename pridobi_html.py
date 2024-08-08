import requests


mojurl = 'https://mangafire.to/type/manga'
mojime = 'mangafire.html'


def pridobi_html(url, filename):
    #pridobimo html
    vsebina = requests.get(url).text

    #sedaj shranimo v datoteko
    with open(filename, 'w', encoding='utf-8') as izhodna:
        izhodna.write(vsebina)
    return None

pridobi_html(mojurl, mojime)
