from MinuOmaMoodul import *
#C:/Users/marina.oleinik/source/repos/Aut_Reg/Salas�nad.txt
salas�nad=loe_failist("Salas�nad.txt")
kasutajanimed=loe_failist("Kasutajad.txt")
while True:
    print(kasutajanimed)
    print(salas�nad)
    print("1-registreerimine\n2-autoriseerimine\n3-nime v�i parooli muutmine\n4-unustanud parooli taastamine\n5-l�petamine\n")
    vastus=int(input("Sisestage arv"))
    if vastus==1:
        print("Registreerimine")
        kasutajanimed,salas�nad=registreerimine(kasutajanimed,salas�nad)
    elif vastus==2:
        print("Autoriseerimine")
        autoriseerimine(kasutajanimed,salas�nad)
    elif vastus==3:
        print("Nime v�i parooli muutmine")
        vastus=input("Kas muudame nime, parooli v�i m�lemad")
        if vastus=="nimi":
            kasutajanimed=nimi_v�i_parooli_muurmine(kasutajanimed)
        elif vastus=="parool":
            salas�nad=nimi_v�i_parooli_muurmine(salas�nad)
        elif vastus=="m�lemad":
            print("Nimi muutmine: ")
            kasutajanimed=nimi_v�i_parooli_muurmine(kasutajanimed)
            print("Parooli muutmine: ")
            salas�nad=nimi_v�i_parooli_muurmine(salas�nad)
    elif vastus==4:
        print("Unustanud parooli taastamine")

    elif vastus==5:
        print("L�petamine")

        break
    else:
        print("Tundmatu valik")
