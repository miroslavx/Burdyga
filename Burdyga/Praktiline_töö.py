from datetime import *

tana=date.today()g
tana=date.today().strftime("%B %d, %Y")

print(f"Täna on {tanaf}")
d=tana.day
m=tana.month
y=tana.year
print(d)
print(m)
print(y)

#Ülesanne 1

print("Tere tulemast!")
nimi=input("Mis on sinu nimi? ").capitalize() #lower()-aaa, upper()-AAA, capitalize
()-Aaa
print("Tere tulemast! Tervitan sind ", nimi)
print("Tere tulemast! Tervitan sind "+ nimi)
try:
   vanus=int(input("Kui vana sa oled? "))
   print("Tere tulemast! Tervitan sind "+nimi+" Sa oled ", vanus, "aastat vana")
   print(f"\tTere tulemast! \nTervitan sind {nimi) Sa oled {vanus} aastat vana")
except:
    print("On vaja numbreid sisestdal")
