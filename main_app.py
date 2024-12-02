import tkinter as tk
from tkinter import Menu
from timer import Timer
from notes import Notes
from todo import TodoList
from calculator import Calculator
from motivational_quotes import get_random_quote

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Productivity App")
        
        self.menu = Menu(root)
        root.config(menu=self.menu)
        
        self.timer_frame = tk.Frame(root)
        self.notes_frame = tk.Frame(root)
        self.todo_frame = tk.Frame(root)
        self.calculator_frame = tk.Frame(root)

        self.menu.add_command(label="Timer", command=self.show_timer)
        self.menu.add_command(label="Notes", command=self.show_notes)
        self.menu.add_command(label="To-Do List", command=self.show_todo)
        self.menu.add_command(label="Calculator", command=self.show_calculator)
        self.menu.add_command(label="Motivational Quote", command=self.show_quote)

        self.quote_label = tk.Label(root, text=get_random_quote(), font=("Arial", 20))
        self.quote_label.pack(pady=20)

    def show_timer(self):
        self.clear_frames()
        self.timer = Timer(self.timer_frame)
        self.timer_frame.pack()

    def show_notes(self):
        self.clear_frames()
        self.notes = Notes(self.notes_frame)
        self.notes_frame.pack()

    def show_todo(self):
        self.clear_frames()
        self.todo = TodoList(self.todo_frame)
        self.todo_frame.pack()

    def show_calculator(self):
        self.clear_frames()
        self.calculator = Calculator(self.calculator_frame)
        self.calculator_frame.pack()

    def show_quote(self):
        self.quote_label.config(text=get_random_quote())

    def clear_frames(self):
        for frame in [self.timer_frame, self.notes_frame, self.todo_frame, self.calculator_frame]:
            frame.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
