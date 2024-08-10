import csv

def write_csv(seznam):
    with open('podatki.csv','w', encoding='utf-8') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['ime','vrsta','poglavja','datum'])
        for row in seznam:
            csv_out.writerow(row)
    return None
