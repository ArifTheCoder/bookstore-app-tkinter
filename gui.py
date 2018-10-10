from tkinter import *
import backend


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)

    entry_title.delete(0, END)
    entry_title.insert(END, selected_tuple[1])
    entry_author.delete(0, END)
    entry_author.insert(END, selected_tuple[2])
    entry_year.delete(0, END)
    entry_year.insert(END, selected_tuple[3])
    entry_ISBN.delete(0, END)
    entry_ISBN.insert(END, selected_tuple[4])


# view
def view_command():
    list1.delete(0, END)

    for row in backend.view():
        list1.insert(END, row)


# Search
def search_command():
    list1.delete(0, END)
    for row in backend.search(title_val.get(), author_val.get(), year_val.get(), isbn_val.get()):
        list1.insert(END, row)


# Add
def add_command():
    backend.insert(title_val.get(), author_val.get(), year_val.get(), isbn_val.get())
    list1.delete(0, END)
    list1.insert(END, (title_val.get(), author_val.get(), year_val.get(), isbn_val.get()))


# Delete
def delete_command():
    backend.delete(selected_tuple[0])


# Update
def update_command():
    backend.update(selected_tuple[0], title_val.get(), author_val.get(), year_val.get(), isbn_val.get())

window = Tk()

window.wm_title("Book Store")

label_title = Label(window, text='Title')
label_title.grid(row=0, column=0)

label_author = Label(window, text='Author')
label_author.grid(row=0, column=2)

label_year = Label(window, text='Year')
label_year.grid(row=1, column=0)

label_ISBN = Label(window, text='ISBN')
label_ISBN.grid(row=1, column=2)

title_val = StringVar()
entry_title = Entry(window, textvariable=title_val)
entry_title.grid(row=0, column=1)

author_val = StringVar()
entry_author = Entry(window, textvariable=author_val)
entry_author.grid(row=0, column=3)

year_val = StringVar()
entry_year = Entry(window, textvariable=year_val)
entry_year.grid(row=1, column=1)

isbn_val = StringVar()
entry_ISBN = Entry(window, textvariable=isbn_val)
entry_ISBN.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

view_btn = Button(window, text='View all', width=12, command=view_command)
view_btn.grid(row=2, column=3)

search_btn = Button(window, text='Search Entry', width=12, command=search_command)
search_btn.grid(row=3, column=3)

add_btn = Button(window, text='Add Entry', width=12, command=add_command)
add_btn.grid(row=4, column=3)

update_btn = Button(window, text='Update', width=12, command=update_command)
update_btn.grid(row=5, column=3)

delete_btn = Button(window, text='Delete', width=12, command=delete_command)
delete_btn.grid(row=6, column=3)

close_btn = Button(window, text='Close', width=12, command=window.destroy)
close_btn.grid(row=7, column=3)

window.mainloop()
