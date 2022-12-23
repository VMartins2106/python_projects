from tkinter import *
from tkinter import messagebox
import os
import banco

def atualizarPagina():
    vquery="SELECT * FROM tbaluno"
    res = banco.dql(vquery)

    margintop = 60
    for cad in res:
        Label(
            app, 
            text=cad[0],
            background="#dde", 
            foreground="#009", 
            anchor=W).place(
                x=10,
                y=margintop,
                width=200,
                height=20
            )
        Label(
            app, 
            text=cad[1],
            background="#dde", 
            foreground="#009", 
            anchor=W).place(
                x=60,
                y=margintop,
                width=200,
                height=20
            )
        Label(
            app, 
            text=cad[2],
            background="#dde", 
            foreground="#009", 
            anchor=W).place(
                x=240,
                y=margintop,
                width=100,
                height=20
            )
        Label(
            app, 
            text=cad[3],
            background="#dde", 
            foreground="#009", 
            anchor=W).place(
                x=340,
                y=margintop,
                width=200,
                height=20
            )
        vquery=f"SELECT objetivo FROM tbaluno WHERE codigoaluno = {cad[0]}"
        res = banco.dql(vquery)
        objetivo = list(res[0])
        Label(
            app, 
            text=objetivo[0],
            background="#dde", 
            foreground="#009", 
            anchor=W).place(
                x=580,
                y=margintop +5,
                width=200,
                height=25
            )
        margintop+=20

def deletar():
    mb=messagebox.askyesno("Deletar","Confirmar deleção deste aluno ?")
    if mb:
        codigo = tb_cod.get()
        tb_cod.delete(0,END)
        vquery=f"DELETE FROM tbaluno where codigoaluno={codigo}"
        banco.dml(vquery)
    atualizarPagina()
        
app=Tk()

app.title("CRUD tkinter")
app.geometry("1000x300")
app.configure(background="#dde")

Label(
    app, 
    text="Informe o código do aluno: ",
    background="#dde", 
    foreground="#009", 
    anchor=W).place(
        x=10,
        y=10,
        width=200,
        height=20
    )
tb_cod=Entry(app)
tb_cod.place(x=10,y=30,width=200,height=20)

atualizarPagina()

Button(
    app, 
    text="Deletar aluno",
    command=deletar
    ).place(
        x=10,
        y=270,
        width=100,
        height=20
        )

app.mainloop()