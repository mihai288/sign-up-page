import tkinter as tk
from tkinter import messagebox
from tkinter import font

def sign_up():
    email = email_entry.get()
    password = password_entry.get()
    if "@" not in email or "." not in email:
        messagebox.showerror("Error", "Invalid email format")
        return
    if not any(char.isupper() for char in password):
        messagebox.showerror("Error", "Password must contain at least one uppercase letter")
        return
    with open("user_details.txt", "w") as file:
        file.write(f"email: {email}\n")
        file.write(f"password: {password}\n")
    messagebox.showinfo("Success", "Sign-up successful! Please log in.")
    switch_to_login()

def switch_to_login():
    signup_frame.pack_forget()
    login_frame.pack(pady=50)

def log_in():
    login_email = login_email_entry.get()
    login_password = login_password_entry.get()
    try:
        with open("user_details.txt", "r") as file:
            lines = file.readlines()
            saved_email = lines[0].strip().split(": ")[1]
            saved_password = lines[1].strip().split(": ")[1]
    except FileNotFoundError:
        messagebox.showerror("Error", "No user registered. Please sign up first.")
        return
    if login_email == saved_email and login_password == saved_password:
        messagebox.showinfo("Success", "Logged in successfully!")
    else:
        messagebox.showerror("Error", "Incorrect email or password")

root = tk.Tk()
root.title("Modern Sign Up & Log In")
root.geometry("400x500")
root.config(bg="#f7f7f7")

title_font = font.Font(family="Helvetica", size=18, weight="bold")
label_font = font.Font(family="Helvetica", size=12)
entry_font = font.Font(family="Helvetica", size=11)
button_style = {"bg": "#4a90e2", "fg": "white", "font": label_font, "activebackground": "#357ABD", "bd": 0, "relief": "flat"}

signup_frame = tk.Frame(root, bg="#f7f7f7", padx=20, pady=20)
signup_frame.pack(pady=50)

tk.Label(signup_frame, text="==== SIGN UP ====", font=title_font, bg="#f7f7f7").pack(pady=10)
tk.Label(signup_frame, text="Email:", font=label_font, bg="#f7f7f7").pack(anchor="w")
email_entry = tk.Entry(signup_frame, font=entry_font, width=30)
email_entry.pack(pady=5)

tk.Label(signup_frame, text="Password:", font=label_font, bg="#f7f7f7").pack(anchor="w")
password_entry = tk.Entry(signup_frame, show="*", font=entry_font, width=30)
password_entry.pack(pady=5)

sign_up_button = tk.Button(signup_frame, text="Sign Up", command=sign_up, **button_style)
sign_up_button.pack(pady=15)

login_frame = tk.Frame(root, bg="#f7f7f7", padx=20, pady=20)

tk.Label(login_frame, text="==== LOG IN ====", font=title_font, bg="#f7f7f7").pack(pady=10)
tk.Label(login_frame, text="Email:", font=label_font, bg="#f7f7f7").pack(anchor="w")
login_email_entry = tk.Entry(login_frame, font=entry_font, width=30)
login_email_entry.pack(pady=5)

tk.Label(login_frame, text="Password:", font=label_font, bg="#f7f7f7").pack(anchor="w")
login_password_entry = tk.Entry(login_frame, show="*", font=entry_font, width=30)
login_password_entry.pack(pady=5)

log_in_button = tk.Button(login_frame, text="Log In", command=log_in, **button_style)
log_in_button.pack(pady=15)

root.mainloop()
