import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

text_contents = dict()


def create_file(content="", title="Untitled"):
    container = ttk.Frame(notebook)
    container.pack()

    # 2. We create text areas and put them inside notebook
    text_area = tk.Text(container)
    text_area.insert("end", content)
    text_area.pack(side="left", fill="both", expand=True)

    # 3. Add each text area to the notebook.
    notebook.add(container, text=title)
    # 4. SELECT() would focus the current tab.
    notebook.select(container)

    # str(text_area) = .!frame.!notebook.!text
    # hash(content) gives the hash value of the data written in the tab.
    text_contents[str(text_area)] = hash(content)

    text_scroll = ttk.Scrollbar(container, orient="vertical", command=text_area.yview)
    text_scroll.pack(side="right", fill="y")
    text_area["yscrollcommand"] = text_scroll.set


def check_for_changes():
    current = get_text_widget()
    content = current.get("1.0", "end-1c")
    name = notebook.tab("current")["text"]

    if hash(content) != text_contents[str(current)]:
        if name[-1] != "*":
            notebook.tab("current", text=name + "*")
    elif name[-1] == "*":
        notebook.tab("current", text=name[:-1])


def close_current_tab():
    current = get_text_widget()
    if current_tab_unsaved() and not confirm_close():
        return

    if len(notebook.tabs()) == 1:
        create_file()

    notebook.forget(current)


def current_tab_unsaved():
    text_widget = get_text_widget()
    content = text_widget.get("1.0", "end-1c")

    return hash(content) != text_contents[str(text_widget)]

def confirm_close():
    return messagebox.askyesno(
            message="You have unsaved changes. Are you sure you want to close?",
            icon="question",
            title="Confirm close"
        )


def confirm_quit():
    unsaved = False

    for tab in notebook.tabs():
        tab_widget = root.nametowidget(tab)
        text_widget = tab_widget.winfo_children()[0]
        content = text_widget.get("1.0", "end-1c")

        if hash(content) != text_contents[str(text_widget)]:
            unsaved = True
            break

    if unsaved:
        confirm = confirm_close()

        if not confirm:
            return

    root.destroy()


def get_text_widget():
    tab_widget = root.nametowidget(notebook.select())
    text_widget = tab_widget.winfo_children()[0]
    return text_widget


def save_file():
    file_path = filedialog.asksaveasfilename()  # C:/Users/mayank.jain/Desktop/text.txt
    try:
        filename = os.path.basename(file_path)  # text.txt
        text_widget = get_text_widget()
        # "1.0" 1 is 1st line, 0 is 1st char. "end-1c" is the end except last char.
        content = text_widget.get("1.0", "end-1c")

        #  Write the content of the tab in the file.
        with open(file_path, "w") as file:
            file.write(content)

    except (AttributeError, FileNotFoundError):
        print("Save operation cancelled!")
        return

    #  "current" signifies the current selected tab in the Notebook.
    #  .tab() would replace the current tab name with the text that is being passed.
    notebook.tab("current", text=filename)
    text_contents[str(text_widget)] = hash(content)


def open_file():
    file_path = filedialog.askopenfilename()

    try:
        filename = os.path.basename(file_path)

        with open(file_path, "r") as file:
            content = file.read()

    except (AttributeError, FileNotFoundError):
        print("Open operation failed")
        return

    create_file(content, filename)


def show_about_info():
    messagebox.showinfo(
        title="About",
        message="A simple text editor designed to help you learn Tkinter"
    )


root = tk.Tk()
root.title("MJ Text Editor")
root.option_add("*tearOff", False)

# Create a frame in the root window.
# Everything inside this frame would be adjusted equally in GUI & it won't affect any other block outside the frame.
main = ttk.Frame(root)
main.pack(fill="both", expand=True, padx=1, pady=(4, 0))

# Create a menu bar.
menubar = tk.Menu()
root.config(menu=menubar)

# Create a drop down for the menu we just created. Also called cascading a menu.
# Here filemenu is another menu having label as "File" & tells the menubar to add as a dropdown.
file_menu = tk.Menu(menubar)
help_menu = tk.Menu(menubar)
menubar.add_cascade(menu=file_menu, label="File")
menubar.add_cascade(menu=help_menu, label="Help")

# Add a command to a particular menu which is going to execute some thing.
# accelerator is a short cut key for the menu.
file_menu.add_command(label="New", command=create_file, accelerator="Ctrl+N")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Exit", command=confirm_quit)
file_menu.add_command(label="Close Tab", command=close_current_tab, accelerator="Ctrl+Q")

help_menu.add_command(label="Help", command=show_about_info)
# The beginning...
# 1. Create Notebook which is a collection of tabs which has different elements inside it.
notebook = ttk.Notebook(main)
notebook.pack(fill="both", expand=True)
create_file()

# Bind the controls in the root with the particular event.
# Note here that lambda fn's are not executed below. They are called only when shortcut key is pressed.
root.bind("<Control-n>", lambda event: create_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())
root.bind("<KeyPress>", lambda event: check_for_changes())
root.bind("<Control-q>", lambda event: close_current_tab())

root.mainloop()
