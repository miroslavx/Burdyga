import string
import random
vokaali=["a","e","u","o","i","ü","õ","ö","ä"]
konsonanti="qwrtpsdfghklzxcvbnm"

markid=string.punctuation #%&'()*+,-./:;<=>?@[\]^_^{|}~

v=k=m=t=0
while True:
    tekst=input("Siseta mingi tekst: ").lower()
    if tekst.isdigit():
        break
    else:
        tekst_list=list(tekst)
        print(tekst_list)
        for taht in tekst_list:
            if taht in vokaali:
                v+=1
            elif taht in konsonanti:
                k+=1
            elif taht in markid:
                m+=1
            elif taht == "":
                t+=1
    print("Vokaali:", v)
    print("Konsotani:", k)
    print("Märki:", m)
    print("Tühikud:", t)


# Ülesanne 2.1

nimed_21 = []
for i in range(5):
    sisend_nimi = input("Sisesta nimi: ")
    nimed_21.append(sisend_nimi)

print("\nTähestikulises järjekorras nimed:")
for n in sorted(nimed_21):
    print(n)

print("\nViimane lisatud nimi:", nimed_21[-1])

muutmise_valik = input("\nKas tahad mõnda nime muuta? (jah/ei): ").lower()
if muutmise_valik == "jah":
    indeks_21 = int(input("Mitmendat nime (1-5) tahad muuta?: "))
    uus_nimi_21 = input("Sisesta uus nimi: ")
    nimed_21[indeks_21 - 1] = uus_nimi_21
    print("Uuendatud nimed:", nimed_21)
else:
    print("Nimesid ei muudeta.")

#Ülesanne 2.2
opilased = ["Juhan", "Kati", "Mario", "Mario", "Mati", "Mati"]
unikaalsed = []
for nimi in opilased:
    if nimi not in unikaalsed:
        unikaalsed.append(nimi)

print("Nimed ilma kordusteta:", unikaalsed)

# Ülesanne 2.3
vanused_23 = [12, 45, 67, 23, 19]
print("Vanused:", vanused_23)
print("Suurim vanus:", max(vanused_23))
print("Väikseim vanus:", min(vanused_23))
kogusumma_23 = sum(vanused_23)
print("Kogusumma:", kogusumma_23)
keskmine_23 = kogusumma_23 / len(vanused_23)
print("Keskmine:", keskmine_23)

# Ülesanne 3 (Tärnid)

arvud_3 = [10, 5, 15, 8, 12]
for arv in arvud_3:
    print("*" * arv)

# Ülesanne 4 
indeks_4 = input("Sisesta postiindeks (5 numbrit): ")
if len(indeks_4) == 5 and indeks_4.isdigit():
    esimene_number_4 = indeks_4[0]
    maakond_4 = ""
    if esimene_number_4 == "1":
        maakond_4 = "Tallinn"
    elif esimene_number_4 == "2":
        maakond_4 = "Narva, Narva-Jõesuu"
    elif esimene_number_4 == "3":
        maakond_4 = "Kohtla-Järve"
    elif esimene_number_4 == "4":
        maakond_4 = "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa"
    elif esimene_number_4 == "5":
        maakond_4 = "Tartu linn"
    elif esimene_number_4 == "6":
        maakond_4 = "Tartumaa, Põlvamaa, Võrumaa, Valgamaa"
    elif esimene_number_4 == "7":
        maakond_4 = "Viljandimaa, Järvamaa, Harjumaa, Raplamaa"
    elif esimene_number_4 == "8":
        maakond_4 = "Pärnumaa"
    elif esimene_number_4 == "9":
        maakond_4 = "Läänemaa, Hiiumaa, Saaremaa"
    else:
        maakond_4 = "Tundmatu piirkond"

    print("See postiindeks kuulub:", maakond_4)

    if "Narva" in maakond_4 or "Tallinn" in maakond_4 or "Kohtla-Järve" in maakond_4:
        print("Оставайтесь дома!")
    else:
        print("Носите маски!")
else:
    print("Sisestatud postiindeks ei ole korrektne!")

# Ülesanne 5 Vahetus

loend_5 = [10, 20, 30, 40, 50, 60]
print("Algne loend:", loend_5)

mitu_vahetada_5 = int(input("Mitu paari soovid vahetada? "))
for i in range(mitu_vahetada_5):
    if i >= len(loend_5)//2:
        break
    loend_5[i], loend_5[-1 - i] = loend_5[-1 - i], loend_5[i]

print("Pärast vahetust:", loend_5)

# Ülesanne 6 Bespoleznoje "bespalk" arv

numbrid_6 = [2, 5, 9, 1, 9, 3]
print("Algne loend:", numbrid_6)
suurim_6 = max(numbrid_6)
positsioon_6 = numbrid_6.index(suurim_6)
asendus_6 = suurim_6 / len(numbrid_6)
numbrid_6[positsioon_6] = asendus_6
print("Uus loend:", numbrid_6)


# Ülesanne 7 
print("=== Ülesanne 7 ===")

numbrid_7 = [3, -1, -7, 4, -2, 10]
print("Algne loend:", numbrid_7)
kasvav_abs_7 = sorted(numbrid_7, key=abs)
kahanev_abs_7 = sorted(numbrid_7, key=abs, reverse=True)

print("Kasvav abs-järjekord:", kasvav_abs_7)
print("Kahanev abs-järjekord:", kahanev_abs_7)

# Ülesanne 8 
sonad_8 = ['крот', 'белка', 'выхухоль']
pikim_8 = max(len(s) for s in sonad_8)
uued_8 = []
for s_8 in sonad_8:
    l_8 = len(s_8)
    erinevus_8 = pikim_8 - l_8
    uued_8.append(s_8 + "_" * erinevus_8)

print("Algne:", sonad_8)
print("Muudetud:", uued_8)
print("\nTeine näide:")
sonad_8b = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
pikim_8b = max(len(s) for s in sonad_8b)
uued_8b = []
for s_8b in sonad_8b:
    erinevus_8b = pikim_8b - len(s_8b)
    uued_8b.append(s_8b + "_" * erinevus_8b)

print("Algne:", sonad_8b)
print("Muudetud:", uued_8b)

# Ülesanne 9 (Nimi kontroll)

sisestatud_nimi_9 = input("Sisesta oma nimi: ")
if not sisestatud_nimi_9.isalpha():
    print("Nimi peab sisaldama ainult tähti!")
else:
    tervitus_9 = sisestatud_nimi_9.capitalize()
    print("Tere,", tervitus_9 + "!")
    pikkus_9 = len(sisestatud_nimi_9)
    print("Sinu nimes on", pikkus_9, "tähte.")
    tahishaalikud_9 = "aeiouõüöä"
    tahish_count_9 = 0

    for t_9 in sisestatud_nimi_9:
        if t_9 in tahishaalikud_9:
            tahish_count_9 += 1

    kaash_count_9 = pikkus_9 - tahish_count_9
    print("Täishäälikuid:", tahish_count_9)
    print("Kaashäälikuid:", kaash_count_9)
    unikaalsed_9 = sorted(set(sisestatud_nimi_9.lower()))
    print("Nimes esinevad tähed (ilma korduseta, a-z):", "".join(unikaalsed_9))


# Ülesanne 10

andmed_10 = [
    "Aadu Suur;56;2500",
    "Malle Kapsas;42;1500",
    "Uudo Koba;32;700",
    "Tiit Kopikas;22;550",
    "Vahur Vana;67;870"]
nimed_10 = []
vanused_10 = []
palgad_10 = []
for rida_10 in andmed_10:
    osad_10 = rida_10.split(";")
    nimed_10.append(osad_10[0])
    vanused_10.append(int(osad_10[1]))
    palgad_10.append(int(osad_10[2]))
suurim_palk_10 = max(palgad_10)
indeks_suurim_10 = palgad_10.index(suurim_palk_10)
print("Kõige suurema palgaga töötaja on:", nimed_10[indeks_suurim_10], 
      "palgaga", suurim_palk_10)

keskmine_palk_10 = sum(palgad_10) / len(palgad_10)
print("Keskmine palk on:", keskmine_palk_10)
ule_keskmise_10 = 0
for p_10 in palgad_10:
    if p_10 > keskmine_palk_10:
        ule_keskmise_10 += 1
print("Keskmisest suuremat palka teenib:", ule_keskmise_10, "inimest.")
vanused_vahem_10 = []
vanused_suurem_10 = []
for i_10 in range(len(palgad_10)):
    if palgad_10[i_10] <= keskmine_palk_10:
        vanused_vahem_10.append(vanused_10[i_10])
    else:
        vanused_suurem_10.append(vanused_10[i_10])
if len(vanused_vahem_10) > 0:
    keskmine_vahem_10 = sum(vanused_vahem_10) / len(vanused_vahem_10)
else:
    keskmine_vahem_10 = 0
if len(vanused_suurem_10) > 0:
    keskmine_suurem_10 = sum(vanused_suurem_10) / len(vanused_suurem_10)
else:
    keskmine_suurem_10 = 0

print("Keskmine vanus neil, kes teenivad kuni/alla keskmise:", keskmine_vahem_10)
print("Keskmine vanus neil, kes teenivad üle keskmise:", keskmine_suurem_10)



#ülesanne 12

loend_12 = []
for i_12 in range(10):
    loend_12.append(random.randint(1, 100))
print("Algne loend:", loend_12)
min_arv_12 = min(loend_12)
max_arv_12 = max(loend_12)
i_min_12 = loend_12.index(min_arv_12)
i_max_12 = loend_12.index(max_arv_12)

loend_12[i_min_12], loend_12[i_max_12] = loend_12[i_max_12], loend_12[i_min_12]
print("Pärast min-max vahetust:", loend_12)

#ulesanne 13 (Arva sõna ära)


sonad_13 = ["auto", "kool", "linn", "python"]
salajane_13 = random.choice(sonad_13)
tulemus_13 = ["_" for _ in salajane_13]
valed_13 = []
katsete_arv_13 = 0

while True:
    print("Praegune seis:", " ".join(tulemus_13))
    sisestus_13 = input("Pakku üks täht: ").lower()
    katsete_arv_13 += 1

    if sisestus_13 in salajane_13:
        for ix, t in enumerate(salajane_13):
            if t == sisestus_13:
                tulemus_13[ix] = t
        if "_" not in tulemus_13:
            print("Tubli! Arvasid sõna ära:", salajane_13)
            print("Katsete arv:", katsete_arv_13)
            break
    else:
        if sisestus_13 not in valed_13:
            valed_13.append(sisestus_13)
        print("Vale täht! Vale pakutud tähed:", valed_13)

# Ülesanne 14

linnad_14 = ["Pariis", "Berliin", "Rooma", "Madrid", "Helsingi",
             "London", "Oslo", "Kopenhaagen", "Ateena", "Praha"]
print("Algsed linnad:")
for linn_14 in linnad_14:
    print(linn_14)
linnad_14.sort()
print("\nTähestikulises järjekorras:", linnad_14)
for _ in range(2):
    uus_linn_14 = input("Lisa uus Euroopa pealinn: ")
    linnad_14.append(uus_linn_14)
linnad_14.sort()
print("\nTähestikulises järjekorras koos lisatutega:")
for i_14, pealinn_14 in enumerate(linnad_14, start=1):
    print(f"{i_14}. {pealinn_14}")
print("Meie järjendis on", len(linnad_14), "Euroopa pealinna.")

# Ülesanne 15
arv_15 = [1, 2, 3, 4]
eesti_15 = ["üks", "kaks", "kolm", "neli"]
inglise_15 = ["one", "two", "three", "four"]
itaalia_15 = ["uno", "due", "tre", "quattro"]
for i_15 in range(len(arv_15)):
    print(arv_15[i_15], "-", eesti_15[i_15], "-", inglise_15[i_15], "-", itaalia_15[i_15])

arv_15.extend([5, 6])
eesti_15.extend(["viis", "kuus"])

if "tre" in itaalia_15:
    print("\nItaalia loendis leidub 'tre'.")
print("\nSorteeritud (tähestikulises järjekorras):")
print("Eesti:", sorted(eesti_15))
print("Inglise:", sorted(inglise_15))
print("Itaalia:", sorted(itaalia_15))
print("Arvud:", sorted(arv_15))

#ülesanne 16
vastused_16 = [
    "Jah, kindlasti!",
    "Jah!",
    "Võib-olla!",
    "Ei!"]
print("Esita mulle jah/ei küsimus.")
kusimus_16 = input("Sisesta oma küsimus: ")
valik_16 = random.choice(vastused_16)
print("Sinu küsimus:", kusimus_16)
print("Vastus:", valik_16)

# Ülesanne 17
sonad_17 = ["automobiil", "karu", "auto", "maastur", "arvuti", "python", "kaotama", "taotlus"]
otsing_17 = input("Sisesta otsingusõna: ")
print("Sobivad tulemused:")
for s_17 in sonad_17:
    if otsing_17 in s_17:
        print(s_17)

# Ülesanne 18
sona_list_18 = []
for i_18 in range(5):
    sona_18 = input("Sisesta üks sõna: ")
    sona_list_18.append(sona_18)
pikim_sona_18 = max(sona_list_18, key=len)
print("Kõige pikem sisestatud sõna on:", pikim_sona_18)
