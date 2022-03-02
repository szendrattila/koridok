"""
csapat;versenyzo;eletkor;palya;korido;kor
Versenylovak;Fürge Ferenc;29;Gran Prix Circuit;00:01:11;1
Versenylovak;Fürge Ferenc;29;Gran Prix Circuit;00:01:05;2
"""

class Korido:
    def __init__(self, sor):
        csapat, versenyzo, eletkor, palya, korido, kor = sor.strip().split(";")
        self.csapat = csapat
        self.versenyzo = versenyzo
        self.eletkor = eletkor
        self.palya = palya
        self.korido = korido
        self.kor = int(kor)
        self.ora = int(korido[:2])
        self.perc = int(korido[3:5])
        self.masodperc = int(korido[6:8])
        
lista =[]

with open("autoverseny.txt", encoding="utf-8") as f:
    f.readline()
    for sor in f:
        lista.append(Korido(sor))
#3.feladat
print(f"3. feladat: {len(lista)}")
#4.feladat
"""
for sor in lista:
    if sor.versenyzo == "Fürge Ferenc" and sor.palya == "Gran Prix Circuit" and sor.kor == 3:
        print(f"4. feladat: {sor.ora * 3600 + sor.perc * 60 + sor.masodperc } másodperc")
"""
masodperc = [sor.ora * 3600 + sor.perc * 60 + sor.masodperc for sor in lista if sor.versenyzo == "Fürge Ferenc" and sor.palya == "Gran Prix Circuit" and sor.kor == 3]

print(f"4. feladat: {masodperc[0]} másodperc")
#5.feladat
bekernev = input("Kérem egy versenyző nevét: \n")
#6.feladat
for sor in lista:
    if sor.versenyzo == bekernev:
        legkisebb = min(lista, key=lambda x:x.korido).korido
        legpalya = min(lista, key=lambda x:x.korido).palya
print(f"6. feladat: {legpalya},{legkisebb}")
        