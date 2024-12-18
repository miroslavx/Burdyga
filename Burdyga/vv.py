print("*** NUMBERIMÄNGUD ***")
print()
while True:
    try:
        a = abs(int(input("Sisestage täisarv => ")))
        break
    except ValueError:
        print("See ei ole täisarv")
if a == 0:
    print("Nulliga pole mõtet midagi teha")
else:
    print("Määrame, mitu numbrit on paaris ja mitu paaritu")
    print()
    c = b = a
    paaris = 0
    paaritu = 0

    while b > 0:
        digit = b % 10 
        if digit % 2 == 0:
            paaris += 1 
        else:
            paaritu += 1  
        b = b // 10  

    print("Paaris numbreid:", paaris)
    print("Paaritu numbreid:", paaritu)
    print()

    print("*Pöörame* sisestatud numbri")
    print()
    b = 0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10 + number
    print("*Pööratud* number", b)
    print()

    print("Kontrollime Sirakuusi hüpoteesi")
    print()

    if c % 2 == 0:
        print("c - paaris number. Jagame kahega.")
    else:
        print("c - paaritu number. Korrutame 3-ga, liidame 1 ja jagame kahega.")
    
    while c != 1:
        if c % 2 == 0:
            c = c / 2 
        else:
            c = (3 * c + 1) / 2 
        print(int(c), end=" ")

    print()
    print("Hüpotees on tõene")