import customtkinter as ctk
import os

# Configure CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# File to save credentials
CREDENTIALS_FILE = "savedcredentials.txt"

# App Window
app = ctk.CTk()
app.title("Password Manager")
app.geometry("550x550")

# ---------- PAGE FRAMES ---------- #
main_frame = ctk.CTkFrame(app)
add_frame = ctk.CTkFrame(app)
view_frame = ctk.CTkFrame(app)

# ---------- PAGE SWITCHING ---------- #
def show_main():
    add_frame.pack_forget()
    view_frame.pack_forget()
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

def show_add_password():
    main_frame.pack_forget()
    add_frame.pack(fill="both", expand=True, padx=20, pady=20)

def show_view_passwords():
    main_frame.pack_forget()
    view_frame.pack(fill="both", expand=True, padx=20, pady=20)
    load_credentials()

# ---------- SAVE & CLEAR ---------- #
def save_credentials():
    entry_type = type_entry.get().strip()
    entry_email = email_entry.get().strip()
    entry_password = password_entry.get().strip()

    if entry_type and entry_email and entry_password:
        with open(CREDENTIALS_FILE, "a") as f:
            f.write(f"{entry_type},{entry_email},{entry_password}\n")
        clear_inputs()

def clear_inputs():
    type_entry.delete(0, ctk.END)
    email_entry.delete(0, ctk.END)
    password_entry.delete(0, ctk.END)

# ---------- LOAD & DISPLAY CREDENTIALS ---------- #
def load_credentials():
    textbox.configure(state="normal")
    textbox.delete("0.0", ctk.END)

    if not os.path.exists(CREDENTIALS_FILE):
        textbox.insert(ctk.END, "No credentials file found.\n")
    else:
        with open(CREDENTIALS_FILE, "r") as f:
            lines = [line.strip() for line in f if line.strip()]

        if not lines:
            textbox.insert(ctk.END, "No saved credentials.\n")
        else:
            for i, line in enumerate(lines, 1):
                parts = line.split(",")
                if len(parts) == 3:
                    entry_type, email, password = parts
                    textbox.insert(ctk.END,
                        f"{i})\n"
                        f"Type:     {entry_type}\n"
                        f"Email:    {email}\n"
                        f"Password: {password}\n"
                        f"{'-'*40}\n"
                    )
                else:
                    textbox.insert(ctk.END, f"{i}) Malformed entry: {line}\n{'-'*40}\n")

    textbox.configure(state="disabled")

# ---------- MAIN PAGE ---------- #
main_label = ctk.CTkLabel(main_frame, text="Password Manager", font=ctk.CTkFont(size=32, weight="bold"))
main_label.pack(pady=40)

add_btn = ctk.CTkButton(main_frame, text="Add Password", command=show_add_password, width=200)
add_btn.pack(pady=10)

view_btn = ctk.CTkButton(main_frame, text="View Password", command=show_view_passwords, width=200)
view_btn.pack(pady=10)

# ---------- ADD PASSWORD PAGE ---------- #
header_label = ctk.CTkLabel(add_frame, text="➕ ADD", font=ctk.CTkFont(size=32, weight="bold"), text_color="#FF66CC")
header_label.pack(pady=(10, 20))

type_label = ctk.CTkLabel(add_frame, text="1] Type:", text_color="#B266FF", anchor="w")
type_label.pack(fill="x")
type_entry = ctk.CTkEntry(add_frame, placeholder_text="e.g., Facebook")
type_entry.pack(pady=5)

email_label = ctk.CTkLabel(add_frame, text="2] Email:", text_color="#B266FF", anchor="w")
email_label.pack(fill="x")
email_entry = ctk.CTkEntry(add_frame, placeholder_text="example@gmail.com")
email_entry.pack(pady=5)

password_label = ctk.CTkLabel(add_frame, text="3] Password:", text_color="#B266FF", anchor="w")
password_label.pack(fill="x")
password_entry = ctk.CTkEntry(add_frame, show="", placeholder_text="**********")
password_entry.pack(pady=5)

button_frame = ctk.CTkFrame(add_frame, fg_color="transparent")
button_frame.pack(pady=20)

save_btn = ctk.CTkButton(button_frame, text="Save", width=100, command=save_credentials)
save_btn.grid(row=0, column=0, padx=5)

clear_btn = ctk.CTkButton(button_frame, text="All Clear", width=100, command=clear_inputs)
clear_btn.grid(row=0, column=1, padx=5)

back_btn = ctk.CTkButton(button_frame, text="Back", width=100, command=show_main)
back_btn.grid(row=0, column=2, padx=5)

# ---------- VIEW PASSWORD PAGE ---------- #
view_label = ctk.CTkLabel(view_frame, text="Saved Credentials", font=ctk.CTkFont(size=28, weight="bold"), text_color="#66CCFF")
view_label.pack(pady=(10, 10))

textbox = ctk.CTkTextbox(view_frame, width=500, height=350, font=ctk.CTkFont(size=14))
textbox.pack(pady=10)
textbox.configure(state="disabled")

back_view_btn = ctk.CTkButton(view_frame, text="Back", command=show_main)
back_view_btn.pack(pady=10)

# Start at Main Page
show_main()

app.mainloop()
