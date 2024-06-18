import tkinter as tk
from tkinter import messagebox as mb
import view
import file
import help

def new_window():
    main()
    # Notification to alert the user
    mb.showinfo("Notification", "New Window Opened")

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
    file_menu.add_command(label="New", command=lambda: file.new_file(window, text_editor))
    file_menu.add_command(label="Open", command=lambda: file.open_file(window, text_editor))
    file_menu.add_command(label="Open New Window", command=new_window)
    file_menu.add_command(label="Save", command=lambda: file.save_file(window, text_editor))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.destroy)

    # View dropdown
    view_menu.add_command(label="Toggle Theme", command=lambda: view.toggle_dark_mode(window, text_editor, current_theme))
    view_menu.add_command(label="Zoom In", command=lambda: view.zoom_in(text_editor, font_size))
    view_menu.add_command(label="Zoom Out", command=lambda: view.zoom_out(text_editor, font_size))

    # Help dropdown
    help_menu.add_command(label="Keyboard Shortcuts", command=help.shortcuts)
    help_menu.add_command(label="Speech to Text", command=lambda: help.speech_to_text(text_editor))

    # Key binds for shortcuts
    window.bind("<Control-o>", lambda x: file.open_file(window, text_editor))
    window.bind("<Control-s>", lambda x: file.save_file(window, text_editor))
    window.bind("<Control-n>", lambda x: file.new_file(window, text_editor))
    window.bind("<Control-w>", lambda x: new_window())
    window.bind("<Control-p>", lambda x: help.speech_to_text(text_editor))
    window.bind("<Control-q>", lambda x: view.toggle_dark_mode(window, text_editor, current_theme))
    window.bind("<Control-=>", lambda x: view.zoom_in(text_editor, font_size))
    window.bind("<Control-minus>", lambda x: view.zoom_out(text_editor, font_size))

    window.mainloop()

main()
