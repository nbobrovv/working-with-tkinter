#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
напишите простейший калькулятор, состоящий из двух текстовых полей,
куда пользователь вводит числа, и четырех кнопок "+", "-", "*", "/". Результат вычисления
должен отображаться в метке. Если арифметическое действие выполнить невозможно
(например, если были введены буквы, а не числа), то в метке должно появляться слово
"ошибка".
"""

from tkinter import *


def add(event):
    try:
        num1 = float(ent1.get())
        num2 = float(ent2.get())
        l1['text'] = num1+num2
    except ValueError:
        l1['text'] = 'Ошибка'


def sub(event):
    try:
        num1 = float(ent1.get())
        num2 = float(ent2.get())
        l1['text'] = num1-num2
    except ValueError:
        l1['text'] = 'Ошибка'


def mul(event):
    try:
        num1 = float(ent1.get())
        num2 = float(ent2.get())
        l1['text'] = num1*num2
    except ValueError:
        l1['text'] = 'Ошибка'


def div(event):
    try:
        num1 = float(ent1.get())
        num2 = float(ent2.get())
        l1['text'] = num1/num2
    except ValueError:
        l1['text'] = 'Ошибка'
    except ZeroDivisionError:
        l1['text'] = 'Деление на 0!'


if __name__ == '__main__':
    root = Tk()
    ent1 = Entry(width=30)
    ent2 = Entry(width=30)
    but1 = Button(text='+')
    but2 = Button(text='-')
    but3 = Button(text='*')
    but4 = Button(text='/')
    l1 = Label(font="Arial 14")
    but1.bind('<Button-1>', add)
    but2.bind('<Button-1>', sub)
    but3.bind('<Button-1>', mul)
    but4.bind('<Button-1>', div)
    l1.config(bd=10)
    ent1.pack()
    ent2.pack()
    but1.pack()
    but2.pack()
    but3.pack()
    but4.pack()
    l1.pack()
    root.mainloop()
