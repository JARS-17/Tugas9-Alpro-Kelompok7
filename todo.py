import tkinter as tk

class TodoList:
    def __init__(self, root):
        self.root = root
        self.listbox = tk.Listbox(root, height=10, width=50, font=("Arial", 14))
        self.listbox.pack(pady=20)

        self.add_button = tk.Button(root, text="Add Task", font=("Arial", 15), command=self.add_task)
        self.add_button.pack(pady=10)

        self.delete_button = tk.Button(root, text="Delete All Tasks", font=("Arial", 15), command=self.delete_all_tasks)
        self.delete_button.pack(pady=10)

    def add_task(self):
        task = self.listbox.get(tk.ACTIVE)
        if task:
            self.listbox.delete(tk.ACTIVE)

    def delete_all_tasks(self):
        self.listbox.delete(0, tk.END)
