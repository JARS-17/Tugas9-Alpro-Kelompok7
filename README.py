import tkinter as tk
import time
import threading

class Timer:
    def _init_(self, root):
        self.root = root
        self.time_left = 0
        self.is_running = False
        self.label = tk.Label(root, text="00:00", font=("Arial", 30))
        self.label.pack(pady=20)
        
        self.entry = tk.Entry(root, font=("Arial", 20))
        self.entry.pack(pady=20)
        
        self.start_button = tk.Button(root, text="Start Timer", font=("Arial", 15), command=self.start_timer)
        self.start_button.pack(pady=10)

    def countdown(self):
        while self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            self.label.config(text=f"{mins:02}:{secs:02}")
            time.sleep(1)
            self.time_left -= 1
        self.label.config(text="Time's up!")
        
    def start_timer(self):
        if self.is_running:
            return
        try:
            self.time_left = int(self.entry.get()) * 60
            self.is_running = True
            threading.Thread(target=self.countdown).start()
        except ValueError:
            self.label.config(text="Enter a valid number")
#donelekku
