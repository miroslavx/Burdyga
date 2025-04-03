import tkinter as tk
from tkinter import filedialog, messagebox
import smtplib
from email.message import EmailMessage
import imghdr
import ssl
import os


root = tk.Tk()
root.title("E-kirja saatmine")
root.geometry("700x550")
root.configure(bg="#e8f1fc")  
email_var = tk.StringVar()
subject_var = tk.StringVar()
attachment_path = None
def vali_pilt():
    """Function to select a file attachment"""
    global attachment_path
    file = filedialog.askopenfilename()
    if file:
        attachment_path = file
        l_lisatud.configure(text=os.path.basename(file))
    return file

def saada_kiri():
    """Function to send the email"""
    global attachment_path
    
    try:
        kellele = email_var.get()
        if not kellele:
            messagebox.showerror("Viga", "Palun sisestage e-posti aadress!")
            return
        teema = subject_var.get()
        kiri = kiri_box.get("1.0", tk.END)
        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = "burmir05@gmail.com"
        password = "stbq irxq spkb mgzz"
        msg = EmailMessage()
        msg.set_content(kiri)
        msg['Subject'] = teema if teema else "E-kiri saatmine"
        msg['From'] = sender_email
        msg['To'] = kellele
        if attachment_path:
            try:
                with open(attachment_path, 'rb') as fpilt:
                    pilt = fpilt.read()
                    
                file_type = imghdr.what(None, pilt)
                if file_type:
                    msg.add_attachment(pilt, maintype='image', subtype=file_type, 
                                      filename=os.path.basename(attachment_path))
                else:
                    filename = os.path.basename(attachment_path)
                    msg.add_attachment(pilt, maintype='application', subtype='octet-stream', 
                                      filename=filename)
            except Exception as e:
                messagebox.showerror("Manuse viga", f"Probleem manusega: {str(e)}")
                return
        context = ssl.create_default_context()
        
        try:
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.send_message(msg)
            server.quit()
            
            messagebox.showinfo("Informatsioon", "Kiri oli saadetud")
            email_var.set("")
            subject_var.set("")
            kiri_box.delete("1.0", tk.END)
            l_lisatud.configure(text="")
            attachment_path = None
            
        except smtplib.SMTPAuthenticationError as auth_error:
            error_message = f"Autentimise viga: {str(auth_error)}\n\n"
            error_message += "Võimalikud lahendused:\n"
            error_message += "1. Kontrollige, et kasutate App Password'i, mitte tavalist parooli\n"
            error_message += "2. Veenduge, et teie e-posti aadress on õige"
            messagebox.showerror("Autentimise viga", error_message)
        except smtplib.SMTPException as smtp_error:
            messagebox.showerror("SMTP viga", f"E-posti saatmisel tekkis viga: {str(smtp_error)}")
            
    except Exception as e:
        messagebox.showerror("Tekkis viga!", str(e))
main_frame = tk.Frame(root, bg="#e8f1fc", padx=20, pady=20)
main_frame.pack(fill="both", expand=True)
header_frame = tk.Frame(main_frame, bg="#e8f1fc")
header_frame.pack(fill="x", pady=(0, 15))
title_label = tk.Label(header_frame, text="🌸 E-kirja saatmine", font=("Arial", 16, "bold"), 
                      bg="#e8f1fc", fg="#29802e")
title_label.pack(side="left")
email_frame = tk.Frame(main_frame, bg="#e8f1fc")
email_frame.pack(fill="x", pady=5)
email_label = tk.Label(email_frame, text="EMAIL:", font=("Arial", 10, "bold"), 
                     bg="#e8f1fc", fg="#3d5ea6")
email_label.pack(side="left", padx=(0, 10))

email_entry = tk.Entry(email_frame, textvariable=email_var, font=("Arial", 10),
                     bd=2, relief="groove", bg="white")
email_entry.pack(side="left", fill="x", expand=True)
subject_frame = tk.Frame(main_frame, bg="#e8f1fc")
subject_frame.pack(fill="x", pady=5)

subject_label = tk.Label(subject_frame, text="TEEMA:", font=("Arial", 10, "bold"), 
                       bg="#e8f1fc", fg="#3d5ea6")
subject_label.pack(side="left", padx=(0, 10))

subject_entry = tk.Entry(subject_frame, textvariable=subject_var, font=("Arial", 10),
                       bd=2, relief="groove", bg="white")
subject_entry.pack(side="left", fill="x", expand=True)
attach_frame = tk.Frame(main_frame, bg="#e8f1fc")
attach_frame.pack(fill="x", pady=5)
attach_label = tk.Label(attach_frame, text="LISA:", font=("Arial", 10, "bold"), 
                      bg="#e8f1fc", fg="#3d5ea6")
attach_label.pack(side="left", padx=(0, 10))
l_lisatud = tk.Label(attach_frame, text="", font=("Arial", 10), bg="#e8f1fc")
l_lisatud.pack(side="left", fill="x", expand=True)
message_frame = tk.Frame(main_frame, bg="#e8f1fc")
message_frame.pack(fill="both", expand=True, pady=5)
message_label = tk.Label(message_frame, text="KIRI:", font=("Arial", 10, "bold"), 
                       bg="#e8f1fc", fg="#3d5ea6")
message_label.pack(anchor="w", padx=(0, 10), pady=(0, 5))
kiri_box_frame = tk.Frame(message_frame, bg="#e8f1fc", bd=2, relief="groove")
kiri_box_frame.pack(fill="both", expand=True)

kiri_box = tk.Text(kiri_box_frame, font=("Arial", 10), wrap="word", 
                 bg="white", bd=0, padx=10, pady=10)
kiri_box.pack(side="left", fill="both", expand=True)
scrollbar = tk.Scrollbar(kiri_box_frame)
scrollbar.pack(side="right", fill="y")
kiri_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=kiri_box.yview)
button_frame = tk.Frame(main_frame, bg="#e8f1fc")
button_frame.pack(fill="x", pady=(15, 0))
lisa_pilt_btn = tk.Button(button_frame, text="📎 Lisa Pilt", command=vali_pilt, 
                        font=("Arial", 10, "bold"), bg="#f7d449", fg="#000000",
                        activebackground="#f5ca2a", activeforeground="#000000",
                        relief="raised", padx=15, pady=6, bd=2)
lisa_pilt_btn.pack(side="left")

saada_btn = tk.Button(button_frame, text="✉️ Saada", command=saada_kiri, 
                    font=("Arial", 10, "bold"), bg="#76c73b", fg="#ffffff",
                    activebackground="#5fa32e", activeforeground="#ffffff",
                    relief="raised", padx=15, pady=6, bd=2)
saada_btn.pack(side="right")
status_frame = tk.Frame(main_frame, bg="#e8f1fc")
status_frame.pack(fill="x", pady=(15, 0))

status_label = tk.Label(status_frame, text="🟢 Online", font=("Arial", 9), 
                      bg="#e8f1fc", fg="#5fa32e")
status_label.pack(side="left")

root.mainloop()
