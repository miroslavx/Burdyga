import random

def genereeri_parool():
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0 + str1 + str2 + str3
    ls = list(str4)
    random.shuffle(ls)
    parool = ''.join([random.choice(ls) for _ in range(12)])
    return parool

def parooli_kontroll(parool):
    erimargid = ".,:;!_*-+()/#¤%&"
    on_num = any(c.isdigit() for c in parool)
    on_väike = any(c.islower() for c in parool)
    on_suur = any(c.isupper() for c in parool)
    on_erimärk = any(c in erimargid for c in parool)
    return on_num and on_väike and on_suur and on_erimärk

def registreeri(logid, paroolid):
    kasutaja = input("Sisesta kasutajanimi: ")
    if kasutaja in logid:
        print("See kasutajanimi on juba olemas!")
        return
    valik = input("Kas soovid parooli genereerida (G) või ise luua (M)? ").upper()
    if valik == 'G':
        parool = genereeri_parool()
        print(f"Genereeritud parool: {parool}")
    elif valik == 'M':
        while True:
            parool = input("Sisesta oma parool: ")
            if parooli_kontroll(parool):
                break
            else:
                print("Parool peab sisaldama vähemalt ühte numbrit, väike- ja suurtähte ning erimärki!")
    else:
        print("Vigane valik!")
        return
    logid.append(kasutaja)
    paroolid.append(parool)
    print("Kasutaja registreeritud!")

def autoriseeri(logid, paroolid):
    kasutaja = input("Sisesta kasutajanimi: ")
    parool = input("Sisesta parool: ")
    if kasutaja in logid:
        indeks = logid.index(kasutaja)
        if paroolid[indeks] == parool:
            print("Autoriseerimine õnnestus!")
            return indeks
        else:
            print("Vale parool!")
    else:
        print("Kasutajat ei leitud!")
    return -1

def muuda_andmeid(logid, paroolid):
    indeks = autoriseeri(logid, paroolid)
    if indeks == -1:
        return
    valik = input("Muuda nime (N) või parooli (P)? ").upper()
    if valik == 'N':
        uus_nimi = input("Sisesta uus kasutajanimi: ")
        if uus_nimi in logid:
            print("See nimi on juba kasutusel!")
        else:
            logid[indeks] = uus_nimi
            print("Nimi muudetud!")
    elif valik == 'P':
        valik = input("Genereeri parool (G) või sisesta ise (M)? ").upper()
        if valik == 'G':
            uus_parool = genereeri_parool()
            print(f"Uus parool: {uus_parool}")
            paroolid[indeks] = uus_parool
        elif valik == 'M':
            while True:
                uus_parool = input("Sisesta uus parool: ")
                if parooli_kontroll(uus_parool):
                    break
                else:
                    print("Parool peab sisaldama vähemalt ühte numbrit, väike- ja suurtähte ning erimärki!")
            paroolid[indeks] = uus_parool
        else:
            print("Vigane valik!")
    else:
        print("Vigane valik!")

def taasta_parool(logid, paroolid):
    kasutaja = input("Sisesta kasutajanimi: ")
    if kasutaja in logid:
        indeks = logid.index(kasutaja)
        uus_parool = genereeri_parool()
        paroolid[indeks] = uus_parool
        print(f"Uus parool: {uus_parool}")
    else:
        print("Kasutajat ei leitud!")
