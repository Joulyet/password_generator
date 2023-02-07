import string
import secrets
import tkinter as tk

def generate_password(n: int) -> str:
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(n))
    return password

def generate_and_display():
    password = generate_password(16)
    password_label.config(text=password)

root = tk.Tk()
root.title("Générateur de mot de passe")

password_label = tk.Label(root, text="")
password_label.pack()

generate_button = tk.Button(root, text="Générer", command=generate_and_display)
generate_button.pack()

root.mainloop()
