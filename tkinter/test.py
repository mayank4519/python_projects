import tkinter as tk
from tkinter import ttk

def greet():
    print("Hello, world")

root = tk.Tk()
root.title("Hello")

greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(side="left", fill="x", expand=True)

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="right", fill="x", expand=True)

# window pops up and code stand still until window exit.
root.mainloop()

greet()