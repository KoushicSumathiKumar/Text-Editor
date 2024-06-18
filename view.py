def toggle_dark_mode(window, text_editor, theme):
    # Toggle the theme between light and dark using the methods below
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
