import tkinter as tk
import random
from tkinter import messagebox
KATSEID = 6
TAHTE_ARV = 5
sonad_fail = "sonad.txt"
tulemused_fail = "tulemused.txt"
salajane_sona = ""
praegune_katsetus = 0
praegused_tahed = []
kasutatud_tahed = {}

vylja_raam = None
lauarakud = []
klahvid = {}
kontroll_nupp = None
sonumi_silt = None

def prochitat_sonafailist():
    try:
        with open(sonad_fail, "r", encoding="utf-8") as f:
            return [sona.strip().upper() for sona in f if len(sona.strip()) == TAHTE_ARV]
    except FileNotFoundError:
        messagebox.showerror("Oshibka", f"Fayl {sonad_fail} ne nayden!")
        return []
def vybrat_sona():
    sonad = prochitat_sonafailist()
    if not sonad:
        messagebox.showerror("Oshibka", "Fayl slov pustoy ili povrezhden!")
        return None
    return random.choice(sonad)

def sozdat_menyu(root):
    menyu = tk.Menu(root)
    root.config(menu=menyu)
    mangu_menyu = tk.Menu(menyu, tearoff=0)
    mangu_menyu.add_command(label="Novaya igra", command=novaya_igra)
    mangu_menyu.add_command(label="Vyyti", command=root.quit)
    menyu.add_cascade(label="Igra", menu=mangu_menyu)

def sozdat_polye(root):
    global vylja_raam, lauarakud
    vylja_raam = tk.Frame(root)
    vylja_raam.pack(pady=10)
    
    lauarakud = []
    for rida in range(KATSEID):
        rea_rakud = []
        for veerg in range(TAHTE_ARV):
            rakk = tk.Label(vylja_raam, 
                           text=" ", 
                           font=("Arial", 24, "bold"), 
                           width=2, 
                           relief="solid",
                           bg="white")
            rakk.grid(row=rida, column=veerg, padx=5, pady=5)
            rea_rakud.append(rakk)
        lauarakud.append(rea_rakud)
def sozdat_klaviatuur(root):
    global klahvid, kontroll_nupp
    klaviatuuri_raam = tk.Frame(root)
    klaviatuuri_raam.pack(pady=10)
    
    klaviatuuri_ryady = [
        ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "Õ"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", "Ü", "Ö", "Ä"],
        ["Z", "X", "C", "V", "B", "N", "M"]
    ]
    
    klahvid = {}
    for ryad in klaviatuuri_ryady:
        rea_raam = tk.Frame(klaviatuuri_raam)
        rea_raam.pack()
        for taht in ryad:
            nupp = tk.Button(rea_raam, 
                            text=taht,
                            font=("Arial", 12),
                            width=2,
                            command=lambda t=taht: dobavit_taht(t))
            nupp.pack(side=tk.LEFT, padx=2, pady=2)
            klahvid[taht] = nupp
  
    spets_raam = tk.Frame(klaviatuuri_raam)
    spets_raam.pack(pady=5)
    tk.Button(spets_raam, text="Nazad", command=nazad).pack(side=tk.LEFT, padx=5)
    kontroll_nupp = tk.Button(spets_raam, text="Proverit", command=proverit)
    kontroll_nupp.pack(side=tk.LEFT, padx=5)
    kontroll_nupp.config(state=tk.DISABLED)
  
def sozdat_sonumi_silt(root):
    global sonumi_silt
    sonumi_silt = tk.Label(root, 
                          text="", 
                          font=("Arial", 14),
                          fg="red")
    sonumi_silt.pack(pady=10)

def dobavit_taht(taht):
    global praegused_tahed, praegune_katsetus
    if len(praegused_tahed) < TAHTE_ARV and praegune_katsetus < KATSEID:
        praegused_tahed.append(taht)
        pozitsiya = len(praegused_tahed) - 1
        lauarakud[praegune_katsetus][pozitsiya].config(text=taht)
        kontroll_nupp.config(state=tk.NORMAL if len(praegused_tahed) == TAHTE_ARV else tk.DISABLED)

def nazad():
    global praegused_tahed, praegune_katsetus
    if praegused_tahed:
        pozitsiya = len(praegused_tahed) - 1
        lauarakud[praegune_katsetus][pozitsiya].config(text=" ")
        praegused_tahed.pop()
        kontroll_nupp.config(state=tk.NORMAL if len(praegused_tahed) == TAHTE_ARV else tk.DISABLED)

def proverit():
    global praegused_tahed, praegune_katsetus, salajane_sona
    pakkumine = "".join(praegused_tahed)
    tsveta = proverit_katset(pakkumine)
    
    for i, tsvet in enumerate(tsveta):
        lauarakud[praegune_katsetus][i].config(bg=tsvet)
        taht = pakkumine[i]
        if taht in klahvid:
            obnovit_tsvet_klavishi(taht, tsvet)
  
    if pakkumine == salajane_sona:
        zavershit_igru(pobeda=True)
    elif praegune_katsetus == KATSEID - 1:
        zavershit_igru(pobeda=False)
    else:
        praegune_katsetus += 1
        praegused_tahed = []
        kontroll_nupp.config(state=tk.DISABLED)

def proverit_katset(pakkumine):
    global salajane_sona
    tsveta = ["gray"] * TAHTE_ARV
    temp_sona = list(salajane_sona)
    for i in range(TAHTE_ARV):
        if pakkumine[i] == temp_sona[i]:
            tsveta[i] = "green"
            temp_sona[i] = None
    for i in range(TAHTE_ARV):
        if tsveta[i] != "green" and pakkumine[i] in temp_sona:
            tsveta[i] = "yellow"
            temp_sona.remove(pakkumine[i])
    
    return tsveta
def obnovit_tsvet_klavishi(taht, novy_tsvet):
    tekushchiy_tsvet = klahvid[taht].cget("bg")
    if tekushchiy_tsvet != "green": 
        klahvid[taht].config(bg=novy_tsvet)

def zavershit_igru(pobeda):
    global salajane_sona, praegune_katsetus
    if pobeda:
        soobshchenie = f"Pravilno! Ugadal slovo {salajane_sona} s {praegune_katsetus+1}-y popytki!"
        zapisat_rezultat(uspekh=True)
    else:
        soobshchenie = f"Igra okonchena! Pravilynoe slovo: {salajane_sona}"
        zapisat_rezultat(uspekh=False)
    
    sonumi_silt.config(text=soobshchenie)
    for klav in klahvid.values():
        klav.config(state=tk.DISABLED)
    kontroll_nupp.config(state=tk.DISABLED)

def zapisat_rezultat(uspekh):
    global salajane_sona, praegune_katsetus
    try:
        with open(tulemused_fail, "a", encoding="utf-8") as f:
            sostoyanie = "Uspekh" if uspekh else "Neudacha"
            f.write(f"{sostoyanie};{salajane_sona};{praegune_katsetus+1}\n")
    except Exception as e:
        messagebox.showerror("Oshibka", f"Ne udalos zapisat rezultaty: {str(e)}")
def novaya_igra():
    global salajane_sona, praegune_katsetus, praegused_tahed
    praegune_katsetus = 0
    praegused_tahed = []
    salajane_sona = vybrat_sona()
    for ryad in lauarakud:
        for rakk in ryad:
            rakk.config(text=" ", bg="white")
    
    for klav in klahvid.values():
        klav.config(bg="SystemButtonFace", state=tk.NORMAL)
    
    sonumi_silt.config(text="")
    kontroll_nupp.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Wordle Igra")
    
    sozdat_menyu(root)
    sozdat_polye(root)
    sozdat_klaviatuur(root)
    sozdat_sonumi_silt(root)
    
    novaya_igra()
    
    root.mainloop()
