import tkinter as tk
import tkinter.font as tkFont
import re
import datetime
from PIL import ImageTk, Image
# изображение и красота окна
BACKGROUND_COLOR = 'light gray'
FAMILY_FONT = "deep sky blue"
WINDOW_SIZE = '350x500'
WINDOW_ICON = "icon/logo.ico"
INCOME_VALUE = 0
CATEGORY_L = []

with open('list.txt') as file:
    temp = file.read()
    CATEGORY_L = temp.split()



# функции
def push_income() -> int:
    global INCOME_VALUE
    temp = income_entry.get()
    if temp and temp.isdigit():
        income_label['text'] = 'Your income'
        INCOME_VALUE = income_entry.get()
        print(INCOME_VALUE)
    else:
        income_label['text'] = 'You did not enter a value'
    return INCOME_VALUE


def add_category():
    category_listbox.insert('end', entry_category.get())
    entry_category.delete(0, 'end')
    f = open('list.txt', 'w')
    f.writelines("\n".join(category_listbox.get(0, 'end')))
    f.close()


def delete_category():
    select = list(category_listbox.curselection())
    select.reverse()
    for i in select:
        category_listbox.delete(i)
    f = open('list.txt', 'w')
    f.writelines("\n".join(category_listbox.get(0, 'end')))
    f.close()

def clear_category():
    category_listbox.delete(0, 'end')
    f = open('list.txt', 'w')
    f.writelines("\n".join(category_listbox.get(0, 'end')))
    f.close()

# рабочая область
root = tk.Tk()
root.title('Calculation of expenses')
root.geometry(WINDOW_SIZE)
root.iconbitmap(WINDOW_ICON)
root.configure(bg=BACKGROUND_COLOR)

fontTitle = tkFont.Font(family=FAMILY_FONT, size=16, weight="bold", slant="italic")
fontTitle2 = tkFont.Font(family=FAMILY_FONT, size=10, weight="bold")
title_label = tk.Label(root, text='Calculation of expenses', font=fontTitle, bg=BACKGROUND_COLOR)
title_label.pack()

income_label = tk.Label(root, text='Your income', bg=BACKGROUND_COLOR)
income_label.pack()
income_entry = tk.Entry(root, width=20, bg=BACKGROUND_COLOR)
income_entry.pack()

income_push_button = tk.Button(root, text='PUSH', width=10, height=1, bg=BACKGROUND_COLOR, command=push_income)
income_push_button.pack(pady=20)

category_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
category_frame.pack(side='top')
category_label = tk.Label(category_frame, text='Category', bg=BACKGROUND_COLOR, font=fontTitle2)
category_label.pack(side='top')

category_listbox = tk.Listbox(category_frame, selectmode='extended', height=7)
category_listbox.pack(side='left')

frame_button = tk.Frame(category_frame, bg=BACKGROUND_COLOR)
frame_button.pack(side='right')

entry_category = tk.Entry(frame_button, width=15)
entry_category.pack(pady=2)
button_category_add = tk.Button(frame_button, text='Add', width=12, bg=BACKGROUND_COLOR, command=add_category)
button_category_add.pack(padx=10, pady=2)
button_category_delete = tk.Button(frame_button, text='Delete', width=12, bg=BACKGROUND_COLOR, command=delete_category)
button_category_delete.pack(padx=10, pady=2)
button_category_clear = tk.Button(frame_button, text='Clear', width=12, bg=BACKGROUND_COLOR, command=clear_category)
button_category_clear.pack(padx=10, pady=2)


for category in CATEGORY_L:
    category_listbox.insert(0, category)






root.mainloop()