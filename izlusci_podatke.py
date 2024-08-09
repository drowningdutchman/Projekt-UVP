import re
import os

#mojdir = "HTML-ji"
#mojest = 805


def izlusci(directory, stran):
    naslovi = []
    poglavja = []
    vrste = []
    datumi = []
    
    with open(os.path.join(directory, f"mangafire{stran}.html"), "r", encoding="utf-8") as datoteka:
        besedilo = datoteka.read()
        
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

        
        vzorec_vrsta = r'<span class="type">(?P<vrste>.*?)</span>'
        vrste = re.findall(vzorec_vrsta, besedilo)

        vzorec_datumi = r'<ul class="content" data-name="chap"> <li> <a href="/read/.*?/.*?/chapter-.*?"> <span>Chap .*? <b>.*?</b></span> <span>(?P<datum>.*?)</span>'
        dat = re.findall(vzorec_datumi, besedilo)
        for datum in dat:
            if "ago" in datum:
                datumi.append("Aug 10, 2024")
            else:
                datumi.append(datum)

        izpisi = zip(naslovi, vrste, poglavja, datumi)
    return list(izpisi)


