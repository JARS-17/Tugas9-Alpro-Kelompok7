import tkinter as tk

class TodoList:
    def __init__(self, root):
        self.root = root
        
        # Listbox untuk menampilkan daftar tugas
        self.listbox = tk.Listbox(root, height=10, width=50, font=("Arial", 14))
        self.listbox.pack(pady=20)
        
        # Entry untuk memasukkan task baru
        self.entry = tk.Entry(root, font=("Arial", 14), width=40)
        self.entry.pack(pady=10)
        
        # Tombol untuk menambah task
        self.add_button = tk.Button(root, text="Add Task", font=("Arial", 15), command=self.add_task)
        self.add_button.pack(pady=10)
        
        # Tombol untuk menghapus semua task
        self.delete_button = tk.Button(root, text="Delete All Tasks", font=("Arial", 15), command=self.delete_all_tasks)
        self.delete_button.pack(pady=10)

    # Fungsi untuk menambah task baru
    def add_task(self):
        task = self.entry.get()  # Ambil task dari entry
        if task:  # Pastikan task tidak kosong
            self.listbox.insert(tk.END, task)  # Menambahkan task ke listbox
            self.entry.delete(0, tk.END)  # Bersihkan entry setelah task ditambahkan

    # Fungsi untuk menghapus semua task
    def delete_all_tasks(self):
        self.listbox.delete(0, tk.END)  # Menghapus semua task dari listbox

if __name__ == "__main__":
    root = tk.Tk()
    root.title("To-Do List")
    todo = TodoList(root)
    root.mainloop()
