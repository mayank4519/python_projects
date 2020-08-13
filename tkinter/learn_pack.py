import tkinter as tk

root = tk.Tk()

tk.Label(root, text="Label left", bg= "green").pack(
    side="left", fill="both", expand=True)

tk.Label(root, text="Label top", bg= "red").pack(side="top", fill="both", expand=True)
tk.Label(root, text="Label top", bg= "red").pack(side="top", fill="both", expand=True)

tk.Label(root, text="Label left", bg= "green").pack(
    side="left", fill="both", expand=True)
tk.Label(root, text="Label left", bg= "green").pack(
    side="left", fill="both", expand=True)

root.mainloop()