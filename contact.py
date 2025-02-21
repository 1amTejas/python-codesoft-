import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []

def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter Name:")
    phone = simpledialog.askstring("Add Contact", "Enter Phone:")
    email = simpledialog.askstring("Add Contact", "Enter Email:")
    address = simpledialog.askstring("Add Contact", "Enter Address:")
    
    if name and phone:
        contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
        update_contact_list()
    else:
        messagebox.showerror("Error", "Name and Phone are required!")

def update_contact_list():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

def search_contact():
    query = simpledialog.askstring("Search Contact", "Enter Name or Phone:")
    results = [c for c in contacts if query in c['Name'] or query in c['Phone']]
    
    listbox.delete(0, tk.END)
    for contact in results:
        listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

def update_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a contact to update")
        return
    
    index = selected[0]
    contact = contacts[index]
    contact['Name'] = simpledialog.askstring("Update Contact", "Enter Name:", initialvalue=contact['Name'])
    contact['Phone'] = simpledialog.askstring("Update Contact", "Enter Phone:", initialvalue=contact['Phone'])
    contact['Email'] = simpledialog.askstring("Update Contact", "Enter Email:", initialvalue=contact['Email'])
    contact['Address'] = simpledialog.askstring("Update Contact", "Enter Address:", initialvalue=contact['Address'])
    update_contact_list()

def delete_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a contact to delete")
        return
    index = selected[0]
    contacts.pop(index)
    update_contact_list()

# GUI Setup
root = tk.Tk()
root.title("Contact Manager")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add", command=add_contact).grid(row=0, column=0)
tk.Button(button_frame, text="Search", command=search_contact).grid(row=0, column=1)
tk.Button(button_frame, text="Update", command=update_contact).grid(row=0, column=2)
tk.Button(button_frame, text="Delete", command=delete_contact).grid(row=0, column=3)

root.mainloop()