#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

"""
Напишите программу, в которой имеется несколько объединенных в группу радиокнопок,
индикатор которых выключен (indicatoron=0). Если какая-нибудь кнопка включается, то в
метке должна отображаться соответствующая ей информация. Обычных кнопок в окне быть
не должно.
"""

persons = {
    'Николай': '+7 988 155-12-12',
    'Дмитрий': '+7 988 156-13-13',
    'Иван': '+7 988 157-14-14'
}


def get_contact():
    label.config(text=persons[var.get()])


if __name__ == "__main__":
    root = Tk()
    root.title('ИВТ-б-о-20-1')
    root.resizable(height=False, width=False)

    f_left = Frame(root)
    f_left.pack(side=LEFT)

    label = Label(root, justify='center', width=40, text='Выберите студента', font=18)
    label.pack(side=LEFT, expand=True)

    var = StringVar()

    for name in persons.keys():
        Radiobutton(f_left, width=20, font=20, text=name, indicatoron=0, variable=var,
                    value=name, command=get_contact).pack(side=TOP)

    root.mainloop()
