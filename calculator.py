import tkinter as tk

class Calculator:
    def _init_(self, root):
        self.root = root
        self.result = tk.Entry(root, font=("Arial", 20), bd=10, relief="sunken", width=14, justify="right")
        self.result.grid(row=0, column=0, columnspan=4)
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        row = 1
        col = 0
        for button in buttons:
            tk.Button(root, text=button, font=("Arial", 15), width=5, height=2, command=lambda b=button: self.on_click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_click(self, button):
        current = self.result.get()
        if button == 'C':
            self.result.delete(0, tk.END)
        elif button == '=':
            try:
                self.result.delete(0, tk.END)
                self.result.insert(tk.END, str(eval(current)))
            except:
                self.result.delete(0, tk.END)
                self.result.insert(tk.END, "Error")
        else:
            self.result.insert(tk.END, button)
