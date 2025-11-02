import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

#Encryption Setup
key = Fernet.generate_key()
f = Fernet(key)

def encrypt_file(filepath):
    with open(filepath, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)
    encrypted_filename = "encrypted_" + filepath.split('/')[-1]

    with open(encrypted_filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    return encrypted_filename

def decrypt_file(filepath):
    with open(filepath, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted = f.decrypt(encrypted_data)
    decrypted_filename = "decrypted_" + filepath.split('/')[-1]

    with open(decrypted_filename, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

    return decrypted_filename

#GUI Setup
root = tk.Tk()
root.title("File Encryptor")
root.geometry("400x250")
root.config(bg="#1e1e1e")

file_path_var = tk.StringVar()

def browse_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        file_path_var.set(filepath)

def encrypt_action():
    filepath = file_path_var.get()
    if not filepath:
        messagebox.showerror("Error", "Please select a file first.")
        return
    encrypted_filename = encrypt_file(filepath)
    messagebox.showinfo("Success", f"File encrypted as {encrypted_filename}")

def decrypt_action():
    filepath = file_path_var.get()
    if not filepath:
        messagebox.showerror("Error", "Please select a file first.")
        return
    decrypted_filename = decrypt_file(filepath)
    messagebox.showinfo("Success", f"File decrypted as {decrypted_filename}")

title_label = tk.Label(root, text="🔐 File Encryptor", fg="white", bg="#1e1e1e", font=("Segoe UI", 16, "bold"))
title_label.pack(pady=10)

file_entry = tk.Entry(root, textvariable=file_path_var, width=40, font=("Segoe UI", 10))
file_entry.pack(pady=5)

browse_btn = tk.Button(root, text="Browse", command=browse_file, bg="#0078D7", fg="white", font=("Segoe UI", 10))
browse_btn.pack(pady=5)

encrypt_btn = tk.Button(root, text="Encrypt", command=encrypt_action, bg="#28a745", fg="white", width=10, font=("Segoe UI", 10))
encrypt_btn.pack(pady=5)

decrypt_btn = tk.Button(root, text="Decrypt", command=decrypt_action, bg="#dc3545", fg="white", width=10, font=("Segoe UI", 10))
decrypt_btn.pack(pady=5)

root.mainloop()