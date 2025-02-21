import tkinter as tk

class ToDoApp:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.root.title("To-Do List")
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        
        self.task_listbox = tk.Listbox(self.frame, width=40, height=10)
        self.task_listbox.pack(side=tk.LEFT, padx=10)
        
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(pady=5)
        
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=5)
    
    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
