import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox as mb
import speech_recognition as sr

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


def new_window():
    main()
    # Notification to alert the user
    mb.showinfo("Notification", "New Window Opened")


def shortcuts():
    # Notification of all of the shortcuts
    mb.showinfo("Notification", "Ctrl + N -> New File\nCtrl + O -> Open File\nCtrl + W -> Open New Window\nCtrl + S -> Save File\nCtrl + t -> Speech to Text")


def speech_to_text(text):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # Notification to alert the user
        mb.showinfo("Notification", "Speak now after closing the notification... With a pause you can stop the Speech to Text")
        audio = recognizer.listen(source)

        try:
            # Notification to alert the user
            mb.showinfo("Notification", "Translating your Speech to text")
            recognized_text = recognizer.recognize_google(audio)
            text.insert(tk.END, recognized_text)
        except sr.UnknownValueError:
            # Error message if the Speech Recognition couldn't understand the users speech/audio
            mb.showerror("Error", "Speech Recognition could not understand audio")
            return
        except sr.RequestError as e:
            # Error message if the request isn't handled by the server
            mb.showerror("Error", f"Could not request results from Speech Recognition service; {e}")


def toggle_dark_mode(window, text_editor, theme):
    # Toggle the theme between light and dark
    if theme[0] == "light":
        apply_dark_theme(window, text_editor)
        theme[0] = "dark"
    else:
        apply_light_theme(window, text_editor)
        theme[0] = "light"


def apply_dark_theme(window, text_editor):
    window.config(bg="#1e1e1e")
    text_editor.config(bg="#1e1e1e", fg="white", insertbackground="white")


def apply_light_theme(window, text_editor):
    window.config(bg="white")
    text_editor.config(bg="white", fg="black", insertbackground="black")


def zoom_in(text_editor, font_size):
    current_font_size = font_size[0]
    if current_font_size < font_size[2]:
        new_font_size = current_font_size + 2
        text_editor.config(font=("TkDefaultFont", new_font_size))
        font_size[0] = new_font_size


def zoom_out(text_editor, font_size):
    current_font_size = font_size[0]
    if current_font_size > font_size[1]:
        new_font_size = current_font_size - 2
        text_editor.config(font=("TkDefaultFont", new_font_size))
        font_size[0] = new_font_size


def main():
    window = tk.Tk()
    window.title("My Text-Editor")
    window.rowconfigure(0, minsize=500)
    window.columnconfigure(1, minsize=700)

    text_editor = tk.Text(window, font=("TkDefaultFont", 12))
    text_editor.grid(row=0, column=1)
    text_editor.pack(expand="yes", fill="both")

    current_theme = ["light"]

    # Current font size, minimum font size, maximum font size
    font_size = [12, 8, 16]

    menu_bar = tk.Menu(window)
    window.config(menu=menu_bar)

    # File menu
    file_menu = tk.Menu(menu_bar, tearoff=0, bd=2)
    view_menu = tk.Menu(menu_bar, tearoff=0, bd=2)
    help_menu = tk.Menu(menu_bar, tearoff=0, bd=2)

    menu_bar.add_cascade(label="File", menu=file_menu)
    menu_bar.add_cascade(label="View", menu=view_menu)
    menu_bar.add_cascade(label="Help", menu=help_menu)

    # File dropdown
    file_menu.add_command(label="New", command=lambda: new_file(window, text_editor))
    file_menu.add_command(label="Open", command=lambda: open_file(window, text_editor))
    file_menu.add_command(label="Open New Window", command=new_window)
    file_menu.add_command(label="Save", command=lambda: save_file(window, text_editor))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.destroy)

    # View dropdown
    view_menu.add_command(label="Toggle Dark Mode", command=lambda: toggle_dark_mode(window, text_editor, current_theme))
    view_menu.add_command(label="Zoom In", command=lambda: zoom_in(text_editor, font_size))
    view_menu.add_command(label="Zoom Out", command=lambda: zoom_out(text_editor, font_size))

    # Help dropdown
    help_menu.add_command(label="Keyboard Shortcuts", command=shortcuts)
    help_menu.add_command(label="Speech to Text", command=lambda: speech_to_text(text_editor))

    # Key binds for shortcuts
    window.bind("<Control-o>", lambda x: open_file(window, text_editor))
    window.bind("<Control-s>", lambda x: save_file(window, text_editor))
    window.bind("<Control-n>", lambda x: new_file(window, text_editor))
    window.bind("<Control-w>", lambda x: new_window())
    window.bind("<Control-p>", lambda x: speech_to_text(text_editor))
    window.bind("<Control-q>", lambda x: toggle_dark_mode(window, text_editor, current_theme))
    window.bind("<Control-=>", lambda x: zoom_in(text_editor, font_size))
    window.bind("<Control-minus>", lambda x: zoom_out(text_editor, font_size))

    window.mainloop()

main()
