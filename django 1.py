from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')

#create functions for buttons / clickable in console

def populate_list():
    for row in db.fetch():
        # organiser_list.delete(0, END)
        # organiser_list.insert(END, row)
        return row

def add_item():
    if data_text.get()=='' or weight_text.get()==''or sleep_text.get()==''or food_text.get()=='':
        messagebox.showerror('Required fields', 'Заполните все поля')
        return

    db.insert(data_text.get(),weight_text.get(),sleep_text.get(),food_text.get())
    organiser_list.delete(0, END)
    organiser_list.insert(END,(data_text.get(),weight_text.get(),sleep_text.get(),food_text.get()))
    clear_text()
    populate_list()
#give data any time when it is selected
def select_item(event):
    try:
        global selected_item
        index = organiser_list.curselection()[0]
        selected_item = organiser_list.get(index)
    #delete the entry and insert it
        data_entry.delete(0,END)
        data_entry.insert(END,selected_item[1])
        weight_entry.delete(0, END)
        weight_entry.insert(END, selected_item[2])
        sleep_entry.delete(0, END)
        sleep_entry.insert(END, selected_item[3])
        food_entry.delete(0, END)
        food_entry.insert(END, selected_item[4])
    except IndexError:
        pass

def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def update_item():
    db.update(selected_item[0],data_text.get(),weight_text.get(),sleep_text.get(),food_text.get())
    populate_list()


def clear_text():
    data_entry.delete(0, END)
    weight_entry.delete(0, END)
    sleep_entry.delete(0, END)
    food_entry.delete(0, END)


#Create window object
app = Tk()
#Creating StringVar object (part)to manipulate values of widgets
data_text = StringVar()
data_label = Label(app, text='Дата:', font =('bold', 12), bg='light blue', pady=30)
data_label.grid(row=0,column=0, sticky='w')
data_entry = Entry(app, textvariable=data_text)
data_entry.grid(row=0,column=1, sticky=W)
#weight
weight_text = StringVar()
weight_label = Label(app, text='Вес:', font =('bold', 12), bg='light blue',pady=30)
weight_label.grid(row=1,column=0, sticky=W)
weight_entry = Entry(app, textvariable=weight_text)
weight_entry.grid(row=1,column=1, sticky=W)
#sleep_hours
sleep_text = StringVar()
sleep_label = Label(app, text='Сон:', font =('bold', 12), bg='light blue',pady=30 )
sleep_label.grid(row=0,column=2, sticky=W)
sleep_entry = Entry(app, textvariable=sleep_text)
sleep_entry.grid(row=0,column=3, sticky=W)
#food
food_text = StringVar()
food_label = Label(app, text='Приём пищи:', font =('bold', 12), bg='light blue',pady=30)
food_label.grid(row=1,column=2, sticky=W)
food_entry = Entry(app, textvariable=food_text)
food_entry.grid(row=1,column=3, sticky=W)
#organiser list(listbox) #columnspan makes a table kind of html
organiser_list =Listbox(app,height=8,width=50,bg='light blue',border=0)
organiser_list.grid(row=3,column=0,columnspan=3,rowspan=6,pady=20,padx=20)
#create scrollbar
scrollbar=Scrollbar(app)
scrollbar.grid(row=3,column=3)
#connect scrollbar to listbox
organiser_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=organiser_list.yview)
#bind select
organiser_list.bind('<<ListboxSelect>>',select_item)

#add buttons
add_button=Button(app, text='Добавить',width=14,command=add_item)
add_button.grid(row=2,column=0,pady=20)

remove_button=Button(app, text='Удалить',width=14,command=remove_item)
remove_button.grid(row=2,column=1)

update_button=Button(app, text='Обновить',width=14,command=update_item)
update_button.grid(row=2,column=2)

clear_button=Button(app, text='Очистить',width=14,command=clear_text)
clear_button.grid(row=2,column=3)


#populate data
populate_list()


#Giving a title
app.title('My organiser')
#Size and color of the background
app.configure(bg='light blue')
app.geometry('650x400')

#Start programm
app.mainloop()




















