import tkinter as tk
from tkinter.ttk import Combobox
import re
import datetime
window_boss = tk.Tk()
window_y = 600
window_boss.geometry(f'600x{window_y}')
window_boss.title('Расходы')
label_money = tk.Label(window_boss, text=f'ваш доход: {open("bank_money.txt").read()}', font=('Comic', 14))
label_money.place(x=225, y=0)
spisok = Combobox(window_boss)
spisok['values'] = [1, 2, 3, 4, 'Hello']
spisok.place(x=225, y=150)

def money_button():
    global money_new
    with open("bank_money.txt", 'w') as basa_name:
        basa_name.write(money_new.get())
        label_money["text"] = f'ваш доход: {money_new.get()}'
        print(spisok.get())
def money():
    global money_new
    with open("bank_money.txt", 'w'):
        window_dop = tk.Toplevel()
        window_dop.geometry('400x400')
        money_new = tk.Entry(window_dop, width=15, font=('Comic', 14))
        money_new.place(x=50, y=0)

        button_money_new = tk.Button(window_dop, command=money_button, width=4, height=2, text='Ок')
        button_money_new.place(x=30, y=190)
def cotegitite():
    global coter
    window_dop = tk.Toplevel()
    window_dop.geometry('400x400')
    coter = tk.Entry(window_dop, width=15, font=('Comic', 14))
    coter.place(x=50, y=0)
    new_button = tk.Button(window_dop, command=coter_button, text='Ок', font=('Comic', 14), width=15, height=2,)
    new_button.place(x=190, y=300)

def coter_button():
    with open("basa_coter.txt", 'a') as coter2:
        coter2.write(f'{coter.get()} ')
button_money = tk.Button(window_boss, command=money, width=15, height=2, text='Изменить доход', font=('Comic', 14))
button_money.place(x=400, y=0)
button_cotegirite = tk.Button(window_boss, command=cotegitite, text='Добавить новую категорию')
button_cotegirite.place(x=200, y=100)
window_boss.mainloop()