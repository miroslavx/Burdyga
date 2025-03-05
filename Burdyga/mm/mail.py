import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from email.message import EmailMessage
import ssl
import smtplib
import imghdr

class EmailApp:
    def __init__(self, root):
        self.root = root
        self.root.title("E-kirja saatmine")
        self.root.geometry("600x500")
        self.root.configure(bg='#e8f5e9')
        self.file = None
        
        self.main_frame = tk.Frame(root, bg='#e8f5e9')
        self.main_frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        self.create_label_entry("EMAIL:", 0)
        self.create_label_entry("TEEMA:", 1)
        self.create_attachment_section()
        self.create_message_body()
        self.create_buttons()

    def create_label_entry(self, text, row):
        label = tk.Label(self.main_frame, text=text, bg='#2e7d32', fg='white', 
                        font=('Arial', 12, 'bold'), width=10)
        label.grid(row=row, column=0, padx=5, pady=5, sticky='w')
        
        entry = tk.Entry(self.main_frame, font=('Arial', 11), width=50)
        entry.grid(row=row, column=1, columnspan=2, padx=5, pady=5, sticky='w')
        
        if text == "EMAIL:":
            self.email_box = entry
        elif text == "TEEMA:":
            self.teema_box = entry

    def create_attachment_section(self):
        attach_label = tk.Label(self.main_frame, text="LISA:", bg='#2e7d32', 
                              fg='white', font=('Arial', 12, 'bold'), width=10)
        attach_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        
        self.l_lisatud = tk.Label(self.main_frame, text="", bg='#e8f5e9', 
                                 font=('Arial', 10), wraplength=350)
        self.l_lisatud.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        
        attach_btn = tk.Button(self.main_frame, text="LISA PILT", 
                             command=self.vali_pilt, bg='#2e7d32', fg='white',
                             font=('Arial', 10, 'bold'))
        attach_btn.grid(row=2, column=2, padx=5, pady=5, sticky='e')

    def create_message_body(self):
        msg_label = tk.Label(self.main_frame, text="KIRI:", bg='#2e7d32', 
                           fg='white', font=('Arial', 12, 'bold'), width=10)
        msg_label.grid(row=3, column=0, padx=5, pady=5, sticky='nw')
        
        self.kiri_box = tk.Text(self.main_frame, height=10, width=50, 
                               font=('Arial', 11))
        self.kiri_box.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

    def create_buttons(self):
        buttons_frame = tk.Frame(self.main_frame, bg='#e8f5e9')
        buttons_frame.grid(row=4, column=1, columnspan=2, pady=20)
        
        clear_btn = tk.Button(buttons_frame, text="PUHASTA", 
                            command=self.clear_form, bg='#2e7d32', fg='white',
                            font=('Arial', 10, 'bold'))
        clear_btn.pack(side='left', padx=5)
        
        send_btn = tk.Button(buttons_frame, text="SAADA", 
                           command=self.saada_kiri, bg='#2e7d32', fg='white',
                           font=('Arial', 10, 'bold'))
        send_btn.pack(side='left', padx=5)

    def vali_pilt(self):
        self.file = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
        if self.file:
            self.l_lisatud.configure(text=self.file)

    def clear_form(self):
        self.email_box.delete(0, tk.END)
        self.teema_box.delete(0, tk.END)
        self.kiri_box.delete('1.0', tk.END)
        self.l_lisatud.configure(text="")
        self.file = None

    def saada_kiri(self):
        try:
            kellele = self.email_box.get()
            teema = self.teema_box.get()
            kiri = self.kiri_box.get("1.0", tk.END)
            msg = EmailMessage()
            msg.set_content(kiri)
            msg['Subject'] = teema
            msg['From'] = "your_email@gmail.com" 
            msg['To'] = kellele
            if self.file:
                with open(self.file, 'rb') as fpilt:
                    pilt = fpilt.read()
                    msg.add_attachment(pilt, 
                                     maintype='image',
                                     subtype=imghdr.what(None, pilt))
            context = ssl.create_default_context()
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls(context=context)
                server.login("your_email@gmail.com", "your_app_password")
                server.send_message(msg)

            messagebox.showinfo("Info", "Kiri edukalt saadetud!")
            self.clear_form()

        except Exception as e:
            messagebox.showerror("Viga!", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = EmailApp(root)
    root.mainloop()
