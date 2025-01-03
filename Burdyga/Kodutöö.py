# Prog0.1
katet1 = float(input("Sisesta esimese kaateti pikkus: "))
katet2 = float(input("Sisesta teise kaateti pikkus: "))

hüpotenuus = (katet1**2 + katet2**2)**0.5

print("Hüpotenuus on:", hüpotenuus)

# ProgÜl0.2
kiirus1 = float(input("Sisesta kiirus 1 (km/h): "))
kiirus2 = float(input("Sisesta kiirus 2 (m/s): "))

kiirus2_kmh = kiirus2 * 3.6

if kiirus1 > kiirus2_kmh:
    print("Kiirus 1 on suurem.")
else:
    print("Kiirus 2 on suurem.")
    
    
# ProgÜl0.3
x = 1

while x < 20:
    t = float(input("Sisesta t väärtus: "))
    y = t + 2 * t - 5
    print("y =", y)
    x = x + 1
    
#Progül.1
N = int(input("Mitu arvu soovite sisestada?: "))
max_arv = None
for i in range(N):
    arv = int(input("Sisestage arv: "))
    if max_arv is None or arv > max_arv:
        max_arv = arv
print("Maksimaalne arv on:", max_arv)

#Progül.2
while True:
    sisend = input("Sisestage täisarv (või 'lopeta', et lõpetada): ")
    if sisend.lower() == "lopeta":
        break
    arv = int(sisend)
    if arv == 13:
        print(77)
    else:
        print(arv)
        

#Progül.3
distants = 10
summa = distants
for i in range(2, 8):
    distants *= 1.1
    summa += distants
print("Kokku läbitud teepikkus 7 päeva jooksul on:", summa)

#Progül.4
M = float(input("Sisestage kanga pikkus meetrites: "))
while True:
    sisend = input("Sisestage järgmise ostja soovitav kogus meetrites (või 'stopp' lõpetamiseks): ")
    if sisend.lower() == "stopp":
        break
    soov = float(sisend)
    if soov <= M:
        M -= soov
        print("Kangas müüdud, järgi jäi:", M, "meetrit")
        if M == 0:
            print("Kangas on täielikult otsas.")
            break
    else:
        print("Materjali ei jätku. Kas soovite osta jäägi?")
        vastus = input("Sisestage 'jah' või 'ei': ")
        if vastus.lower() == "jah":
            print("Müüdud jääk:", M, "meetrit")
            M = 0
            break
        else:
            print("Jätkame järgmise ostjaga.")
            


#Progül.5
while True:
    a = float(input("Sisestage trapezi esimese aluse pikkus: "))
    b = float(input("Sisestage trapezi teise aluse pikkus: "))
    h = float(input("Sisestage trapezi kõrgus: "))
    pindala = (a + b) / 2 * h
    print("Trapezi pindala on:", pindala)
    veel = input("Kas arvutada järgmine trapez? (jah/ei): ")
    if veel.lower() != "jah":
        break
        
#Progül.6
arv = int(input("Sisestage täisarv: "))
if arv % 3 == 0:
    print("Sisestatud arv jagub kolmega ilma jäägita.")
else:
    print("Sisestatud arv ei jagu kolmega ilma jäägita.")