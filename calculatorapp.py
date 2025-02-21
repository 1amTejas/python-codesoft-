import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation")
            return
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Simple Calculator")

entry1 = tk.Entry(root)
entry1.pack()

operation_var = tk.StringVar(value='+')
operations = ['+', '-', '*', '/']
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.pack()

entry2 = tk.Entry(root)
entry2.pack()

calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.pack()

result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()
