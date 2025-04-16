import tkinter as tk
from tkinter import messagebox

import re

import random

def press(key):
    if key == "x²":
        entry.insert(tk.END, "²")
    elif key == "x³":
        entry.insert(tk.END, "³")
    else:
        entry.insert(tk.END, key)
    adjust_entry_width()  # lai nebūtu par maz vietas

def clear():
    entry.delete(0, tk.END)
    adjust_entry_width() 

def adjust_entry_width():# lai nebūtu par maz vietas
    content_length = len(entry.get())
    new_width = max(20, content_length)  # Minimum width is 20
    entry.config(width=new_width)

def calculate():#complex aprēķini lol
    try:
        typeShit = entry.get()
        #es teikšu godīgi, es nezinu kā strādā 32. rinda, to man iedeva github copilot :D
        typeShit = typeShit.replace("²", "**2").replace("³", "**3")# nomainīt ² un ³ lai python var izdarīt savu maģiju
        typeShit = re.sub(r'(\d|\*\*\d)(\()', r'\1*\2', typeShit)  # Pārliecinās, ka starp skaitli un atvērtu iekavu ir reizināšanas zīme
        rezultats = eval(typeShit) + (1 * random.uniform(-0.00000001, 0.00000001))
        rezultats = round(rezultats, 10)  # noapaļo līdz 10 cipariem aiz komata
        if random.randint(0, 100) < 5 or rezultats > 100000:
            rezultats = "Hello World!"
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(rezultats))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

#main window
root = tk.Tk()
root.title("Goofy Calculator")

#ievades laukums
entry = tk.Entry(root, width=20, font=("Arial", 16), bd=5, insertwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4)

#pogas n stuff
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('(', 1, 4),(')', 1, 5),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('x²', 2, 4),('x³', 2, 5),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=calculate)
    elif text == "C":
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=clear)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda t=text: press(t))
    btn.grid(row=row, column=col)

root.mainloop()