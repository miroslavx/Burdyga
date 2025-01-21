
ikoodid = []
arvud = []

while True:
    isikukood = input("Sisesta isikukood: ")
    
    if isikukood.lower() == "stop":
        break
        
    if len(isikukood) != 11:
        arvud.append(isikukood)
        print("Vale pikkus")
        continue
        
    esimene = isikukood[0]
    if esimene not in "123456":
        arvud.append(isikukood)
        continue
        
    kuu = int(isikukood[3:5])
    paev = int(isikukood[5:7])
    
    if kuu < 1 or kuu > 12 or paev < 1 or paev > 31:
        arvud.append(isikukood)
        continue
        
    # Kontrollnumber
    astme1 = [1,2,3,4,5,6,7,8,9,1]
    astme2 = [3,4,5,6,7,8,9,1,2,3]
    
    summa1 = 0
    for i in range(10):
        summa1 += int(isikukood[i]) * astme1[i]
    
    jaak1 = summa1 % 11
    
    if jaak1 == 10:
        summa2 = 0
        for i in range(10):
            summa2 += int(isikukood[i]) * astme2[i]
        jaak2 = summa2 % 11
        if jaak2 == 10:
            kontroll = 0
        else:
            kontroll = jaak2
    else:
        kontroll = jaak1
        
    if int(isikukood[10]) != kontroll:
        arvud.append(isikukood)
        continue
    
    sugu = "naine" if esimene in "246" else "mees"
    
    kood = int(isikukood[7:10])
    
    if 1 <= kood <= 10:
        haigla = "Kuressaare Haigla"
    elif 11 <= kood <= 19:
        haigla = "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif 21 <= kood <= 220:
        haigla = "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"  
    elif 221 <= kood <= 270:
        haigla = "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif 271 <= kood <= 370:
        haigla = "Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif 371 <= kood <= 420:
        haigla = "Narva Haigla"
    elif 421 <= kood <= 470:
        haigla = "Pärnu Haigla"
    elif 471 <= kood <= 490:
        haigla = "Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif 491 <= kood <= 520:
        haigla = "Järvamaa Haigla (Paide)"
    elif 521 <= kood <= 570:
        haigla = "Rakvere, Tapa haigla"
    elif 571 <= kood <= 600:
        haigla = "Valga Haigla"
    elif 601 <= kood <= 650:
        haigla = "Viljandi Haigla"
    elif 651 <= kood <= 700:
        haigla = "Lõuna-Eesti Haigla (Võru), Põlva Haigla"
        
    aasta = isikukood[1:3]
    sajand = "20" if esimene in "456" else "19"
    
    print(f"See on {sugu}, tema sünnipäev on {paev}.{kuu}.{sajand}{aasta} ja sünnikoht on {haigla}")
    
    ikoodid.append(isikukood)

arvud.sort()
ikoodid.sort(key=lambda x: ("135".find(x[0]), x))

print("\nValed isikukoodid:", arvud)
print("\nÕiged isikukoodid:", ikoodid)
