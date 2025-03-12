import sqlite3
from sqlite3 import Error
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

def create_connection(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print("Ühendus andmebaasiga loodud")
        return conn
    except Error as e:
        print(f"Viga '{e}'")
    return conn

def create_tables(conn):
    create_autorid_table = """
    CREATE TABLE IF NOT EXISTS Autorid (
        autor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        autor_nimi TEXT NOT NULL,
        sünnikuupäev DATE
    );
    """
    
    create_zanrid_table = """
    CREATE TABLE IF NOT EXISTS Žanrid (
        žanr_id INTEGER PRIMARY KEY AUTOINCREMENT,
        žanri_nimi TEXT NOT NULL UNIQUE
    );
    """
    
    create_raamatud_table = """
    CREATE TABLE IF NOT EXISTS Raamatud (
        raamat_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pealkiri TEXT NOT NULL,
        väljaandmise_kuupäev DATE,
        autor_id INTEGER,
        žanr_id INTEGER,
        FOREIGN KEY (autor_id) REFERENCES Autorid (autor_id),
        FOREIGN KEY (žanr_id) REFERENCES Žanrid (žanr_id)
    );
    """
    
    try:
        c = conn.cursor()
        c.execute(create_autorid_table)
        c.execute(create_zanrid_table)
        c.execute(create_raamatud_table)
        conn.commit()
    except Error as e:
        print(f"Viga tabelite loomisel: {e}")

def insert_autor(conn, autor_nimi, sünnikuupäev):
    sql = '''INSERT INTO Autorid(autor_nimi, sünnikuupäev)
             VALUES(?,?)'''
    try:
        c = conn.cursor()
        c.execute(sql, (autor_nimi, sünnikuupäev))
        conn.commit()
        return c.lastrowid
    except Error as e:
        print(f"Viga autori lisamisel: {e}")

def insert_zanr(conn, žanri_nimi):
    sql = '''INSERT INTO Žanrid(žanri_nimi)
             VALUES(?)'''
    try:
        c = conn.cursor()
        c.execute(sql, (žanri_nimi,))
        conn.commit()
        return c.lastrowid
    except Error as e:
        print(f"Viga žanri lisamisel: {e}")

def insert_raamat(conn, pealkiri, väljaandmise_kuupäev, autor_id, žanr_id):
    sql = '''INSERT INTO Raamatud(pealkiri, väljaandmise_kuupäev, autor_id, žanr_id)
             VALUES(?,?,?,?)'''
    try:
        c = conn.cursor()
        c.execute(sql, (pealkiri, väljaandmise_kuupäev, autor_id, žanr_id))
        conn.commit()
        return c.lastrowid
    except Error as e:
        print(f"Viga raamatu lisamisel: {e}")

def get_all_raamatud(conn):
    sql = '''SELECT Raamatud.*, Autorid.autor_nimi, Žanrid.žanri_nimi 
             FROM Raamatud
             LEFT JOIN Autorid ON Raamatud.autor_id = Autorid.autor_id
             LEFT JOIN Žanrid ON Raamatud.žanr_id = Žanrid.žanr_id'''
    try:
        c = conn.cursor()
        c.execute(sql)
        return c.fetchall()
    except Error as e:
        print(f"Viga raamatute laadimisel: {e}")

def update_raamat(conn, raamat_id, pealkiri, kuupäev, autor_id, žanr_id):
    sql = '''UPDATE Raamatud
             SET pealkiri = ?,
                 väljaandmise_kuupäev = ?,
                 autor_id = ?,
                 žanr_id = ?
             WHERE raamat_id = ?'''
    try:
        c = conn.cursor()
        c.execute(sql, (pealkiri, kuupäev, autor_id, žanr_id, raamat_id))
        conn.commit()
    except Error as e:
        print(f"Viga raamatu uuendamisel: {e}")

def delete_raamatud(conn, condition):
    sql = f"DELETE FROM Raamatud WHERE {condition}"
    try:
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
    except Error as e:
        print(f"Viga raamatute kustutamisel: {e}")

def drop_table(conn, table_name):
    sql = f"DROP TABLE IF EXISTS {table_name}"
    try:
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
    except Error as e:
        print(f"Viga tabeli {table_name} kustutamisel: {e}")
class BookApp(tk.Tk):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        self.title("Raamatukataloog")
        self.geometry("800x600")
        
        self.create_widgets()
        self.load_data()
        
    def create_widgets(self):
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self.books_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.books_frame, text="Raamatud")
        self.books_tree = ttk.Treeview(self.books_frame, columns=('ID', 'Pealkiri', 'Kuupäev', 'Autor', 'Žanr'), show='headings')
        self.books_tree.heading('ID', text='ID')
        self.books_tree.heading('Pealkiri', text='Pealkiri')
        self.books_tree.heading('Kuupäev', text='Väljaandmise kuupäev')
        self.books_tree.heading('Autor', text='Autor')
        self.books_tree.heading('Žanr', text='Žanr')
        self.books_tree.pack(fill=tk.BOTH, expand=True)
        add_frame = ttk.Frame(self.books_frame)
        add_frame.pack(pady=10)
        
        ttk.Label(add_frame, text="Pealkiri:").grid(row=0, column=0)
        self.title_entry = ttk.Entry(add_frame)
        self.title_entry.grid(row=0, column=1)
        
        ttk.Label(add_frame, text="Kuupäev (YYYY-MM-DD):").grid(row=1, column=0)
        self.date_entry = ttk.Entry(add_frame)
        self.date_entry.grid(row=1, column=1)
        
        ttk.Label(add_frame, text="Autor ID:").grid(row=2, column=0)
        self.author_entry = ttk.Entry(add_frame)
        self.author_entry.grid(row=2, column=1)
        
        ttk.Label(add_frame, text="Žanr ID:").grid(row=3, column=0)
        self.genre_entry = ttk.Entry(add_frame)
        self.genre_entry.grid(row=3, column=1)
        
        ttk.Button(add_frame, text="Lisa uus raamat", command=self.add_book).grid(row=4, columnspan=2)
        
    def load_data(self):
        for item in self.books_tree.get_children():
            self.books_tree.delete(item)
        books = get_all_raamatud(self.conn)
        for book in books:
            self.books_tree.insert('', 'end', values=book)
    
    def add_book(self):
        pealkiri = self.title_entry.get()
        kuupäev = self.date_entry.get()
        autor_id = self.author_entry.get()
        žanr_id = self.genre_entry.get()
        
        if not pealkiri or not kuupäev or not autor_id or not žanr_id:
            messagebox.showerror("Viga", "Kõik väljad peavad olema täidetud")
            return
            
        try:
            insert_raamat(self.conn, pealkiri, kuupäev, autor_id, žanr_id)
            self.load_data()
            messagebox.showinfo("Edukas", "Raamat lisatud edukalt")
        except Error as e:
            messagebox.showerror("Viga", f"Viga raamatu lisamisel: {e}")

if __name__ == "__main__":

    conn = create_connection("raamatud.db")
    if conn is not None:
        create_tables(conn)
        try:

            insert_autor(conn, "J.K. Rowling", "1965-07-31")
            insert_autor(conn, "George Orwell", "1903-06-25")
            insert_zanr(conn, "Fantaasia")
            insert_zanr(conn, "Düstoopia")
            insert_raamat(conn, "Harry Potter", "1997-06-26", 1, 1)
            insert_raamat(conn, "1984", "1949-06-08", 2, 2)
        except Error as e:
            print(f"Viga näidisandmete lisamisel: {e}")
        app = BookApp(conn)
        app.mainloop()
        
        conn.close()
    else:
        print("Andmebaasiühenduse loomine ebaõnnestus")
