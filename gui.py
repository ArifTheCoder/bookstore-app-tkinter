from tkinter import *
import backend

window = Tk()

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

view_btn = Button(window, text='View all', width=12)
view_btn.grid(row=2, column=3)

search_btn = Button(window, text='Search Entry', width=12)
search_btn.grid(row=3, column=3)

add_btn = Button(window, text='Add Entry', width=12)
add_btn.grid(row=4, column=3)

update_btn = Button(window, text='Update', width=12)
update_btn.grid(row=5, column=3)

delete_btn = Button(window, text='Delete', width=12)
delete_btn.grid(row=6, column=3)

close_btn = Button(window, text='Close', width=12)
close_btn.grid(row=7, column=3)

window.mainloop()