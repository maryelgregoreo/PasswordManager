import customtkinter as ctk

# App settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Password Manager")
app.geometry("500x500")

# Path to your file
file_path = r"S:/SE/Assessment 2/Username,Password.txt"

# Frame
frame = ctk.CTkFrame(app)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Header
header_label = ctk.CTkLabel(frame, text="➕ ADD", font=ctk.CTkFont(size=32, weight="bold"), text_color="#FF66CC")
header_label.pack(pady=(10, 20))

# Input Fields
type_label = ctk.CTkLabel(frame, text="1] Type:", text_color="#B266FF", anchor="w")
type_label.pack(fill="x")
type_entry = ctk.CTkEntry(frame, placeholder_text="e.g., Facebook")
type_entry.pack(pady=5)

email_label = ctk.CTkLabel(frame, text="2] Email:", text_color="#B266FF", anchor="w")
email_label.pack(fill="x")
email_entry = ctk.CTkEntry(frame, placeholder_text="example@gmail.com")
email_entry.pack(pady=5)

username_label = ctk.CTkLabel(frame, text="3] Username:", text_color="#B266FF", anchor="w")
username_label.pack(fill="x")
username_entry = ctk.CTkEntry(frame)
username_entry.pack(pady=5)

password_label = ctk.CTkLabel(frame, text="4] Password:", text_color="#B266FF", anchor="w")
password_label.pack(fill="x")
password_entry = ctk.CTkEntry(frame, show="", placeholder_text="**********")
password_entry.insert(0, "1234567890")
password_entry.pack(pady=5)

# Buttons
button_frame = ctk.CTkFrame(frame, fg_color="transparent")
button_frame.pack(pady=20)

save_btn = ctk.CTkButton(button_frame, text="Save", width=100)
save_btn.grid(row=0, column=0, padx=5)

clear_btn = ctk.CTkButton(button_frame, text="All Clear", width=100)
clear_btn.grid(row=0, column=1, padx=5)

back_btn = ctk.CTkButton(button_frame, text="Back", width=100)
back_btn.grid(row=0, column=2, padx=5)

app.mainloop()
