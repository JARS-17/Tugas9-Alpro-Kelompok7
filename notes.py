import tkinter as tk
from tkinter import messagebox

class Notes:
    def __init__(self, root):
        self.root = root
        self.text_area = tk.Text(root, height=10, width=50, font=("Arial", 14))
        self.text_area.pack(pady=20)
        
        self.save_button = tk.Button(root, text="Save Note", font=("Arial", 15), command=self.save_note)
        self.save_button.pack(pady=10)

        self.read_button = tk.Button(root, text="Read Note", font=("Arial", 15), command=self.read_note)
        self.read_button.pack(pady=10)

    def save_note(self):
        with open("note.txt", "w") as file:
            file.write(self.text_area.get("1.0", tk.END))
        messagebox.showinfo("Info", "Note saved successfully!")

    def read_note(self):
        try:
            with open("note.txt", "r") as file:
                note = file.read()
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, note)
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No saved notes found.")
