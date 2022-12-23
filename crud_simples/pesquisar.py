from tkinter import *
import os
import banco

app=Tk()

app.title("CRUD tkinter")
app.geometry("1000x300")
app.configure(background="#dde")

vquery="SELECT * FROM tbaluno"
res = banco.dql(vquery)

margintop = 0

for cad in res:
    Label(
        app, 
        text=cad[1],
        background="#dde", 
        foreground="#009", 
        anchor=W).place(
            x=10,
            y=margintop + 10,
            width=200,
            height=20
        )
    Label(
        app, 
        text=cad[2],
        background="#dde", 
        foreground="#009", 
        anchor=W).place(
            x=300,
            y=margintop + 10,
            width=100,
            height=20
        )
    Label(
        app, 
        text=cad[3],
        background="#dde", 
        foreground="#009", 
        anchor=W).place(
            x=500,
            y=margintop + 10,
            width=200,
            height=20
        )
    Label(
        app, 
        text=cad[4],
        background="#dde", 
        foreground="#009", 
        anchor=W).place(
            x=800,
            y=margintop + 16,
            width=200,
            height=20
        )
    margintop+=50

app.mainloop()