import tkinter as tk
from tkinter import messagebox
import string
import secrets


# -------------------------
# Generate Password
# -------------------------
def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showwarning(
                "Warning",
                "Password length should be at least 4"
            )
            return

        characters = (
            string.ascii_uppercase +
            string.ascii_lowercase +
            string.digits +
            string.punctuation
        )

        password = ''.join(
            secrets.choice(characters)
            for _ in range(length)
        )

        password_var.set(password)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Enter a valid password length."
        )


# -------------------------
# Password Strength Auditor
# -------------------------
def check_strength():

    password = audit_entry.get()

    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        strength_label.config(
            text="Weak",
            fg="red"
        )

    elif score <= 4:
        strength_label.config(
            text="Medium",
            fg="orange"
        )

    elif score == 5:
        strength_label.config(
            text="Strong",
            fg="green"
        )

    else:
        strength_label.config(
            text="Very Strong",
            fg="darkgreen"
        )


# -------------------------
# Copy Password
# -------------------------
def copy_password():

    password = password_var.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)

        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard!"
        )


# -------------------------
# Main Window
# -------------------------
root = tk.Tk()

root.title("Cryptographic Password Generator")
root.geometry("600x500")
root.configure(bg="#000000")

# -------------------------
# Title
# -------------------------
title = tk.Label(
    root,
    text="Cryptographic Password Generator",
    font=("Arial", 18, "bold"),
    bg="#F0F8FF"
)

title.pack(pady=15)

# -------------------------
# Password Generator
# -------------------------
tk.Label(
    root,
    text="Password Length:",
    font=("Arial", 12),
    bg="#F0F8FF"
).pack()

length_entry = tk.Entry(
    root,
    font=("Arial", 12)
)

length_entry.pack(pady=5)

generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12),
    bg="lightblue",
    command=generate_password
)

generate_btn.pack(pady=10)

password_var = tk.StringVar()

password_entry = tk.Entry(
    root,
    textvariable=password_var,
    width=40,
    font=("Arial", 12)
)

password_entry.pack(pady=5)

copy_btn = tk.Button(
    root,
    text="Copy Password",
    font=("Arial", 12),
    command=copy_password
)

copy_btn.pack(pady=10)

# -------------------------
# Divider
# -------------------------
tk.Label(
    root,
    text="-----------------------------------------",
    bg="#F0F8FF"
).pack()

# -------------------------
# Strength Auditor
# -------------------------
audit_title = tk.Label(
    root,
    text="Password Strength Auditor",
    font=("Arial", 16, "bold"),
    bg="#F0F8FF"
)

audit_title.pack(pady=10)

audit_entry = tk.Entry(
    root,
    width=40,
    font=("Arial", 12)
)

audit_entry.pack(pady=5)

audit_btn = tk.Button(
    root,
    text="Check Strength",
    font=("Arial", 12),
    bg="lightgreen",
    command=check_strength
)

audit_btn.pack(pady=10)

strength_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="#F0F8FF"
)
BG_COLOR = "#000000"
TEXT_COLOR = "#00FF00"

for widget in root.winfo_children():
    try:
        widget.config(
            bg=BG_COLOR,
            fg=TEXT_COLOR
        )
    except:
        pass

strength_label.pack(pady=10)

root.mainloop()