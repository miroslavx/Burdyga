from MinuOmaMoodul import *
kus_vas={}

k�simused, vastused=loe_ankeet("Ankeet.txt")
print(k�simused)
print(vastused)
for i in range(len(k�simused)):
    print(f"{i+1}. K�simus on: "+k�simused[i]+", vastus on: "+vastused[i])



#print(kus_vas)
failide_kustutamine()

�mber_kirjuta_fail(input("Faili nimi: "))

kirjuta_failisse("P�evad.txt")

p�evad=loe_failist("P�evad.txt")
#1
print(p�evad)
#2
for p�ev in p�evad:
    print(p�ev)
