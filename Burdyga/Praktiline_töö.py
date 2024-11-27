from datetime import *
import math

#Ülesanne 1
tana=date.today()
tana=date.today().strftime("%B %d, %Y")

print(f"Täna on {tanaf}")
d=tana.day
m=tana.month
y=tana.year
print(d)
print(m)
print(y)

#Ülesanne 1.1

print("Tere tulemast!")
nimi=input("Mis on sinu nimi? ").capitalize() #lower()-aaa, upper()-AAA, capitalize
()-Aaa
print("Tere tulemast! Tervitan sind ", nimi)
print("Tere tulemast! Tervitan sind "+ nimi)
try:
   vanus=int(input("Kui vana sa oled? "))
   print("Tere tulemast! Tervitan sind "+nimi+" Sa oled ", vanus, "aastat vana")
   print(f"\tTere tulemast! \nTervitan sind {nimi} Sa oled {vanus} aastat vana")
except:
    print("On vaja numbreid sisestdal")

#Ülesanne 2

avaldis1 = 3 + 8 / (4 - 2) * 4
avaldis2 = (3 + 8) / 4 - 2 * 4
avaldis3 = 3 + (8 / 4) - (2 * 4)

print("Algne avaldis 3 + 8 / (4 - 2) * 4 =", avaldis1)
print("(3 + 8) / 4 - 2 * 4 =", avaldis2)
print("3 + (8 / 4) - (2 * 4) =", avaldis3)

#Ülesanne 3

R = float(input("Sisesta ringi raadius R: "))

ruut_pindala = (2 * R) ** 2
ruut_umbermoot = 4 * (2 * R)
ring_pindala = math.pi * R ** 2
ring_umbermoot = 2 * math.pi * R

print("Ruudu pindala:", ruut_pindala)
print("Ruudu ümbermõõt:", ruut_umbermoot)
print("Ringi pindala:", ring_pindala)
print("Ringi ümbermõõt:", ring_umbermoot)

#Ülesanne 4
maa_raadius = 6378000  # metr
munt_diameeter = 0.02575  # 2-eurose 
pi = 3.14159

maa_umbermoot = 2 * pi * maa_raadius
muntide_arv = maa_umbermoot / munt_diameeter
print("Müntide arv ümber Maa:", round(muntide_arv))

#Ülesanne 5
koll = "KILL-KOLL"
killadi_koll = "KILLADI-KOLL"
print(f"{koll} {koll} {killadi_koll} {koll} {koll} {killadi_koll} {koll} {koll} KILLKOLL")
print(koll)

#Ülesanne 6
laulusonad = """
Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.
"""

print(laulusonad.upper())

#Üleasnne 7
pikkus = float(input("Sisesta ristküliku pikkus: "))
laius = float(input("Sisesta ristküliku laius: "))

pindala = pikkus * laius
umbermoot = 2 * (pikkus + laius)

print("Ristküliku pindala:", pindala)
print("Ristküliku ümbermõõt:", umbermoot)


#Ülesanne 8

kütus = float(input("Sisesta tangitud kütuse liitrid:"))
km = float(input("Sisesta läbitud kilomeetrid :"))

kulu = (kütus / km) * 100
print("Kütusekulu 100 km kohta:", round(kulu, 2), "l/100km")

#Ülesanne 9
kiirus = 29.9  #Km/chas
minutid = float(input("Sisesta aeg minutites: "))

teepikkus = (kiirus / 60) * minutid
print(f"Rulluisutaja jõuab {round(teepikkus, 2)} km kaugusele.")



#Üleasnne 10
minutid = int(input("Sisesta aeg minutites: "))

tunnid = minutid // 60
ulejaanud_minutid = minutid % 60

print(f"{tunnid}:{ulejaanud_minutid}")
