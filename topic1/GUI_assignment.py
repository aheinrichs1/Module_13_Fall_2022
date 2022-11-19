"""
Program: GUI_assignment.py
Author: Alex Heinrichs
Date Created: 11/19/2022

Program for a number guessing game!
"""
import tkinter
import random


def pick_1():
    if 1 == answer:
        label.config(text="You Win!")
    else:
        label.config(text="You Lose! Pick again loser!")
        b1['state'] = tkinter.DISABLED



def pick_2():
    if 2 == answer:
        label.config(text="You Win!")
    else:
        label.config(text="You Lose! Pick again loser!")
    return tkinter.DISABLED


def pick_3():
    if 3 == answer:
        label.config(text="You Win!")
    else:
        label.config(text="You Lose! Pick again loser!")
    return tkinter.DISABLED


def pick_4():
    if 4 == answer:
        label.config(text="You Win!")
    else:
        label.config(text="You Lose! Pick again loser!")
    return tkinter.DISABLED


def pick_5():
    if 5 == answer:
        label.config(text="You Win!")
    else:
        label.config(text="You Lose! Pick again loser!")
    return tkinter.DISABLED


def pick_6():
    if 6 == answer:
        label.config(text="You Win!")
    else:
        label.config(text="You Lose! Pick again loser!")
    return tkinter.DISABLED


def pick_7():
    if 7 == answer:
        label.config(text="You Win!")
    else:
        label.config(text="You Lose! Pick again loser!")
    return tkinter.DISABLED


def pick_8():
    if 8 == answer:
        label.config(text="You Win!")
    else:
        label.config(text="You Lose! Pick again loser!")
    return tkinter.DISABLED


def pick_9():
    if 9 == answer:
        label.config(text="You Win!")
    else:
        label.config(text="You Lose! Pick again loser!")
    return tkinter.DISABLED


def pick_10():
    if 10 == answer:
        label.config(text="You Win!")
    else:
        label.config(text="You Lose! Pick again loser!")
    return tkinter.DISABLED


answer: int = random.randint(1, 10)
m = tkinter.Tk()
m.title('Number Game')
label = tkinter.Label(m, text="Waiting for selection")
label.grid(row=11)
var1 = tkinter.IntVar()
b1 = tkinter.Button(m, text="Guess 1", command=pick_1).grid(row=0)
b2 = tkinter.Button(m, text="Guess 2", command=pick_2).grid(row=1)
b3 = tkinter.Button(m, text="Guess 3", command=pick_3).grid(row=2)
b4 = tkinter.Button(m, text="Guess 4", command=pick_4).grid(row=3)
b5 = tkinter.Button(m, text="Guess 5", command=pick_5).grid(row=4)
b6 = tkinter.Button(m, text="Guess 6", command=pick_6).grid(row=5)
b7 = tkinter.Button(m, text="Guess 7", command=pick_7).grid(row=6)
b8 = tkinter.Button(m, text="Guess 8", command=pick_8).grid(row=7)
b9 = tkinter.Button(m, text="Guess 9", command=pick_9).grid(row=8)
b10 = tkinter.Button(m, text="Guess 10", command=pick_10).grid(row=9)

tkinter.Button(m, text='Exit', command=m.destroy)
m.mainloop()
