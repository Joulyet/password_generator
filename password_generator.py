import string
import secrets
import tkinter as tk
import sqlite3

def generate_password(n: int, include_letters: bool, include_numbers: bool, include_symbols: bool) -> str:
    alphabet = ""
    if include_letters:
        alphabet += string.ascii_letters
    if include_numbers:
        alphabet += string.digits
    if include_symbols:
        alphabet += string.punctuation
    password = ""
    for i in range(n):
        password += secrets.choice(alphabet)
    return password

def generate_and_display():
    n = int(length_entry.get())
    include_letters = letters_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()
    password = generate_password(n, include_letters, include_numbers, include_symbols)
    password_label.config(text=password)
    save_button.config(state="normal")

def save_password():
    password = password_label.cget("text")
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS passwords (password TEXT)")
    c.execute("INSERT INTO passwords VALUES (?)", (password,))
    conn.commit()
    conn.close()
    save_button.config(state="disabled")

root = tk.Tk()
root.title("Générateur de mot de passe")

length_label = tk.Label(root, text="Longueur du mot de passe :")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

letters_var = tk.BooleanVar()
letters_checkbutton = tk.Checkbutton(root, text="Lettres", variable=letters_var)
letters_checkbutton.pack()

numbers_var = tk.BooleanVar()
numbers_checkbutton = tk.Checkbutton(root, text="Chiffres", variable=numbers_var)
numbers_checkbutton.pack()

symbols_var = tk.BooleanVar()
symbols_checkbutton = tk.Checkbutton(root, text="Caractères spéciaux", variable=symbols_var)
symbols_checkbutton.pack()

password_label = tk.Label(root, text="")
password_label.pack()

generate_button = tk.Button(root, text="Générer", command=generate_and_display)
generate_button.pack()

save_button = tk.Button(root, text="Enregistrer", command=save_password, state="disabled")
save_button.pack()

root.mainloop()
