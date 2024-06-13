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
    # Notification containing all of the shortcuts
    mb.showinfo("Notification", "Ctrl + N -> New File\nCtrl + O -> Open File\nCtrl + W -> Open New Window\nCtrl + S -> Save File\nCtrl + t -> Speech to Text") 


def speech_to_text(text):
    recogniser = sr.Recognizer()
    with sr.Microphone() as source:
        # Notification to alert the user
        mb.showinfo("Notification", "Speak now after closing the notification... With a pause you can stop the Speech to Text")
        audio = recogniser.listen(source)

        try:
            mb.showinfo("Notification", "Translating your Speech to text")
            recognised_text = recogniser.recognize_google(audio)
            text.insert(tk.END, recognised_text)

        except sr.UnknownValueError:
            # Error message if the Speech Regonition couldn't understand the users speech/audio
            mb.showerror("Error", "Speech Recognition could not understand audio")
            return
        except sr.RequestError as e:
            # Error message if the request isn't handled by the server
            mb.showerror("Error", f"Could not request results from Speech Recognition service; {e}")


def main():
    window = tk.Tk()

    window.title("My Text-Editor")
    window.rowconfigure(0, minsize=500)
    window.columnconfigure(1, minsize=700)

    text_editor = tk.Text(window)
    text_editor.grid(row=0, column=1)
    text_editor.pack(expand="yes", fill="both")

    # File-menu
    menu_bar = tk.Menu(window)
    window.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0, bd=2)
    help_menu = tk.Menu(menu_bar, tearoff=0, bd=2)

    menu_bar.add_cascade(label="File", menu=file_menu)
    menu_bar.add_cascade(label="Help", menu=help_menu)

    file_menu.add_command(label="New", command=lambda: new_file(window, text_editor))
    file_menu.add_command(label="Open", command=lambda: open_file(window, text_editor))
    file_menu.add_command(label="Open New Window", command=lambda: new_window())
    file_menu.add_command(label="Save", command=lambda: save_file(window, text_editor))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.destroy)

    help_menu.add_command(label="Keyboard Shortcuts", command=lambda: shortcuts())
    help_menu.add_command(label="Speech to Text", command=lambda: speech_to_text(text_editor))

    # Key binds for shortcuts
    window.bind("<Control-o>", lambda x: open_file(window, text_editor))
    window.bind("<Control-s>", lambda x: save_file(window, text_editor))
    window.bind("<Control-n>", lambda x: new_file(window, text_editor))
    window.bind("<Control-w>", lambda x: new_window())
    window.bind("<Control-t>", lambda x: speech_to_text(text_editor))

    window.mainloop()

main()
