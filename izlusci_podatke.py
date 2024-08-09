import re
import os

mojdir = "HTML-ji"
mojest = 95


def izlusci(directory, stran):
    naslovi = []
    poglavja = []
    zanri = []
    ocena = []
    
    with open(os.path.join(directory, f"mangafire{stran}.html"), "r", encoding="utf-8") as dat:
        besedilo = dat.read()
        
        vzorec_naslovi = r'alt="(?P<naslov>.*?)>'
        for nas in re.findall(vzorec_naslovi, besedilo):
            if nas == 'MangaFire"':
                continue
            else:
                a = re.sub('&#039;', '"' , nas)
                naslovi.append(a[:-1])
                
        vzorec_poglavja = r'<ul class="content" data-name="chap"> <li> <a href="/read/.*?/.*?/chapter-(?P<poglavja>.*?)">'        
        for pog in  re.findall(vzorec_poglavja, besedilo):
            poglavja.append(float(pog))

        
        vzorec_zanri = r'<b class="text-primary">.*?</b>'
        b = re.findall(vzorec_zanri, besedilo)
        print(b)



        
    return ocena

izlusci("HTML-ji", 1)


