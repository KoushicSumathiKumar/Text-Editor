import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox as mb


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
    tk.messagebox.showinfo("Notification","File Opened") 


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
    tk.messagebox.showinfo("Notification", "File Saved") 

def new_file(window, text):
    save_or_no=mb.askquestion("Notification", "Would you like to save the current file?")
    if save_or_no == "yes" :
        save_file(window, text)

    # "1.0" -> "1" = 1st line and "0" means 1st column
    # "tk.END" means the end of the file
    text.delete("1.0", tk.END)
    window.title("New File")

    # Notification to alert the user
    tk.messagebox.showinfo("Notification","New File Opened")

def new_window():
    main() 


def main():
    window = tk.Tk()

    window.title("My Text-Editor")
    window.rowconfigure(0, minsize=500)
    window.columnconfigure(1, minsize=700)

    text_editor = tk.Text(window)
    text_editor.grid(row=0, column=1)
    text_editor.pack(expand="yes", fill="both")


    # relief=tk.RAISED is to give 3D Effect
    # frame = tk.Frame(window, relief=tk.RAISED,bd=2)

    # File-menu
    menu_bar = tk.Menu(window)
    window.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)

    file_menu.add_command(label="New", command=lambda: new_file(window, text_editor))
    file_menu.add_command(label="Open", command=lambda: open_file(window, text_editor))
    file_menu.add_command(label="Open New Window", command=lambda: new_window())
    file_menu.add_command(label="Save", command=lambda: save_file(window, text_editor))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.destroy)


    # Key binds for shortcuts
    window.bind("<Control-o>", lambda x: open_file(window, text_editor))
    window.bind("<Control-s>", lambda x: save_file(window, text_editor))
    window.bind("<Control-n>", lambda x: new_file(window, text_editor))
    window.bind("<Control-w>", lambda x: new_window())



    window.mainloop()

main()