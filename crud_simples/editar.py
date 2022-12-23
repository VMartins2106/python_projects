from tkinter import *
import os
import banco

def gravarDados():
    codigo = tb_cod.get()
    vnome=tb_nome.get()
    vfone=tb_fone.get()
    vemail=tb_email.get()
    vobj=tb_obj.get("1.0", END)
    if (vnome != "") & (vfone != "") & (vemail != "") & (vobj != ""):
        vquery=f"UPDATE tbaluno SET nome = '{vnome}',telefone = '{vfone}',email= '{vemail}',objetivo = '{vobj}' WHERE codigoaluno = {int(codigo)}"
        banco.dml(vquery)
        tb_cod.delete(0,END)
        tb_nome.delete(0,END)
        tb_fone.delete(0,END)
        tb_email.delete(0,END)
        tb_obj.delete("1.0",END)
        print("Dados gravados")
    else:
        print("ERRO")

app=Tk()

app.title("CFB Cursos")
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

Label(
    app, 
    text="Nome: ",
    background="#dde", 
    foreground="#009", 
    anchor=W).place(
        x=350,
        y=10,
        width=100,
        height=20
    )
tb_nome=Entry(app)
tb_nome.place(x=350,y=30,width=200,height=20)

Label(
    app, 
    text="Telefone: ",
    background="#dde", 
    foreground="#009", 
    anchor=W).place(
        x=350,
        y=60,
        width=100,
        height=20
    )
tb_fone=Entry(app)
tb_fone.place(x=350,y=80,width=100,height=20)

Label(
    app, 
    text="Email: ",
    background="#dde", 
    foreground="#009", 
    anchor=W).place(
        x=350,
        y=110,
        width=100,
        height=20
    )
tb_email=Entry(app)
tb_email.place(x=350,y=130,width=300,height=20)

Label(
    app, 
    text="Objetivo: ",
    background="#dde", 
    foreground="#009", 
    anchor=W).place(
        x=350,
        y=160,
        width=100,
        height=20
    )
tb_obj=Text(app)
tb_obj.place(x=350,y=180,width=300,height=80)

Button(
    app, 
    text="Salvar",
    command=gravarDados
    ).place(
        x=350,
        y=270,
        width=100,
        height=20
        )
    
app.mainloop()