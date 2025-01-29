def registreerimine(loginid, paroolid):
    kasutajanimi = input("Sisestage uus kasutajanimi: ")
    if kasutajanimi in loginid:
        print("Kasutajanimi on juba olemas!")
        return

    print("Valige parooli loomise viis:")
    print("1. Automaatne parooli genereerimine")
    print("2. Sisestage parool ise")
    valik = input("Teie valik (1 või 2): ")

    if valik == "1":
        parool = loo_parool()
        print("Teie automaatselt genereeritud parool on:", parool)
    elif valik == "2":
        parool = input("Sisestage parool: ")
    else:
        print("Vale valik!")
        return

    loginid.append(kasutajanimi)
    paroolid.append(parool)
    print("Registreerimine õnnestus!")


def loo_parool():
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = "0123456789"
    str2 = "qwertyuiopasdfghjklzxcvbnm"
    str3 = "QWERTYUIOPASDFGHJKLZXCVBNM"
    str4 = str0 + str1 + str2 + str3
    ls = list(str4)
    parool = ""
    for i in range(12):
        indeks = (i * 7 + 3) % len(ls)
        parool += ls[indeks]
    return parool


def autoriseerimine(loginid, paroolid):
    kasutajanimi = input("Sisestage kasutajanimi: ")
    if kasutajanimi not in loginid:
        print("Kasutajanime ei leitud!")
        return

    parool = input("Sisestage parool: ")
    indeks = loginid.index(kasutajanimi)

    if paroolid[indeks] == parool:
        print("Autoriseerimine õnnestus!")
    else:
        print("Vale parool!")


def muuda_andmeid(loginid, paroolid):
    kasutajanimi = input("Sisestage kasutajanimi: ")
    if kasutajanimi not in loginid:
        print("Kasutajanime ei leitud!")
        return

    parool = input("Sisestage vana parool: ")
    indeks = loginid.index(kasutajanimi)

    if paroolid[indeks] == parool:
        print("Mida soovite muuta?")
        print("1. Kasutajanime")
        print("2. Parooli")
        valik = input("Teie valik (1 või 2): ")

        if valik == "1":
            uus_nimi = input("Sisestage uus kasutajanimi: ")
            if uus_nimi in loginid:
                print("Selline nimi on juba kasutusel!")
                return
            loginid[indeks] = uus_nimi
            print("Kasutajanimi muudetud!")
        elif valik == "2":
            uus_parool = input("Sisestage uus parool: ")
            paroolid[indeks] = uus_parool
            print("Parool muudetud!")
        else:
            print("Vale valik!")
    else:
        print("Vale parool!")


def parooli_taastamine(loginid, paroolid):
    kasutajanimi = input("Sisestage kasutajanimi: ")
    if kasutajanimi not in loginid:
        print("Kasutajanime ei leitud!")
        return

    uus_parool = loo_parool()
    indeks = loginid.index(kasutajanimi)
    paroolid[indeks] = uus_parool
    print("Teie uus parool on:", uus_parool)