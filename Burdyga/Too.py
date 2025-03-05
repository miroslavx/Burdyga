import tkinter as tk
import random
words = [
    "TERAS", "KLAAR", "LINNA", "ROHUS",
    "SUVIS", "TALVE", "METSA", "KALLE",
    "PÄIKE", "ÕUN", "TÜHI", "KÜLIM",
    "MÄGI", "JÕGI", "NÄIDE"
]
MAX_KATSEID = 6  
SÕNA_PIKKUS = 5  
juur = None  
salajane_sõna = None  
katseid = []  
praegune_katse = 0 
lahtrid = []  
sisend = None  
nupp = None
klaviatuur = {}
teade_silt = None  

def initsialiseeri_mäng(juur_param):
    global juur, salajane_sõna, katseid, praegune_katse
    juur = juur_param
    juur.title("Wordle")
    
    salajane_sõna = random.choice(words).upper()
    katseid = []
    praegune_katse = 0
    
    loo_võre()
    loo_sisend()
    loo_klaviatuur()
    loo_teade_silt()
    
def loo_võre():
    global lahtrid
    võre_raam = tk.Frame(juur)
    võre_raam.pack(pady=10)
    
    lahtrid = []
    for rida in range(MAX_KATSEID):
        rea_lahtrid = []
        for veerg in range(SÕNA_PIKKUS):
            laht = tk.Label(võre_raam, 
                           text=" ", 
                           font=("Arial", 24), 
                           width=2, 
                           relief="solid",
                           bg="white")
            laht.grid(row=rida, column=veerg, padx=5, pady=5)
            rea_lahtrid.append(laht)
        lahtrid.append(rea_lahtrid)
def loo_sisend():
    global sisend, nupp
    sisend_raam = tk.Frame(juur)
    sisend_raam.pack(pady=10)
    
    sisend = tk.Entry(sisend_raam, 
                    font=("Arial", 24), 
                    width=6,
                    justify="center")
    sisend.pack(side=tk.LEFT, padx=5)
    sisend.bind("<Return>", lambda event: kontrolli_arvamust())
    
    nupp = tk.Button(sisend_raam, 
                      text="Kontrolli", 
                      command=kontrolli_arvamust)
    nupp.pack(side=tk.LEFT, padx=5)

def loo_klaviatuur():
    global klaviatuur
    klaviatuur_raam = tk.Frame(juur)
klaviatuur_raam.pack(pady=10)
    
    klaviatuur = {}
    read = ["QWERTYUIÕ", "ASDFGHJKÄ", "ZXCVBNMÖÜ"]
    
    for rida in read:
        rea_raam = tk.Frame(klaviatuur_raam)
        rea_raam.pack()
        for täht in rida:
            nupp = tk.Label(rea_raam, 
                         text=täht, 
                         font=("Arial", 12), 
                         width=2, 
                        relief="raised",
                         bg="white")
        nupp.pack(side=tk.LEFT, padx=2, pady=2)
            klaviatuur[täht] = nupp

def loo_teade_silt():
    global teade_silt
    teade_silt = tk.Label(juur, 
            text="", 
             font=("Arial", 14),
                 fg="red")
    teade_silt.pack(pady=10)

def kontrolli_arvamust():
    global praegune_katse
    arvamus = sisend.get().upper()
    
    if len(arvamus) != SÕNA_PIKKUS:
        näita_teadet(f"Sisesta {SÕNA_PIKKUS}-täheline sõna!")
        return
    katseid.append(arvamus)
    uuenda_võre()
    uuenda_klaviatuuri(arvamus)
    
    if arvamus == salajane_sõna:
        näita_teadet("Arvasid sõna ära! Palju õnne!")
        keelata_sisend()
    elif praegune_katse >= MAX_KATSEID - 1:
        näita_teadet(f"Mäng läbi! Sõna oli: {salajane_sõna}")
        keelata_sisend()
    else:
        praegune_katse += 1
    
    sisend.delete(0, tk.END)
def uuenda_võre():
    arvamus = katseid[-1]
    värvid = saa_värvid(arvamus)
    
    for veerg in range(SÕNA_PIKKUS):
        lahtrid[praegune_katse][veerg].config(
            text=arvamus[veerg],
            bg=värvid[veerg])

def saa_värvid(arvamus):
    värvid = ["gray"] * SÕNA_PIKKUS
    salajane = list(salajane_sõna)
    arvamus_list = list(arvamus)
    for i in range(SÕNA_PIKKUS):
        if arvamus_list[i] == salajane[i]:
            värvid[i] = "green"
            salajane[i] = None
            arvamus_list[i] = None
    
    for i in range(SÕNA_PIKKUS):
        if arvamus_list[i] is not None and arvamus_list[i] in salajane:
            värvid[i] = "yellow"
            salajane.remove(arvamus_list[i])   
    return värvid
    
def uuenda_klaviatuuri(arvamus):
    värvid = saa_värvid(arvamus)
    kasutatud_tähed = set(arvamus)
    
    for täht in kasutatud_tähed:
        if täht in klaviatuur:
            praegune_värv = klaviatuur[täht].cget("bg")
            uus_värv = saa_tähe_värv(täht, värvid, arvamus)
            
            if praegune_värv != "green":
                klaviatuur[täht].config(bg=uus_värv)
def saa_tähe_värv(täht, värvid, arvamus):
    parim_värv = "gray"
    for i in range(SÕNA_PIKKUS):
        if arvamus[i] == täht:
            if värvid[i] == "green":
                return "green"
            elif värvid[i] == "yellow":
                parim_värv = "yellow"
    return parim_värv
    
def näita_teadet(teade):
    teade_silt.config(text=teade)

def keelata_sisend():
    sisend.config(state=tk.DISABLED)
    nupp.config(state=tk.DISABLED)
if __name__ == "__main__":
    juur = tk.Tk()
    initsialiseeri_mäng(juur)
    juur.mainloop()
