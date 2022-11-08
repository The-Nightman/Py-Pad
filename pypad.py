# pip install customtkinter

import tkinter.font
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import webbrowser

open_file_name = False

f_size_list = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]
f_style_list = [
    "normal roman",
    "normal italic",
    "bold roman",
    "bold italic"
]

default_font, default_style, default_size = "Consolas", "normal roman", 11
current_font, current_style, current_size = default_font, default_style, default_size
sample_font, sample_style, sample_size = current_font, current_style, current_size


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


def update_font_list(data):
    font_list.delete(0, "end")
    for item in data:
        font_list.insert("end", item)


def update_style_list(data):
    font_style_list.delete(0, "end")
    for item in data:
        font_style_list.insert("end", item)


def update_size_list(data):
    font_size_list.delete(0, "end")
    for item in data:
        font_size_list.insert("end", item)


def entry_fill_font(event):
    global sample_font
    font_entry.delete(0, "end")
    list_selection = font_list.curselection()
    font_entry.insert(0, font_list.get(list_selection[0]))
    sample_font = str(font_entry.get())
    update_sample()


def entry_fill_style(event):
    global sample_style
    font_style_entry.delete(0, "end")
    list_selection = font_style_list.curselection()
    font_style_entry.insert(0, font_style_list.get(list_selection[0]))
    sample_style = str(font_style_entry.get())
    update_sample()


def entry_fill_size(event):
    global sample_size
    font_size_entry.delete(0, "end")
    list_selection = font_size_list.curselection()
    font_size_entry.insert(0, font_size_list.get(list_selection[0]))
    sample_size = int(font_size_entry.get())
    update_sample()


def update_sample():
    sample_text.configure(font=(sample_font, sample_size, sample_style))


def update_format():
    global current_font
    global current_style
    global current_size
    current_font = sample_font
    current_style = sample_style
    current_size = sample_size
    text_box.configure(font=(current_font, current_size, current_style))
    font_window.destroy()


def cancel_format():
    global sample_font
    global sample_style
    global sample_size
    sample_font = current_font
    sample_style = current_style
    sample_size = current_size
    font_window.destroy()


def autofill_font(event):
    entry = font_entry.get()

    if entry == "":
        data = f_list
    else:
        data = []
        for item in f_list:
            if entry.lower() in item.lower():
                data.append(item)
    update_font_list(data)


def font_size_type(event):
    global sample_size
    sample_size = font_size_entry.get()
    sample_text.configure(font=(sample_font, sample_size))


def create_about_window():
    global about_image
    about_window = tk.Toplevel(app)
    about_window.geometry(f"{350}x{220}")
    about_window.title("About Py Pad")
    about_window.resizable(False, False)
    about_window.transient(app)
    about_window_button = ctk.CTkButton(
        about_window, text="OK", corner_radius=3, width=100, command=about_window.destroy)
    about_window_button.pack(side="bottom", anchor="e", padx=10, pady=10)
    about_image = tk.PhotoImage(file="Python\\Py-Pad\\thenightman.png")
    about_image_container = ctk.CTkLabel(about_window, image=about_image)
    about_image_container.pack(pady="15")
    about_text = ctk.CTkLabel(about_window, text_color="black",
                              text="Py Pad designed and written by The Nightman")
    about_text.pack(pady="0")
    about_text_link = tk.Label(
        about_window, fg="blue", cursor="hand2", text="https://github.com/The-Nightman")
    about_text_link.bind(
        "<Button-1>", lambda x: webbrowser.open_new("https://github.com/The-Nightman"))
    about_text_link.pack(pady="5")
    about_window.grab_set()


def create_font_window():
    global font_window
    global font_entry
    global font_style_entry
    global font_size_entry
    global font_list
    global font_style_list
    global font_size_list
    global sample_text
    global f_list
    font_window = tk.Toplevel(app)
    font_window.geometry(f"{427}x{440}")
    font_window.title("Font")
    font_window.resizable(False, False)
    font_window.transient(app)
    font_window.grab_set()
    font_button_frame = tk.Frame(font_window, width=210)
    font_button_frame.pack(side="bottom", anchor="e", pady=10)
    font_window_button_close = ctk.CTkButton(
        font_button_frame, text="Cancel", corner_radius=3, width=100, command=cancel_format)
    font_window_button = ctk.CTkButton(
        font_button_frame, text="OK", corner_radius=3, width=100, command=update_format)
    font_window_button_close.pack(side="right", padx=10)
    font_window_button.pack(side="left")

    sample_frame = tk.Frame(font_window, width=250, height=80,
                            highlightbackground="grey", highlightthickness=1)
    sample_frame.pack(side="bottom", anchor="e", pady=15, padx=15)
    sample_frame.pack_propagate(False)
    sample_label = tk.Label(sample_frame, text="Sample")
    sample_label.pack(side="top", anchor="nw")
    sample_text = tk.Label(sample_frame, text="AaBbYyZz", font=(
        sample_font, sample_size, sample_style))
    sample_text.pack()

    font_frame = ctk.CTkFrame(font_window, width=172)
    font_frame.pack(side="left", anchor="n", pady=30, padx=11)
    font_style_frame = ctk.CTkFrame(font_window, width=130)
    font_style_frame.pack(side="left", anchor="n", pady=30, padx=4)
    font_size_frame = ctk.CTkFrame(font_window, width=74)
    font_size_frame.pack(side="right", anchor="n", pady=30, padx=15)

    font_label = tk.Label(font_frame, text="Font")
    font_label.pack(side="top", anchor="nw")
    font_entry = tk.Entry(font_frame)
    font_entry.insert("end", current_font)
    font_entry.pack(side="top", fill="x")
    font_scroll_y = ctk.CTkScrollbar(
        font_frame, width=18, orientation="vertical")
    font_list = tk.Listbox(font_frame, width=25,
                           yscrollcommand=font_scroll_y.set)
    font_list.configure(exportselection=False)
    font_list.pack(side="left", fill="y")
    font_scroll_y.pack(side="right", anchor="e", fill="both")
    font_scroll_y.configure(command=font_list.yview)
    f_list = tkinter.font.families()
    update_font_list(f_list)

    font_style_label = tk.Label(font_style_frame, text="Font style:")
    font_style_label.pack(side="top", anchor="nw")
    font_style_entry = tk.Entry(font_style_frame)
    font_style_entry.insert("end", current_style)
    font_style_entry.pack(side="top", fill="x")
    font_style_scroll_y = ctk.CTkScrollbar(
        font_style_frame, width=18, orientation="vertical")
    font_style_list = tk.Listbox(
        font_style_frame, width=18, yscrollcommand=font_style_scroll_y.set)
    font_style_list.configure(exportselection=False)
    font_style_list.pack(side="left", fill="y")
    font_style_scroll_y.pack(side="right", anchor="e", fill="both")
    font_style_scroll_y.configure(command=font_style_list.yview)
    update_style_list(f_style_list)

    font_size_label = tk.Label(font_size_frame, text="Size:")
    font_size_label.pack(side="top", anchor="nw")
    font_size_entry = tk.Entry(font_size_frame)
    font_size_entry.insert("end", current_size)
    font_size_entry.pack(side="top", fill="x")
    font_size_scroll_y = ctk.CTkScrollbar(
        font_size_frame, width=18, orientation="vertical")
    font_size_list = tk.Listbox(
        font_size_frame, width=7, yscrollcommand=font_size_scroll_y.set)
    font_size_list.configure(exportselection=False)
    font_size_list.pack(side="left", fill="y")
    font_size_scroll_y.pack(side="right", anchor="e", fill="both")
    font_size_scroll_y.configure(command=font_size_list.yview)
    update_size_list(f_size_list)

    font_list.bind("<<ListboxSelect>>", entry_fill_font)
    font_style_list.bind("<<ListboxSelect>>", entry_fill_style)
    font_size_list.bind("<<ListboxSelect>>", entry_fill_size)
    font_entry.bind("<KeyRelease>", autofill_font)
    font_size_entry.bind("<KeyRelease>", font_size_type)


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

text_box = tk.Text(frame, wrap="none", font=(current_font, current_size, current_style), selectbackground="#33b1ff",
                   selectforeground="black", undo=True, yscrollcommand=text_scroll_y.set, xscrollcommand=text_scroll_x.set)
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
format_menu.add_command(label="Font...", command=create_font_window)

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
