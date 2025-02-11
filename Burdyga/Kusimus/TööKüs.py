import random

def loe_kusimused(failinimi):
    kus_vas = {}
    with open(failinimi, 'r', encoding='utf-8-sig') as f:
        for rida in f:
            osad = rida.strip().split(':')
            if len(osad) >= 2:
                kusimus = osad[0]
                vastus = ':'.join(osad[1:])
                kus_vas[kusimus] = vastus
    return kus_vas

def küsi_kandidaat(kus_vas):
    nimi = input("Sisesta oma nimi: ")
    õiged = 0
    valitud = random.sample(list(kus_vas.keys()), 5)
    for küsimus in valitud:
        print(küsimus)
        vastus = input("Sinu vastus: ")
        if vastus.strip().lower() == kus_vas[küsimus].strip().lower():
            õiged += 1
    return nimi, õiged

def lisa_faili(failinimi, andmed, rea_formaat):
    with open(failinimi, 'a', encoding='utf-8-sig') as f:
        f.write(rea_formaat.format(*andmed) + '\n')

def loe_fail(failinimi):
    try:
        with open(failinimi, 'r', encoding='utf-8-sig') as f:
            return [rida.strip() for rida in f]
    except FileNotFoundError:
        return []

def kirjuta_fail(failinimi, sisu):
    with open(failinimi, 'w', encoding='utf-8-sig') as f:
        for line in sisu:
            f.write(line + '\n')

def kuva_fail(failinimi, pealkiri):
    print(f"\n{pealkiri}:")
    sisu = loe_fail(failinimi)
    for rida in sisu:
        print(rida)

kus_vas = loe_kusimused('kusimused_vastused.txt')
kandidaadid = []

for _ in range(5):
    nimi, õiged = küsi_kandidaat(kus_vas)
    kandidaadid.append((nimi, õiged))

vastuvõetud = []
eisoobi = []

for nimi, õiged in kandidaadid:
    if õiged >= 3:
        vastuvõetud.append((nimi, õiged))
    else:
        eisoobi.append(nimi)

vastuvõetud.sort(key=lambda x: (-x[1], x[0]))
eisoobi.sort()

kirjuta_fail('vastuvõetud.txt', [f"{nimi}:{õiged}" for nimi, õiged in vastuvõetud])
kirjuta_fail('eisoobi.txt', eisoobi)

kuva_fail('vastuvõetud.txt', "Vastuvõetud kandidaadid")
kuva_fail('eisoobi.txt', "Eisoobi kandidaadid")