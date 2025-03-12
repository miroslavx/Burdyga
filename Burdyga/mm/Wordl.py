

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

valja_raam = None
lauarakud = []
klahvid = {}
kontroll_nupp = None
sonumi_silt = None

def loe_sonad_failist():
    try:
        with open(sonad_fail, "r", encoding="utf-8") as f:
            return [sona.strip().upper() for sona in f if len(sona.strip()) == TAHTE_ARV]
    except FileNotFoundError:
        messagebox.showerror("Viga", f"Faili {sonad_fail} ei leitud!")
        return []

def vali_sona():
    sonad = loe_sonad_failist()
    if not sonad:
        messagebox.showerror("Viga", "Sõnade fail on tühi või vigane!")
        return None
    return random.choice(sonad)

def loo_valjak(root):
    global valja_raam, lauarakud
    valja_raam = tk.Frame(root, bg="black")
    valja_raam.pack(pady=20)
   
    lauarakud = []
    for rida in range(KATSEID):
        rea_rakud = []
        for veerg in range(TAHTE_ARV):
            rakk = tk.Label(valja_raam,
                           text=" ",
                           font=("Courier New", 28, "bold"),
                           width=3,
                           relief="sunken",
                           bg="black",
                           fg="#00FF00",
                           bd=8,
                           padx=8,
                           pady=8)
            rakk.grid(row=rida, column=veerg, padx=4, pady=4)
            rea_rakud.append(rakk)
        lauarakud.append(rea_rakud)

def loo_klaviatuur(root):
    global klahvid, kontroll_nupp
    klaviatuuri_raam = tk.Frame(root, bg="black")
    klaviatuuri_raam.pack(pady=15)
   
    klaviatuuri_read = [
        ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "Õ"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", "Ü", "Ö", "Ä"],
        ["Z", "X", "C", "V", "B", "N", "M"]
    ]
   
    klahvid = {}
    for rida in klaviatuuri_read:
        rea_raam = tk.Frame(klaviatuuri_raam, bg="black")
        rea_raam.pack()
        for taht in rida:
            nupp = tk.Button(rea_raam,
                            text=taht,
                            font=("Courier New", 16, "bold"),
                            width=4,
                            relief="ridge",
                            bg="#0A0A0A",
                            fg="#00FF00",
                            activebackground="#002200",
                            activeforeground="#00FF00",
                            bd=6,
                            command=lambda t=taht: lisa_taht(t))
            nupp.pack(side=tk.LEFT, padx=2, pady=2)
            klahvid[taht] = nupp

    spets_raam = tk.Frame(klaviatuuri_raam, bg="black")
    spets_raam.pack(pady=10)
   
    tk.Button(spets_raam,
             text="← Tagasi",
             font=("Courier New", 14, "bold"),
             width=8,
             bg="#0A0A0A",
             fg="#00FF00",
             relief="ridge",
             bd=6,
             command=tagasi).pack(side=tk.LEFT, padx=8)
   
    kontroll_nupp = tk.Button(spets_raam,
                            text="KONTROLL",
                            font=("Courier New", 14, "bold"),
                            width=12,
                            bg="#0A0A0A",
                            fg="#FFFF00",
                            relief="ridge",
                            bd=6,
                            command=kontrolli)
    kontroll_nupp.pack(side=tk.LEFT, padx=8)
    kontroll_nupp.config(state=tk.DISABLED)

def loo_sonumi_silt(root):
    global sonumi_silt
    sonumi_silt = tk.Label(root,
                          text="",
                          font=("Courier New", 16, "bold"),
                          fg="#00FF00",
                          bg="black")
    sonumi_silt.pack(pady=15)

def lisa_taht(taht):
    global praegused_tahed, praegune_katsetus
    if len(praegused_tahed) < TAHTE_ARV and praegune_katsetus < KATSEID:
        praegused_tahed.append(taht)
        positsioon = len(praegused_tahed) - 1
        lauarakud[praegune_katsetus][positsioon].config(text=taht)
        kontroll_nupp.config(state=tk.NORMAL if len(praegused_tahed) == TAHTE_ARV else tk.DISABLED)

def tagasi():
    global praegused_tahed, praegune_katsetus
    if praegused_tahed:
        positsioon = len(praegused_tahed) - 1
        lauarakud[praegune_katsetus][positsioon].config(text=" ")
        praegused_tahed.pop()
        kontroll_nupp.config(state=tk.NORMAL if len(praegused_tahed) == TAHTE_ARV else tk.DISABLED)

def kontrolli():
    global praegused_tahed, praegune_katsetus, salajane_sona
    pakkumine = "".join(praegused_tahed)
    varvid = kontrolli_katset(pakkumine)
   
    for i, varv in enumerate(varvid):
        lauarakud[praegune_katsetus][i].config(bg=varv)
        taht = pakkumine[i]
        if taht in klahvid:
            uuenda_klahvi_varvi(taht, varv)
 
    if pakkumine == salajane_sona:
        lopeta_mang(voitis=True)
    elif praegune_katsetus == KATSEID - 1:
        lopeta_mang(voitis=False)
    else:
        praegune_katsetus += 1
        praegused_tahed = []
        kontroll_nupp.config(state=tk.DISABLED)

def kontrolli_katset(pakkumine):
    global salajane_sona
    varvid = ["#0A0A0A"] * TAHTE_ARV
    temp_sona = list(salajane_sona)
    for i in range(TAHTE_ARV):
        if pakkumine[i] == temp_sona[i]:
            varvid[i] = "#006600"
            temp_sona[i] = None
    for i in range(TAHTE_ARV):
        if varvid[i] != "#006600" and pakkumine[i] in temp_sona:
            varvid[i] = "#666600"
            temp_sona.remove(pakkumine[i])
    return varvid

def uuenda_klahvi_varvi(taht, uus_varv):
    praegune_varv = klahvid[taht].cget("bg")
    if praegune_varv != "#006600":
        klahvid[taht].config(bg=uus_varv)

def lopeta_mang(voitis):
    global salajane_sona, praegune_katsetus
    if voitis:
        teade = f"ÕIGE! {praegune_katsetus+1}. KATSEL!"
    else:
        teade = f"MÄNG LÄBI! ÕIGE SÕNA: {salajane_sona}"
   
    sonumi_silt.config(text=teade)
    for klahv in klahvid.values():
        klahv.config(state=tk.DISABLED)
    kontroll_nupp.config(state=tk.DISABLED)
    salvesta_tulemus(voitis)

def salvesta_tulemus(edukus):
    global salajane_sona, praegune_katsetus
    try:
        with open(tulemused_fail, "a", encoding="utf-8") as f:
            olek = "EDU" if edukus else "EBAEDU"
            f.write(f"{olek};{salajane_sona};{praegune_katsetus+1}\n")
    except Exception as e:
        messagebox.showerror("Viga", f"Salvestamine ebaõnnestus: {str(e)}")

def uus_mang():
    global salajane_sona, praegune_katsetus, praegused_tahed
    praegune_katsetus = 0
    praegused_tahed = []
    salajane_sona = vali_sona()
    for rida in lauarakud:
        for rakk in rida:
            rakk.config(text=" ", bg="black")
   
    for klahv in klahvid.values():
        klahv.config(bg="#0A0A0A", state=tk.NORMAL)
   
    sonumi_silt.config(text="")
    kontroll_nupp.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("WORDLE - RETRO")
    root.configure(bg="black")
   
    loo_valjak(root)
    loo_klaviatuur(root)
    loo_sonumi_silt(root)
   
    uus_mang()
   
    root.mainloop()


