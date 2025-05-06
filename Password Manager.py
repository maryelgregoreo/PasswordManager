import customtkinter as ctk
import random
import string
import pyperclip
import os

# Path to your file
file_path = r"S:/SE/Assessment 2/Username,Password.txt"

# Load credentials from file
def load_credentials():
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as f:
        lines = f.readlines()
    creds = []
    for line in lines:
        if ',' in line:
            username, password = line.strip().split(',', 1)
            creds.append({"username": username, "password": password})
    return creds

# Save a new credential to file
def save_credential_to_file(username, password):
    with open(file_path, "a") as f:
        f.write(f"{username},{password}\n")

credentials = load_credentials()

def generate_password(length=10):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))

def add_entry():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        credentials.append({"username": username, "password": password})
        save_credential_to_file(username, password)
        update_listbox()
        username_entry.delete(0, ctk.END)
        password_entry.delete(0, ctk.END)

def update_listbox():
    listbox.delete(0, ctk.END)
    for entry in credentials:
        listbox.insert(ctk.END, f"{entry['username']} | {entry['password']}")

def copy_selected():
    selected = listbox.curselection()
    if selected:
        item = credentials[selected[0]]
        pyperclip.copy(f"{item['username']}:{item['password']}")

# UI setup
ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("Password Manager")
app.geometry("500x400")

frame = ctk.CTkFrame(app)
frame.pack(padx=20, pady=20, fill="both", expand=True)

username_entry = ctk.CTkEntry(frame, placeholder_text="Username")
username_entry.pack(pady=5)

password_entry = ctk.CTkEntry(frame, placeholder_text="Password", show="*")
password_entry.pack(pady=5)

generate_btn = ctk.CTkButton(frame, text="Generate Password", command=lambda: password_entry.insert(0, generate_password()))
generate_btn.pack(pady=5)

add_btn = ctk.CTkButton(frame, text="Add Entry", command=add_entry)
add_btn.pack(pady=5)

listbox = ctk.CTkTextbox(frame, height=150)
listbox.pack(pady=10, fill="both", expand=True)
update_listbox()

copy_btn = ctk.CTkButton(frame, text="Copy Selected", command=copy_selected)
copy_btn.pack(pady=5)

app.mainloop()
