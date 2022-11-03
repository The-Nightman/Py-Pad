# pip install customtkinter

import customtkinter
import tkinter
from tkinter import filedialog

customtkinter.set_appearance_mode("light")

app = customtkinter.CTk()
app.geometry(f"{800}x{700}")
app.title("Untitled - Py Pad")

open_file_name = False


def new_file():
    global open_file_name
    open_file_name = False
    text_box.delete("1.0", "end")
    app.title("Untitled - Py Pad")


def open_file():
    txt_file = filedialog.askopenfilename(initialdir="C:", title="Open File", filetypes=(
        ("Text Files", "*.txt"), ("All Files", "*.*")))
    if txt_file:
        global open_file_name
        open_file_name = txt_file
    title = txt_file.replace("\\", "/").split("/")
    app.title(f"{title[-1]} - Py Pad")
    txt_file = open(txt_file, "r")
    content = txt_file.read()
    text_box.delete("1.0", "end")
    text_box.insert("end", content)


def save_as():
    txt_file = filedialog.asksaveasfilename(
        defaultextension=".*", initialdir="C:", title="Save As", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if txt_file:
        title = txt_file.replace("\\", "/").split("/")
        app.title(f"{title[-1]} - Py Pad")
        txt_file = open(txt_file, "w")
        txt_file.write(text_box.get("1.0", "end"))
        txt_file.close


def save():
    global open_file_name
    if open_file_name:
        txt_file = open(open_file_name, "w")
        txt_file.write(text_box.get("1.0", "end"))
        txt_file.close
    else:
        save_as()


def cut_text():
    global text_select
    if tkinter.Event:
        text_select = app.clipboard_get()
    else:
        if text_box.selection_get():
            text_select = text_box.selection_get()
            text_box.delete("sel.first", "sel.last")
            app.clipboard_clear()
            app.clipboard_append()


def copy_text():
    global text_select
    if tkinter.Event:
        text_select = app.clipboard_get()
    if text_box.selection_get():
        text_select = text_box.selection_get()
        app.clipboard_clear()
        app.clipboard_append()


def paste_text():
    global text_select
    if tkinter.Event:
        text_select = app.clipboard_get()
    else:
        cursor_pos = text_box.index(tkinter.INSERT)
        text_box.insert(cursor_pos, text_select)


frame = customtkinter.CTkFrame(app)
frame.pack(fill="both", expand=True)

text_scroll_y = customtkinter.CTkScrollbar(frame, corner_radius=7)
text_scroll_x = customtkinter.CTkScrollbar(
    frame, corner_radius=7, orientation="horizontal")
text_scroll_y.pack(side="right", fill="y")
text_scroll_x.pack(side="bottom", fill="x")

text_box = tkinter.Text(frame, wrap="none", font=("Helvetica", 11),
                                    selectbackground="#00ffff", selectforeground="black", undo=True, yscrollcommand=text_scroll_y.set, xscrollcommand=text_scroll_x.set)
text_box.pack(fill="both", expand=True)

text_scroll_y.configure(command=text_box.yview)
text_scroll_x.configure(command=text_box.xview)

menu_widget = tkinter.Menu(app)
app.config(menu=menu_widget)

file_menu = tkinter.Menu(menu_widget, tearoff=False)
menu_widget.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", accelerator="Ctrl+n", command=new_file)
file_menu.add_command(label="Open...", accelerator="Ctrl+o", command=open_file)
file_menu.add_command(label="Save", accelerator="Ctrl+s", command=save)
file_menu.add_command(label="Save As...",
                      accelerator="Ctrl+Shift+s", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)

edit_menu = tkinter.Menu(menu_widget, tearoff=False)
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

format_menu = tkinter.Menu(menu_widget, tearoff=False)
menu_widget.add_cascade(label="Format", menu=format_menu)
format_menu.add_command(label="Text Wrapping")
format_menu.add_command(label="Font...")

help_menu = tkinter.Menu(menu_widget, tearoff=False)
menu_widget.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About Py Pad")

context_bar = customtkinter.CTkLabel(app, text="test", anchor="e", height=22)
context_bar.pack(side="bottom", fill="x")

app.bind("<Control-Key-x>", cut_text)
app.bind("<Control-Key-c>", copy_text)
app.bind("<Control-Key-v>", paste_text)

app.mainloop()
