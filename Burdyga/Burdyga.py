

from random import *  # Kõik funktsioonid, randint as rd funktsioonide ümbernimetus
from math import *  # Pi kasutamiseks

# Ülesanne 1
print("Tere Tulemast")
nimi = input("Mis on sinu nimi? ")
print("Tere Tulemast! Tervitan sind", nimi)
print("Tere Tulemast! Tervitan sind " + nimi)  
vanus = int(input("Kui vana sa oled? "))
print("Tere Tulemast! Tervitan sind " + nimi + ", sa oled " + str(vanus) + " aastat vana")  
print(f"Tere Tulemast! Tervitan sind {nimi}, sa oled {vanus} aastat vana")

# Ülesanne 2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_kaib_koolis = True  

print(f"Vanuse tüüp: {type(vanus)}")
print(f"Eesnime tüüp: {type(eesnimi)}")
print(f"Pikkuse tüüp: {type(pikkus)}")
print(f"Kas käib koolis tüüp: {type(kas_kaib_koolis)}")

kas_kaib_koolis = False
print(f"Kas käib koolis väärtus: {kas_kaib_koolis}")

# Ülesanne 3
kokku = randint(1, 1000)  
print(f"Kokku on {kokku} kommi")
kommi = int(input("Mitu kommi sa tahad? "))
kokku -= kommi
print(f"Kokku on {kokku} kommi alles")

# Ülesanne 4
print("Läbimõõdu leidmine")  
l = float(input("Ümbermõõt: "))
d = l / pi
print(f"Läbimõõdu suurus on {d:.2f}")



#ülesanne 5
N = float(input("Sisesta ristküliku laius: "))
M = float(input("Sisesta ristküliku pikkus: "))
diagonaal = math.sqrt(N**2 + M**2)
print(f"Ristküliku diagonaal on {diagonaal:.2f}")

#ülesanne 6
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg
print(f"Sinu kiirus oli {kiirus:.2f} km/h")

#ülesanne 7
arvud = []
for i in range(5):
    arv = int(input(f"Sisesta {i+1}. täisarv: "))
    arvud.append(arv)
keskmine = sum(arvud) / len(arvud)
print(f"Aritmeetiline keskmine on {keskmine:.2f}")

#ülesanne 8
print("   @..@")
print("  (----)")
print(" ( \\__/ )")
print("^^ \"\" ^^")

#ülesanne 9
a = 3
b = 4
c = 5
P = a + b + c
print(f"Kolmnurga ümbermõõt on {P}")

#ülesanne 10
P = int(input("Mitu sõpra on? "))
pitsa_hind = 12.90
jootraha = pitsa_hind * 0.1
kokku = pitsa_hind + jootraha
igaüks_maksab = kokku / P
print(f"Igaüks peab maksma {igaüks_maksab:.2f} €")


