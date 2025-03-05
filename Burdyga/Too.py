import tkinter as tk
import random

words = [
    "TERAS", "KLAAR", "LINNA", "ROHUS",
    "SUVIS", "TALVE", "METSA", "KALLE",
    "PÄIKE", "ÕUN", "TÜHI", "KÜLIM",
    "MÄGI", "JÕGI", "NÄIDE"
]

MAX_ATTEMPTS = 6
WORD_LENGTH = 5

class WordleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle")
        
        self.secret_word = random.choice(words).upper()
        self.attempts = []
        self.current_attempt = 0
        
        self.create_grid()
        self.create_input()
        self.create_keyboard()
        self.create_message_label()
    
    def create_grid(self):
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(pady=10)
        
        self.cells = []
        for row in range(MAX_ATTEMPTS):
            row_cells = []
            for col in range(WORD_LENGTH):
                cell = tk.Label(self.grid_frame, 
                               text=" ", 
                               font=("Arial", 24), 
                               width=2, 
                               relief="solid",
                               bg="white")
                cell.grid(row=row, column=col, padx=5, pady=5)
                row_cells.append(cell)
            self.cells.append(row_cells)
    
    def create_input(self):
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)
        
        self.entry = tk.Entry(input_frame, 
                            font=("Arial", 24), 
                            width=6,
                            justify="center")
        self.entry.pack(side=tk.LEFT, padx=5)
        self.entry.bind("<Return>", lambda event: self.check_guess())
        
        self.button = tk.Button(input_frame, 
                              text="Kontrolli", 
                              command=self.check_guess)
        self.button.pack(side=tk.LEFT, padx=5)
    
    def create_keyboard(self):
        keyboard_frame = tk.Frame(self.root)
        keyboard_frame.pack(pady=10)
        
        self.keyboard = {}
        rows = ["QWERTYUIÕ", "ASDFGHJKÄ", "ZXCVBNMÖÜ"]
        
        for row in rows:
            row_frame = tk.Frame(keyboard_frame)
            row_frame.pack()
            for char in row:
                btn = tk.Label(row_frame, 
                             text=char, 
                             font=("Arial", 12), 
                             width=2, 
                             relief="raised",
                             bg="white")
                btn.pack(side=tk.LEFT, padx=2, pady=2)
                self.keyboard[char] = btn
    
    def create_message_label(self):
        self.message_label = tk.Label(self.root, 
                                    text="", 
                                    font=("Arial", 14),
                                    fg="red")
        self.message_label.pack(pady=10)
    
    def check_guess(self):
        guess = self.entry.get().upper()
        
        if len(guess) != WORD_LENGTH:
            self.show_message(f"Sisesta {WORD_LENGTH}-täheline sõna!")
            return
        
        self.attempts.append(guess)
        self.update_grid()
        self.update_keyboard(guess)
        
        if guess == self.secret_word:
            self.show_message("Arvasid sõna ära! Palju õnne!")
            self.disable_input()
        elif self.current_attempt >= MAX_ATTEMPTS - 1:
            self.show_message(f"Mäng läbi! Sõna oli: {self.secret_word}")
            self.disable_input()
        else:
            self.current_attempt += 1
        
        self.entry.delete(0, tk.END)
    
    def update_grid(self):
        guess = self.attempts[-1]
        colors = self.get_colors(guess)
        
        for col in range(WORD_LENGTH):
            self.cells[self.current_attempt][col].config(
                text=guess[col],
                bg=colors[col]
            )
    
    def get_colors(self, guess):
        colors = ["gray"] * WORD_LENGTH
        secret = list(self.secret_word)
        guess_list = list(guess)
        
        for i in range(WORD_LENGTH):
            if guess_list[i] == secret[i]:
                colors[i] = "green"
                secret[i] = None
                guess_list[i] = None
        
        for i in range(WORD_LENGTH):
            if guess_list[i] is not None and guess_list[i] in secret:
                colors[i] = "yellow"
                secret.remove(guess_list[i])
        
        return colors
    
    def update_keyboard(self, guess):
        colors = self.get_colors(guess)
        used_letters = set(guess)
        
        for letter in used_letters:
            if letter in self.keyboard:
                current_color = self.keyboard[letter].cget("bg")
                new_color = self.get_letter_color(letter, colors, guess)
                
                if current_color != "green":
                    self.keyboard[letter].config(bg=new_color)
    
    def get_letter_color(self, letter, colors, guess):
        best_color = "gray"
        for i in range(WORD_LENGTH):
            if guess[i] == letter:
                if colors[i] == "green":
                    return "green"
                elif colors[i] == "yellow":
                    best_color = "yellow"
        return best_color
    
    def show_message(self, message):
        self.message_label.config(text=message)
    
    def disable_input(self):
        self.entry.config(state=tk.DISABLED)
        self.button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = WordleGame(root)
    root.mainloop()
