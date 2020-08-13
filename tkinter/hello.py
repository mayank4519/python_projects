import tkinter as tk
from tkinter import ttk

def greet():
    print(f"Hello, {user_name.get() or 'World'}")

root = tk.Tk()
root.title("Hello")

user_name = tk.StringVar()

name_label = ttk.Label(root, text="Name: ")
name_label.pack(side="left", padx=(5, 10), pady=(10, 10))
name_entry = ttk.Entry(root, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()

greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(side="left", fill="x", expand=True)

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="right", fill="x", expand=True)

# window pops up and code stand still until window exit.
root.mainloop()