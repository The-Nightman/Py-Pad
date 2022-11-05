# pip install customtkinter

import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import webbrowser

open_file_name = False


def new_file(event=None):
    global open_file_name
    if tk.Event:
        open_file_name = False
        text_box.delete("1.0", "end")
        app.title("Untitled - Py Pad")
    else:
        open_file_name = False
        text_box.delete("1.0", "end")
        app.title("Untitled - Py Pad")


def open_file(event=None):
    global open_file_name
    if tk.Event:
        txt_file = filedialog.askopenfilename(initialdir="C:", title="Open File", filetypes=(
            ("Text Files", "*.txt"), ("All Files", "*.*")))
        if txt_file == "":
            txt_file = open_file_name
        if txt_file:
            open_file_name = txt_file
        title = txt_file.replace("\\", "/").split("/")
        app.title(f"{title[-1]} - Py Pad")
        txt_file = open(txt_file, "r")
        content = txt_file.read()
        text_box.delete("1.0", "end")
        text_box.insert("end", content)
    else:
        txt_file = filedialog.askopenfilename(initialdir="C:", title="Open File", filetypes=(
            ("Text Files", "*.txt"), ("All Files", "*.*")))
        if txt_file == "":
            txt_file = open_file_name
        if txt_file:
            open_file_name = txt_file
        title = txt_file.replace("\\", "/").split("/")
        app.title(f"{title[-1]} - Py Pad")
        txt_file = open(txt_file, "r")
        content = txt_file.read()
        text_box.delete("1.0", "end")
        text_box.insert("end", content)


def save_as(event=None):
    if tk.Event:
        txt_file = filedialog.asksaveasfilename(
            defaultextension=".*", initialdir="C:", title="Save As", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if txt_file:
            title = txt_file.replace("\\", "/").split("/")
            app.title(f"{title[-1]} - Py Pad")
            txt_file = open(txt_file, "w")
            txt_file.write(text_box.get("1.0", "end"))
            txt_file.close
    else:
        txt_file = filedialog.asksaveasfilename(
            defaultextension=".*", initialdir="C:", title="Save As", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if txt_file:
            title = txt_file.replace("\\", "/").split("/")
            app.title(f"{title[-1]} - Py Pad")
            txt_file = open(txt_file, "w")
            txt_file.write(text_box.get("1.0", "end"))
            txt_file.close


def save(event=None):
    global open_file_name
    if tk.Event:
        if open_file_name:
            txt_file = open(open_file_name, "w")
            txt_file.write(text_box.get("1.0", "end"))
            txt_file.close
        else:
            save_as()
    else:
        if open_file_name:
            txt_file = open(open_file_name, "w")
            txt_file.write(text_box.get("1.0", "end"))
            txt_file.close
        else:
            save_as()


def cut_text():
    global text_select
    if tk.Event:
        text_select = app.clipboard_get()
    else:
        if text_box.selection_get():
            text_select = text_box.selection_get()
            text_box.delete("sel.first", "sel.last")
            app.clipboard_clear()
            app.clipboard_append()


def copy_text():
    global text_select
    if tk.Event:
        text_select = app.clipboard_get()
    if text_box.selection_get():
        text_select = text_box.selection_get()
        app.clipboard_clear()
        app.clipboard_append()


def paste_text():
    global text_select
    if tk.Event:
        text_select = app.clipboard_get()
    else:
        cursor_pos = text_box.index(tk.INSERT)
        text_box.insert(cursor_pos, text_select)


def toggle_wrap():
    if text_box["wrap"] == "word":
        text_box.configure(wrap="none")
    else:
        text_box.configure(wrap="word")


def create_about_window():
    global about_image
    about_window = tk.Toplevel(app)
    about_window.geometry(f"{350}x{220}")
    about_window.title("About Py Pad")
    about_window.resizable(False, False)
    about_window.transient(app)
    about_window_button = ctk.CTkButton(
        about_window, text="OK", relief="groove", corner_radius=3, command=about_window.destroy)
    about_window_button.pack(side="bottom", anchor="e", padx=10, pady=10)
    about_image = tk.PhotoImage(file="Python\\Py-Pad\\thenightman.png")
    about_image_container = ctk.CTkLabel(
        about_window, image=about_image)
    about_image_container.pack(pady="15")
    about_text = ctk.CTkLabel(
        about_window, text_color="black", text="Py Pad designed and written by The Nightman")
    about_text.pack(pady="0")
    about_text_link = tk.Label(
        about_window, fg="blue", cursor="hand2", text="https://github.com/The-Nightman")
    about_text_link.bind(
        "<Button-1>", lambda x: webbrowser.open_new("https://github.com/The-Nightman"))
    about_text_link.pack(pady="5")
    about_window.grab_set()


ctk.set_appearance_mode("light")

app = ctk.CTk()
app.geometry(f"{800}x{700}")
app.title("Untitled - Py Pad")

frame = ctk.CTkFrame(app)
frame.pack(fill="both", expand=True)

text_scroll_y = ctk.CTkScrollbar(frame, corner_radius=7)
text_scroll_x = ctk.CTkScrollbar(
    frame, corner_radius=7, orientation="horizontal")
text_scroll_y.pack(side="right", fill="y")
text_scroll_x.pack(side="bottom", fill="x")

text_box = tk.Text(frame, wrap="none", font=("Helvetica", 11),
                   selectbackground="#33b1ff", selectforeground="black", undo=True, yscrollcommand=text_scroll_y.set, xscrollcommand=text_scroll_x.set)
text_box.pack(fill="both", expand=True)

text_scroll_y.configure(command=text_box.yview)
text_scroll_x.configure(command=text_box.xview)

menu_widget = tk.Menu(app)
app.config(menu=menu_widget)

file_menu = tk.Menu(menu_widget, tearoff=False)
menu_widget.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", accelerator="Ctrl+n",
                      command=lambda: new_file())
file_menu.add_command(label="Open...", accelerator="Ctrl+o",
                      command=lambda: open_file())
file_menu.add_command(label="Save", accelerator="Ctrl+s",
                      command=lambda: save())
file_menu.add_command(label="Save As...",
                      accelerator="Ctrl+Shift+s", command=lambda: save_as())
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)

edit_menu = tk.Menu(menu_widget, tearoff=False)
menu_widget.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", accelerator="Ctrl+z",
                      command=text_box.edit_undo)
edit_menu.add_separator()
edit_menu.add_command(label="Redo", accelerator="Ctrl+y",
                      command=text_box.edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", accelerator="Ctrl+x",
                      command=lambda: cut_text())
edit_menu.add_command(label="Copy", accelerator="Ctrl+c",
                      command=lambda: copy_text())
edit_menu.add_command(label="Paste", accelerator="Ctrl+v",
                      command=lambda: paste_text())

format_menu = tk.Menu(menu_widget, tearoff=False)
menu_widget.add_cascade(label="Format", menu=format_menu)
format_menu.add_checkbutton(label="Text Wrapping",
                            command=lambda: toggle_wrap())
format_menu.add_command(label="Font...")

help_menu = tk.Menu(menu_widget, tearoff=False)
menu_widget.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About Py Pad", command=create_about_window)

context_bar = ctk.CTkLabel(app, text="test", anchor="e", height=22)
context_bar.pack(side="bottom", fill="x")

app.bind("<Control-Key-x>", cut_text)
app.bind("<Control-Key-c>", copy_text)
app.bind("<Control-Key-v>", paste_text)
app.bind("<Control-Key-s>", save)
app.bind("<Control-Key-n>", new_file)
app.bind("<Control-Key-o>", open_file)
app.bind("<Control-Key-S>", save_as)

app.mainloop()
