from MyModule import registreerimine, autoriseerimine, muuda_andmeid, parooli_taastamine

loginid = []
paroolid = []

while True:
    print("\nValige tegevus:")
    print("1. Registreerimine")
    print("2. Autoriseerimine")
    print("3. Nime või parooli muutmine")
    print("4. Unustatud parooli taastamine")
    print("5. Lõpetamine")

    valik = input("Teie valik: ")

    if valik == "1":
        registreerimine(loginid, paroolid)
    elif valik == "2":
        autoriseerimine(loginid, paroolid)
    elif valik == "3":
        muuda_andmeid(loginid, paroolid)
    elif valik == "4":
        parooli_taastamine(loginid, paroolid)
    elif valik == "5":
        print("Programmi lõpetamine.")
        break
    else:
        print("Vale valik, proovige uuesti!")