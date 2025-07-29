import tkinter as tk
from tkinter import messagebox
import re

# === Recursive Expression Evaluation ===

def evaluate_expression(expr):
    expr = expr.replace(' ', '')
    while '(' in expr:
        inner = re.search(r'\(([^()]+)\)', expr)
        if not inner:
            raise ValueError("Mismatched parentheses.")
        value = evaluate_expression(inner.group(1))
        expr = expr[:inner.start()] + str(value) + expr[inner.end():]
    return eval_no_parentheses(expr)

def eval_no_parentheses(expr):
    tokens = re.findall(r'-?\d+\.?\d*|[+\-*/]', expr)

    # Handle * and /
    i = 0
    while i < len(tokens):
        if tokens[i] in ('*', '/'):
            left = float(tokens[i - 1])
            right = float(tokens[i + 1])
            result = left * right if tokens[i] == '*' else left / right
            tokens[i - 1:i + 2] = [str(result)]
            i = 0
        else:
            i += 1

    # Handle + and -
    result = float(tokens[0])
    i = 1
    while i < len(tokens):
        op = tokens[i]
        num = float(tokens[i + 1])
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        i += 2

    return result

# === GUI Calculator ===

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recursive Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.display = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="ridge", justify='right')
        self.display.pack(padx=10, pady=10, fill='x')

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '(', ')'],
            ['C', '=', '+']
        ]

        for row in buttons:
            frame = tk.Frame(self.root)
            frame.pack(expand=True, fill='both')
            for btn in row:
                action = lambda x=btn: self.on_button_click(x)
                tk.Button(frame, text=btn, font=("Arial", 18), command=action).pack(side='left', expand=True, fill='both')

    def on_button_click(self, char):
        if char == "C":
            self.display.delete(0, tk.END)
        elif char == "=":
            try:
                expr = self.display.get()
                result = evaluate_expression(expr)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            self.display.insert(tk.END, char)

# === Run the App ===

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()