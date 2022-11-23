"""
Program: database_and_gui_assignment.py
Author: Alex Heinrichs
Date Created: 11/21/2022

Connecting to a database with a primitive GUI add-on called tkinter
"""
import tkinter
import sqlite3
from sqlite3 import Error

from topic2.connect_sqlite import *
from topic2.create_database_table import *
from topic2.create_rows import *
from topic2.database_query import *


def create_db_and_table():
    create_tables("pythonsqlite.db")
    print('working')


def add_person():
    first_name = person_first_name.get()
    last_name = person_last_name.get()
    if first_name == '' or last_name == '':
        print('Please fill in all fields')
        raise ValueError
    p = (first_name, last_name)
    create_person(conn, p)


def add_student():
    first_name = student_first_name.get()
    last_name = student_last_name.get()
    major = student_major.get()
    sdate = student_startdate.get()
    if first_name == '' or last_name == '' or major == '' or sdate == '':
        print('Please fill in all fields')
        raise ValueError
    cur = conn.cursor()
    cur.execute("SELECT id FROM person WHERE firstname = '{}' AND lastname = '{}'".format(first_name, last_name))
    pid = cur.fetchone()
    if pid is None:
        print('No Person found, Please try again')
        raise ValueError
    s = (pid[0], major, sdate)
    create_student(conn, s)


def view_person_table():
    persons = select_all_persons(conn)
    pt = 'Person Table:\nId, First name, Last name'
    for person in persons:
        pt += '\n'
        for field in person:
            pt += str(field) + ' '
    table_label.config(text=pt)


def view_student_table():
    students = select_all_students(conn)
    st = 'Person Table:\nPerson ID, Major, Start Date, End Date'
    for student in students:
        st += '\n'
        for field in student:
            st += str(field) + ' '
    table_label.config(text=st)


conn = create_connection("pythonsqlite.db")
with conn:
    m = tkinter.Tk()
    m.title('Database and GUI assignment')
    person_first_name = tkinter.StringVar()
    person_last_name = tkinter.StringVar()
    student_first_name = tkinter.StringVar()
    student_last_name = tkinter.StringVar()
    student_major = tkinter.StringVar()
    student_startdate = tkinter.StringVar()

    tkinter.Button(m, text="Create Database and Table", command=create_db_and_table).grid(row=0)
    tkinter.Entry(m, textvariable=person_first_name).grid(row=1)
    tkinter.Entry(m, textvariable=person_last_name).grid(row=2)
    tkinter.Button(m, text="Add Person", command=add_person).grid(row=3)
    tkinter.Entry(m, textvariable=student_first_name).grid(row=4)
    tkinter.Entry(m, textvariable=student_last_name).grid(row=5)
    tkinter.Entry(m, textvariable=student_major).grid(row=6)
    tkinter.Entry(m, textvariable=student_startdate).grid(row=7)
    tkinter.Button(m, text="Add Student", command=add_student).grid(row=8)
    tkinter.Button(m, text="View Person Table", command=view_person_table).grid(row=9)
    tkinter.Button(m, text="View Student Table", command=view_student_table).grid(row=10)
    table_label = tkinter.Label(m)
    table_label.grid(row=11)
    tkinter.Button(m, text="Exit", command=m.destroy).grid(row=12)
    m.mainloop()
