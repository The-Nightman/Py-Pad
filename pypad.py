import customtkinter
import tkinter

customtkinter.set_appearance_mode("light")

app = customtkinter.CTk()
app.geometry(f"{800}x{700}")
app.title("Py Pad")

frame = customtkinter.CTkFrame(app)
frame.pack(fill="both", expand=True)

text_scroll_y = customtkinter.CTkScrollbar(frame, corner_radius=7)
text_scroll_x = customtkinter.CTkScrollbar(
    frame, corner_radius=7, orientation="horizontal")
text_scroll_y.pack(side="right", fill="y")
text_scroll_x.pack(side="bottom", fill="x")


text_box = customtkinter.CTkTextbox(frame, wrap="none", text_font=("Helvetica", 11), text_color="black",
                                    selectbackground="#00ffff", selectforeground="black", undo=True, corner_radius=0, yscrollcommand=text_scroll_y.set, xscrollcommand=text_scroll_x.set)
text_box.pack(fill="both", expand=True)

text_scroll_y.configure(command=text_box.yview)
text_scroll_x.configure(command=text_box.xview)

menu_widget = tkinter.Menu(app)
app.config(menu=menu_widget)

file_menu = tkinter.Menu(menu_widget, tearoff=False)
menu_widget.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit")

edit_menu = tkinter.Menu(menu_widget, tearoff=False)
menu_widget.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

app.mainloop()
