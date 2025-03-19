import sqlite3
import tkinter as tk
from tkinter import ttk
import subprocess

def loo_andmebaas():
    try:
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        print("Ühendus andmebaasiga on edukalt loodud")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                director TEXT,
                release_year INTEGER,
                genre TEXT,
                duration INTEGER,
                rating REAL,
                language TEXT,
                country TEXT,
                description TEXT
            )
        ''')

        cursor.executemany('''
            INSERT OR IGNORE INTO movies (title, director, release_year, genre, duration, rating, language, country, description) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', [
            ('The From In With.', 'Francis Ford Coppola', 1994, 'Draama', 142, 9.3, 'Inglise', 'USA', 'The In With By On. A In From By The At. On A With By By On To A.'),
            ('The By On To.', 'Christopher Nolan', 2010, 'Ulme', 148, 8.8, 'Inglise', 'Ühendkuningriik', 'The A The On The In. By To A At On The. From The In With At In To A.'),
            ('In The With On.', 'Quentin Tarantino', 1972, 'Krimi', 175, 9.2, 'Inglise', 'USA', 'On From The By At The A. In From By With To On. A The By In With At On To A.'),
            ('The A To From.', 'Steven Spielberg', 1994, 'Seiklus', 154, 8.9, 'Inglise', 'Prantsusmaa', 'With By In The A On. The With To A At The From. On A From With At By The.'),
            ('On The From With.', 'Martin Scorsese', 2008, 'Action', 152, 9.0, 'Inglise', 'Saksamaa', 'The A By On In The. At With To A From On The. With On By The A In To From.'),
            ('From The By With.', 'Christopher Nolan', 1960, 'Draama', 134, 8.5, 'Inglise', 'Ühendkuningriik', 'The A On From The At. With To By In A The On. At The In From With By To A.'),
            ('The By On A.', 'Francis Ford Coppola', 1999, 'Põnevik', 112, 7.8, 'Inglise', 'USA', 'A The On By In The At. From With A On By To The. In The By With At A From.'),
            ('On A The From.', 'Quentin Tarantino', 2015, 'Komöödia', 126, 7.9, 'Inglise', 'Itaalia', 'By With A On In The From. The By At A With On To. At In The By From With A.'),
            ('By The On From.', 'Steven Spielberg', 1975, 'Action', 143, 8.7, 'Inglise', 'Prantsusmaa', 'A With On The By From In. The A At On With To From. By In The A From With At On.'),
            ('From With The By.', 'Martin Scorsese', 1980, 'Krimi', 163, 9.1, 'Inglise', 'Saksamaa', 'On The A By In The From. With By On A The In From. To The In At By With On A.')
        ])
        conn.commit()
        print("Tabel on loodud ja andmed on sisestatud")

    except sqlite3.Error as error:
        print("Viga andmebaasi loomisel või andmete sisestamisel:", error)
    finally:
        if conn:
            conn.close()
            print("Andmebaasi ühendus on suletud")
def load_data_from_db(tree, search_query=""):
    for item in tree.get_children():
        tree.delete(item)

    try:
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        if search_query:
            cursor.execute("SELECT title, director, release_year, genre, duration, rating, language, country, description FROM movies WHERE title LIKE ?", ('%' + search_query + '%',))
        else:
            cursor.execute("SELECT title, director, release_year, genre, duration, rating, language, country, description FROM movies")

        rows = cursor.fetchall()
        for row in rows:
            tree.insert("", "end", values=row)

    except sqlite3.Error as error:
        print("Viga andmete lugemisel:", error)
    finally:
        if conn:
            conn.close()
            print("Andmebaasi ühendus on suletud")
def add_data():
    try:
        subprocess.run(["python", "01.py"])
    except Exception as e:
        print("Viga andmete lisamise faili avamisel:", e)
def on_search():
    search_query = search_entry.get()
    load_data_from_db(tree, search_query)
if __name__ == "__main__":
    loo_andmebaas()
    root = tk.Tk()
    root.title("Filmid")
    search_frame = tk.Frame(root)
    search_frame.pack(pady=10)

    search_label = tk.Label(search_frame, text="Otsi filmi pealkirja järgi:")
    search_label.pack(side=tk.LEFT)

    search_entry = tk.Entry(search_frame)
    search_entry.pack(side=tk.LEFT, padx=10)

    search_button = tk.Button(search_frame, text="Otsi", command=on_search)
    search_button.pack(side=tk.LEFT)
    frame = tk.Frame(root)
    frame.pack(pady=20, fill=tk.BOTH, expand=True)
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set, columns=("title", "director", "year", "genre", "duration", "rating", "language", "country", "description"), show="headings")
    tree.pack(fill=tk.BOTH, expand=True)
    scrollbar.config(command=tree.yview)
    tree.heading("title", text="Pealkiri")
    tree.heading("director", text="Režissöör")
    tree.heading("year", text="Aasta")
    tree.heading("genre", text="Žanr")
    tree.heading("duration", text="Kestus")
    tree.heading("rating", text="Reiting")
    tree.heading("language", text="Keel")
    tree.heading("country", text="Riik")
    tree.heading("description", text="Kirjeldus")

    tree.column("title", width=150)
    tree.column("director", width=100)
    tree.column("year", width=60)
    tree.column("genre", width=100)
    tree.column("duration", width=60)
    tree.column("rating", width=60)
    tree.column("language", width=80)
    tree.column("country", width=80)
    tree.column("description", width=200)
    load_data_from_db(tree)
    open_button = tk.Button(root, text="Lisa andmeid", command=add_data)
    open_button.pack(pady=20)

    root.mainloop()
