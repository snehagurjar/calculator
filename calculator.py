import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")

        # Entry widget for display
        self.display = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Define buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        # Place buttons in grid
        row_val = 1
        col_val = 0
        for button_text in buttons:
            button = tk.Button(root, text=button_text, font=("Arial", 18), width=5, height=2,
                               command=lambda text=button_text: self.on_button_click(text))
            button.grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == 'C':
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid input")
                self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
