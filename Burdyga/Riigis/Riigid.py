import random

def loe_fail(failinimi="riigid_pealinnd.txt"):
    riigid = {}
    try:
        with open(failinimi, 'r', encoding='utf-8') as fail:
            for rida in fail:
                if '-' in rida:
                    riik, pealinn = rida.strip().split('-', 1)
                    riigid[riik] = pealinn
    except FileNotFoundError:
        print("Faili ei leitud! Loome uue tühja sõnastiku.")
    return riigid

def salvesta_fail(riigid, failinimi="riigid_pealinnd.txt"):
    with open(failinimi, 'w', encoding='utf-8') as fail:
        for riik, pealinn in riigid.items():
            fail.write(f"{riik}-{pealinn}\n")

def otsi_pealinn(riigid, riik):
    return riigid.get(riik, "Riiki ei leitud!")

def otsi_riik(riigid, pealinn):
    for riik, peal in riigid.items():
        if peal == pealinn:
            return riik
    return "Pealinna ei leitud!"
def lisa_riik(riigid):
    riik = input("Sisesta riigi nimi: ")
    pealinn = input("Sisesta pealinna nimi: ")
    riigid[riik] = pealinn
    salvesta_fail(riigid)
    print("Lisatud edukalt!")

def paranda_viga(riigid):
    riik = input("Sisesta riigi nimi, mida soovid parandada: ")
    if riik in riigid:
        uus_pealinn = input("Sisesta õige pealinna nimi: ")
        riigid[riik] = uus_pealinn
        salvesta_fail(riigid)
        print("Parandatud edukalt!")
    else:
        print("Riiki ei leitud!")

def test_teadmised(riigid):
    if not riigid:
        print("Sõnastik on tühi!")
        return
    õiged = 0
    kokku = 5 
    küsimused = list(riigid.items())
    for _ in range(min(kokku, len(riigid))):
        riik, pealinn = random.choice(küsimused)
        if random.choice([True, False]):
            vastus = input(f"Mis on {riik} pealinn? ")
            if vastus.lower() == pealinn.lower():
                print("Õige!")
                õiged += 1
            else:
                print(f"Vale! Õige vastus on {pealinn}")
        else:
            vastus = input(f"Mis riigi pealinn on {pealinn}? ")
            if vastus.lower() == riik.lower():
                print("Õige!")
                õiged += 1
            else:
                print(f"Vale! Õige vastus on {riik}")
    
    protsent = (õiged / kokku) * 100
    print(f"\nTulemus: {protsent}% ({õiged}/{kokku} õiget)")

def main():
    riigid = loe_fail()
    while True:
        print("\nValige tegevus:")
        print("1. Otsi pealinna")
        print("2. Otsi riiki")
        print("3. Lisa uus riik")
        print("4. Paranda viga")
        print("5. Testi teadmisi")
        print("6. Välju")
        
        valik = input("Sisesta valik (1-6): ")
        
        if valik == "1":
            riik = input("Sisesta riigi nimi: ")
            print(otsi_pealinn(riigid, riik))
        elif valik == "2":
            pealinn = input("Sisesta pealinna nimi: ")
            print(otsi_riik(riigid, pealinn))
        elif valik == "3":
            lisa_riik(riigid)
        elif valik == "4":
            paranda_viga(riigid)
        elif valik == "5":
            test_teadmised(riigid)
        elif valik == "6":
            print("Head aega!")
            break
        else:
            print("Vale valik!")

if __name__ == "__main__":
    main()
