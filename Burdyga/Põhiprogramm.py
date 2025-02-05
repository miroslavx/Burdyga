from MyModule import registreeri, autoriseeri, muuda_andmeid, taasta_parool

logid = []
paroolid = []

while True:
    print("\nVali tegevus:")
    print("1. Registreerimine")
    print("2. Autoriseerimine")
    print("3. Muuda nime/parooli")
    print("4. Taasta parool")
    print("5. Välju")
    valik = input("Sisesta number (1-5): ")

    if valik == '1':
        registreeri(logid, paroolid)
    elif valik == '2':
        autoriseeri(logid, paroolid)
    elif valik == '3':
        muuda_andmeid(logid, paroolid)
    elif valik == '4':
        taasta_parool(logid, paroolid)
    elif valik == '5':
        print("Head aega!")
        break
    else:
        print("Vigane valik!")
