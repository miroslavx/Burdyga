import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

class Andmebaas:
    def __init__(self, db_name='andmebaas.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.loo_tabelid()
        
    def loo_tabelid(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Kategooriad (
                kategooria_id INTEGER PRIMARY KEY AUTOINCREMENT,
                kategooria_nimi TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Brandid (
                brandi_id INTEGER PRIMARY KEY AUTOINCREMENT,
                brandi_nimi TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Tooted (
                toote_id INTEGER PRIMARY KEY AUTOINCREMENT,
                toote_nimi TEXT NOT NULL,
                hind REAL NOT NULL,
                kategooria_id INTEGER,
                brandi_id INTEGER,
                FOREIGN KEY (kategooria_id) REFERENCES Kategooriad(kategooria_id),
                FOREIGN KEY (brandi_id) REFERENCES Brandid(brandi_id)
            )
        ''')
        self.conn.commit()
    
    def lisa_kategooria(self, nimi):
        self.cursor.execute('INSERT INTO Kategooriad (kategooria_nimi) VALUES (?)', (nimi,))
        self.conn.commit()
    
    def lisa_brand(self, nimi):
        self.cursor.execute('INSERT INTO Brandid (brandi_nimi) VALUES (?)', (nimi,))
        self.conn.commit()
    
    def lisa_toode(self, nimi, hind, kategooria_id, brandi_id):
        self.cursor.execute('''
            INSERT INTO Tooted (toote_nimi, hind, kategooria_id, brandi_id)
            VALUES (?, ?, ?, ?)
        ''', (nimi, hind, kategooria_id, brandi_id))
        self.conn.commit()
    
    def koik_tooted(self):
        self.cursor.execute('''
            SELECT t.toote_nimi, t.hind, k.kategooria_nimi, b.brandi_nimi 
            FROM Tooted t
            JOIN Kategooriad k ON t.kategooria_id = k.kategooria_id
            JOIN Brandid b ON t.brandi_id = b.brandi_id
        ''')
        return self.cursor.fetchall()
    
    def tooted_kategooria_jargi(self, kategooria_id):
        self.cursor.execute('''
            SELECT t.toote_nimi, t.hind, b.brandi_nimi 
            FROM Tooted t
            JOIN Brandid b ON t.brandi_id = b.brandi_id
            WHERE t.kategooria_id = ?
        ''', (kategooria_id,))
        return self.cursor.fetchall()
    
    def tooted_brandi_jargi(self, brandi_id):
        self.cursor.execute('''
            SELECT t.toote_nimi, t.hind, k.kategooria_nimi 
            FROM Tooted t
            JOIN Kategooriad k ON t.kategooria_id = k.kategooria_id
            WHERE t.brandi_id = ?
        ''', (brandi_id,))
        return self.cursor.fetchall()
    
    def uuenda_toote_hinda(self, toote_id, uus_hind):
        self.cursor.execute('''
            UPDATE Tooted SET hind = ? WHERE toote_id = ?
        ''', (uus_hind, toote_id))
        self.conn.commit()
    
    def uuenda_kategooria_nime(self, kategooria_id, uus_nimi):
        self.cursor.execute('''
            UPDATE Kategooriad SET kategooria_nimi = ? WHERE kategooria_id = ?
        ''', (uus_nimi, kategooria_id))
        self.conn.commit()
    
    def kustuta_tooted_kategooria_jargi(self, kategooria_id):
        self.cursor.execute('DELETE FROM Tooted WHERE kategooria_id = ?', (kategooria_id,))
        self.conn.commit()
    
    def kustuta_tooted_brandi_jargi(self, brandi_id):
        self.cursor.execute('DELETE FROM Tooted WHERE brandi_id = ?', (brandi_id,))
        self.conn.commit()
    
    def kustuta_tabel(self, tabeli_nimi):
        self.cursor.execute(f'DROP TABLE IF EXISTS {tabeli_nimi}')
        self.conn.commit()
    
    def koik_kategooriad(self):
        self.cursor.execute('SELECT * FROM Kategooriad')
        return self.cursor.fetchall()
    
    def koik_brandid(self):
        self.cursor.execute('SELECT * FROM Brandid')
        return self.cursor.fetchall()
    
    def sulge(self):
        self.conn.close()

class Rakendus(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Toodete haldamine")
        self.db = Andmebaas()
        
        self.loo_nupud()
        self.uuenda_nimekirju()
        
    def loo_nupud(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(padx=10, pady=10, expand=True, fill='both')
        
        self.vaatamise_leht = ttk.Frame(self.notebook)
        self.notebook.add(self.vaatamise_leht, text="Vaata")
        self.loo_vaatamise_leht()
        
        self.lisamise_leht = ttk.Frame(self.notebook)
        self.notebook.add(self.lisamise_leht, text="Lisa")
        self.loo_lisamise_leht()
        
        self.haldamise_leht = ttk.Frame(self.notebook)
        self.notebook.add(self.haldamise_leht, text="Halda")
        self.loo_haldamise_leht()
    
    def loo_vaatamise_leht(self):
        veerud = ('nimi', 'hind', 'kategooria', 'brand')
        self.tree = ttk.Treeview(self.vaatamise_leht, columns=veerud, show='headings')
        self.tree.heading('nimi', text='Nimi')
        self.tree.heading('hind', text='Hind')
        self.tree.heading('kategooria', text='Kategooria')
        self.tree.heading('brand', text='Brand')
        self.tree.pack(fill='both', expand=True)
        
        self.uuenda_tooteid()
    
    def loo_lisamise_leht(self):
        ttk.Label(self.lisamise_leht, text="Toote nimi:").grid(row=0, column=0, padx=5, pady=5)
        self.toote_nimi = ttk.Entry(self.lisamise_leht)
        self.toote_nimi.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.lisamise_leht, text="Hind:").grid(row=1, column=0, padx=5, pady=5)
        self.toote_hind = ttk.Entry(self.lisamise_leht)
        self.toote_hind.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(self.lisamise_leht, text="Kategooria:").grid(row=2, column=0, padx=5, pady=5)
        self.kategooria_combo = ttk.Combobox(self.lisamise_leht, state='readonly')
        self.kategooria_combo.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(self.lisamise_leht, text="Brand:").grid(row=3, column=0, padx=5, pady=5)
        self.brand_combo = ttk.Combobox(self.lisamise_leht, state='readonly')
        self.brand_combo.grid(row=3, column=1, padx=5, pady=5)
        
        ttk.Button(self.lisamise_leht, text="Lisa toode", command=self.lisa_toode).grid(row=4, column=0, columnspan=2, pady=5)
        
        ttk.Label(self.lisamise_leht, text="Uus kategooria:").grid(row=5, column=0, padx=5, pady=5)
        self.uus_kategooria = ttk.Entry(self.lisamise_leht)
        self.uus_kategooria.grid(row=5, column=1, padx=5, pady=5)
        ttk.Button(self.lisamise_leht, text="Lisa kategooria", command=self.lisa_kategooria).grid(row=6, column=0, columnspan=2, pady=5)
        
        ttk.Label(self.lisamise_leht, text="Uus brand:").grid(row=7, column=0, padx=5, pady=5)
        self.uus_brand = ttk.Entry(self.lisamise_leht)
        self.uus_brand.grid(row=7, column=1, padx=5, pady=5)
        ttk.Button(self.lisamise_leht, text="Lisa brand", command=self.lisa_brand).grid(row=8, column=0, columnspan=2, pady=5)
    
    def loo_haldamise_leht(self):
        ttk.Button(self.haldamise_leht, text="Kustuta toodete tabel", 
                  command=lambda: self.db.kustuta_tabel('Tooted')).pack(pady=5)
        ttk.Button(self.haldamise_leht, text="Taasta tabelid", 
                  command=self.db.loo_tabelid).pack(pady=5)
    
    def uuenda_nimekirju(self):
        kategooriad = [kat[1] for kat in self.db.koik_kategooriad()]
        self.kategooria_combo['values'] = kategooriad
        brandid = [brand[1] for brand in self.db.koik_brandid()]
        self.brand_combo['values'] = brandid
    
    def uuenda_tooteid(self):
        for rida in self.tree.get_children():
            self.tree.delete(rida)
        for toode in self.db.koik_tooted():
            self.tree.insert('', 'end', values=toode)
    
    def lisa_toode(self):
        nimi = self.toote_nimi.get()
        hind = self.toote_hind.get()
        kategooria = self.kategooria_combo.current() + 1
        brand = self.brand_combo.current() + 1
        
        if nimi and hind and kategooria and brand:
            try:
                self.db.lisa_toode(nimi, float(hind), kategooria, brand)
                self.uuenda_tooteid()
                self.uuenda_nimekirju()
                messagebox.showinfo("Onnestus", "Toode lisatud")
            except:
                messagebox.showerror("Viga", "Kontrolli sisestatud andmeid")
        else:
            messagebox.showerror("Viga", "Taida koik väljad")
    
    def lisa_kategooria(self):
        nimi = self.uus_kategooria.get()
        if nimi:
            self.db.lisa_kategooria(nimi)
            self.uuenda_nimekirju()
            messagebox.showinfo("Onnestus", "Kategooria lisatud")
        else:
            messagebox.showerror("Viga", "Sisesta kategooria nimi")
    
    def lisa_brand(self):
        nimi = self.uus_brand.get()
        if nimi:
            self.db.lisa_brand(nimi)
            self.uuenda_nimekirju()
            messagebox.showinfo("Onnestus", "Brand lisatud")
        else:
            messagebox.showerror("Viga", "Sisesta brandi nimi")
    
    def __del__(self):
        self.db.sulge()

if __name__ == "__main__":
    rakendus = Rakendus()
    rakendus.mainloop()
