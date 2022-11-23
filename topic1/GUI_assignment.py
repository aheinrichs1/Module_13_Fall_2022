"""
Program: GUI_assignment.py
Author: Alex Heinrichs
Date Created: 11/19/2022

Program for a number guessing game!
"""
import tkinter
import random


def start_game():
    b0.config(state="disabled")
    b1.config(state="active")
    b2.config(state="active")
    b3.config(state="active")
    b4.config(state="active")
    b5.config(state="active")
    b6.config(state="active")
    b7.config(state="active")
    b8.config(state="active")
    b9.config(state="active")
    b10.config(state="active")
    label.config(text="Waiting for selection")


def end_game():
    b1.config(state="disabled")
    b2.config(state="disabled")
    b3.config(state="disabled")
    b4.config(state="disabled")
    b5.config(state="disabled")
    b6.config(state="disabled")
    b7.config(state="disabled")
    b8.config(state="disabled")
    b9.config(state="disabled")
    b10.config(state="disabled")


def pick_1():
    if 1 == answer:
        label.config(text="WINNER!\nWINNER!\nWINNER!\nWINNER!\nAnswer: 1")
        list_label.config(text=guessed_list.__str__())
        end_game()
    else:
        label.config(text="You Lose! Pick again loser!")
        guessed_list.add_guess(1)
        b1.config(state="disabled")


def pick_2():
    if 2 == answer:
        label.config(text="WINNER!\nWINNER!\nWINNER!\nWINNER!\nAnswer: 2")
        list_label.config(text=guessed_list.__str__())
        end_game()
    else:
        label.config(text="You Lose! Pick again loser!")
        guessed_list.add_guess(2)
        b2.config(state="disabled")


def pick_3():
    if 3 == answer:
        label.config(text="WINNER!\nWINNER!\nWINNER!\nWINNER!\nAnswer: 3")
        list_label.config(text=guessed_list.__str__())
        end_game()
    else:
        label.config(text="You Lose! Pick again loser!")
        guessed_list.add_guess(3)
        b3.config(state="disabled")


def pick_4():
    if 4 == answer:
        label.config(text="WINNER!\nWINNER!\nWINNER!\nWINNER!\nAnswer: 4")
        list_label.config(text=guessed_list.__str__())
        end_game()
    else:
        label.config(text="You Lose! Pick again loser!")
        guessed_list.add_guess(4)
        b4.config(state="disabled")


def pick_5():
    if 5 == answer:
        label.config(text="WINNER!\nWINNER!\nWINNER!\nWINNER!\nAnswer: 5")
        list_label.config(text=guessed_list.__str__())
        end_game()
    else:
        label.config(text="You Lose! Pick again loser!")
        guessed_list.add_guess(5)
        b5.config(state="disabled")


def pick_6():
    if 6 == answer:
        label.config(text="WINNER!\nWINNER!\nWINNER!\nWINNER!\nAnswer: 6")
        list_label.config(text=guessed_list.__str__())
        end_game()
    else:
        label.config(text="You Lose! Pick again loser!")
        guessed_list.add_guess(6)
        b6.config(state="disabled")


def pick_7():
    if 7 == answer:
        label.config(text="WINNER!\nWINNER!\nWINNER!\nWINNER!\nAnswer: 7")
        list_label.config(text=guessed_list.__str__())
        end_game()
    else:
        label.config(text="You Lose! Pick again loser!")
        guessed_list.add_guess(7)
        b7.config(state="disabled")


def pick_8():
    if 8 == answer:
        label.config(text="WINNER!\nWINNER!\nWINNER!\nWINNER!\nAnswer: 8")
        list_label.config(text=guessed_list.__str__())
        end_game()
    else:
        label.config(text="You Lose! Pick again loser!")
        guessed_list.add_guess(8)
        b8.config(state="disabled")


def pick_9():
    if 9 == answer:
        label.config(text="WINNER!\nWINNER!\nWINNER!\nWINNER!\nAnswer: 9")
        list_label.config(text=guessed_list.__str__())
        end_game()
    else:
        label.config(text="You Lose! Pick again loser!")
        guessed_list.add_guess(9)
        b9.config(state="disabled")


def pick_10():
    if 10 == answer:
        label.config(text="WINNER!\nWINNER!\nWINNER!\nWINNER!\nAnswer: 10")
        list_label.config(text=guessed_list.__str__())
        end_game()
    else:
        label.config(text="You Lose! Pick again loser!")
        guessed_list.add_guess(10)
        b10.config(state="disabled")


class NumberGuesser:
    def __init__(self):
        self.guessed_list = []

    def add_guess(self, guess):
        self.guessed_list.append(guess)

    def __str__(self):
        guesses = 'Guesses:'
        for guess in self.guessed_list:
            guesses += '\n' + str(guess)
        return guesses


answer: int = random.randint(1, 10)
guessed_list = NumberGuesser()
m = tkinter.Tk()
m.title('Number Game')
b0 = tkinter.Button(m, text="Start Game", command=start_game)
b0.grid(row=0)
b1 = tkinter.Button(m, text="Guess 1", state="disabled", command=pick_1)
b1.grid(row=1)
b2 = tkinter.Button(m, text="Guess 2", state="disabled",  command=pick_2)
b2.grid(row=2)
b3 = tkinter.Button(m, text="Guess 3", state="disabled",  command=pick_3)
b3.grid(row=3)
b4 = tkinter.Button(m, text="Guess 4", state="disabled",  command=pick_4)
b4.grid(row=4)
b5 = tkinter.Button(m, text="Guess 5", state="disabled",  command=pick_5)
b5.grid(row=5)
b6 = tkinter.Button(m, text="Guess 6", state="disabled",  command=pick_6)
b6.grid(row=6)
b7 = tkinter.Button(m, text="Guess 7", state="disabled",  command=pick_7)
b7.grid(row=7)
b8 = tkinter.Button(m, text="Guess 8", state="disabled",  command=pick_8)
b8.grid(row=8)
b9 = tkinter.Button(m, text="Guess 9", state="disabled",  command=pick_9)
b9.grid(row=9)
b10 = tkinter.Button(m, text="Guess 10", state="disabled",  command=pick_10)
b10.grid(row=10)
label = tkinter.Label(m)
label.grid(row=12)
list_label = tkinter.Label(m)
list_label.grid(row=13)
tkinter.Button(m, text='Exit', command=m.destroy).grid(row=11)

m.mainloop()
