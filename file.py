import tkinter as tk
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window, text):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return
    # "1.0" -> "1" = 1st line and "0" means 1st column
    # "tk.END" means the end of the file
    text.delete(1.0, tk.END)
    with open(filepath, "r") as file:
        content = file.read()
        text.insert(tk.END, content)

    window.title(filepath)
    # Notification to alert the user
    mb.showinfo("Notification", "File Opened")


def save_file(window, text):
    filepath = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return

    # "1.0" -> "1" = 1st line and "0" means 1st column
    # "tk.END" means the end of the file
    with open(filepath, "w") as file:
        content = text.get(1.0, tk.END)
        file.write(content)

    window.title(filepath)
    # Notification to alert the user
    mb.showinfo("Notification", "File Saved")


def new_file(window, text):

    # options to save their current file
    save_or_no = mb.askquestion("Notification", "Would you like to save the current file?")
    if save_or_no == "yes":
        save_file(window, text)

    # "1.0" -> "1" = 1st line and "0" means 1st column
    # "tk.END" means the end of the file
    text.delete("1.0", tk.END)
    window.title("New File")

    # Notification to alert the user
    mb.showinfo("Notification", "New File Opened")


