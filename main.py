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


    # relief=tk.RAISED is to give 3D Effect
    frame = tk.Frame(window, relief=tk.RAISED,bd=2)


    open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_editor))
    save_button = tk.Button(frame, text="Save", command=lambda: save_file(window, text_editor))
    new_button = tk.Button(frame, text="New File", command=lambda: new_file(window, text_editor))
    new_window_button = tk.Button(frame, text="New Window", command=lambda: new_window())




    open_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    save_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    new_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    new_window_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

    frame.grid(row=0, column=0, sticky="ns")

    # Key binds for shortcuts
    window.bind("<Control-o>", lambda x: open_file(window, text_editor))
    window.bind("<Control-s>", lambda x: save_file(window, text_editor))
    window.bind("<Control-n>", lambda x: new_file(window, text_editor))
    window.bind("<Control-w>", lambda x: new_window())



    window.mainloop()

main()