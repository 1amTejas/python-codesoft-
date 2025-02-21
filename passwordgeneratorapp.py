import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Please enter a positive number")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

root = tk.Tk()
root.title("Password Generator")

entry_length = tk.Entry(root)
entry_length.pack()

gen_button = tk.Button(root, text="Generate Password", command=generate_password)
gen_button.pack()

result_label = tk.Label(root, text="Generated Password:")
result_label.pack()

root.mainloop()
