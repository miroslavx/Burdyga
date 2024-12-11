import math

# �lesanne 1
number = float(input("Sisestage arv: "))

if number > 0:
    if number % 2 == 0:
        print("Arv on positiivne ja paarisarv.")
    else:
        print("Arv on positiivne ja paaritu arv.")
elif number < 0:
    print("Arv on negatiivne.")
else:
    print("Arv on null.")

# �lesanne 2
a = int(input("Sisestage esimene nurk: "))
b = int(input("Sisestage teine nurk: "))
c = int(input("Sisestage kolmas nurk: "))

if a > 0 and b > 0 and c > 0 and a + b + c == 180:
    if a == b == c:
        print("See on v�rdk�lgne kolmnurk.")
    elif a == b or b == c or a == c:
        print("See on v�rdhaarne kolmnurk.")
    else:
        print("See on erik�lgne kolmnurk.")
else:
    print("Need nurgad ei saa moodustada kolmnurka.")

# �lesanne 3
vastus = input("Kas soovite n�dala p�eva numbrit p�evanimeks t�lkida? (jah/ei): ").strip().lower()

if vastus == "jah":
    number = int(input("Sisestage p�evanumber (1-7): "))
    n�dalap�evad = ["Esmasp�ev", "Teisip�ev", "Kolmap�ev", "Neljap�ev", "Reede", "Laup�ev", "P�hap�ev"]
    
    if 1 <= number <= 7:
        print(f"See on {n�dalap�evad[number - 1]}.")
    else:
        print("Palun sisestage arv vahemikus 1 kuni 7.")
else:
    print("T�lget ei soovitud.")

# �lesanne 4
def leia_tahtkuju(p�ev, kuu):
    if (kuu == 1 and 20 <= p�ev <= 31) or (kuu == 2 and 1 <= p�ev <= 18):
        return "Veevalaja"
    elif (kuu == 2 and 19 <= p�ev <= 29) or (kuu == 3 and 1 <= p�ev <= 20):
        return "Kalad"
    elif (kuu == 3 and 21 <= p�ev <= 31) or (kuu == 4 and 1 <= p�ev <= 19):
        return "J��r"
    elif (kuu == 4 and 20 <= p�ev <= 30) or (kuu == 5 and 1 <= p�ev <= 20):
        return "S�nn"
    elif (kuu == 5 and 21 <= p�ev <= 31) or (kuu == 6 and 1 <= p�ev <= 20):
        return "Kaksikud"
    elif (kuu == 6 and 21 <= p�ev <= 30) or (kuu == 7 and 1 <= p�ev <= 22):
        return "V�hk"
    elif (kuu == 7 and 23 <= p�ev <= 31) or (kuu == 8 and 1 <= p�ev <= 22):
        return "L�vi"
    elif (kuu == 8 and 23 <= p�ev <= 31) or (kuu == 9 and 1 <= p�ev <= 22):
        return "Neitsi"
    elif (kuu == 9 and 23 <= p�ev <= 30) or (kuu == 10 and 1 <= p�ev <= 22):
        return "Kaalud"
    elif (kuu == 10 and 23 <= p�ev <= 31) or (kuu == 11 and 1 <= p�ev <= 21):
        return "Skorpion"
    elif (kuu == 11 and 22 <= p�ev <= 30) or (kuu == 12 and 1 <= p�ev <= 21):
        return "Ambur"
    elif (kuu == 12 and 22 <= p�ev <= 31) or (kuu == 1 and 1 <= p�ev <= 19):
        return "Kaljukits"
    else:
        return None

try:
    p�ev = int(input("Sisestage s�nnikuup�ev (1-31): "))
    kuu = int(input("Sisestage s�nnikuu (1-12): "))
    
    t�htkuju = leia_tahtkuju(p�ev, kuu)
    if t�htkuju:
        print(f"Teie t�htkuju on {t�htkuju}.")
    else:
        print("Sisestasite kehtetu kuup�eva.")
except ValueError:
    print("Palun sisestage kehtiv arv.")

# �lesanne 5
sisend = input("Sisestage v��rtus: ")

try:
    if "." in sisend or "," in sisend:
        arv = float(sisend.replace(",", "."))
        print(f"70% sellest arvust on {arv * 0.7}.")
    else:
        arv = int(sisend)
        print(f"50% sellest arvust on {arv * 0.5}.")
except ValueError:
    print(f"Sisestasite teksti: {sisend}")

#�lesanne 6

# K�si kasutajalt, kas ta soovib v�rrandit lahendada
vastus = input("Kas soovite ruutv�rrandit lahendada? (jah/ei): ").strip().lower()

if vastus == "jah":
    # Sisesta a, b ja c
    try:
        a = float(input("Sisestage a: "))
        b = float(input("Sisestage b: "))
        c = float(input("Sisestage c: "))
        
        if a == 0:
            print("Tegemist ei ole ruutv�rrandiga, kuna a = 0.")
        else:
            # Diskriminandi arvutamine
            D = b**2 - 4 * a * c
            
            print(f"Diskriminant D = {D}")
            
            if D > 0:
                # Kui D > 0, kaks lahendit
                x1 = (-b + math.sqrt(D)) / (2 * a)
                x2 = (-b - math.sqrt(D)) / (2 * a)
                print(f"Kaks lahendit: x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")
            elif D == 0:
                # Kui D = 0, �ks lahend
                x = -b / (2 * a)
                print(f"�ks lahend: x = {round(x, 2)}")
            else:
                # Kui D < 0, lahendid puuduvad
                print("Reaalarvulisi lahendeid ei ole, kuna D < 0.")
    except ValueError:
        print("Sisestage numbrilised v��rtused.")
else:
    print("Lahendamist ei soovitud. Head p�eva!")
	
