from tkinter import *
import os
import banco

def gravarDados():
    vnome=tb_nome.get()
    vfone=tb_fone.get()
    vemail=tb_email.get()
    vobj=tb_obj.get("1.0", END)
    if (vnome != "") & (vfone != "") & (vemail != "") & (vobj != ""):
        vquery=f"INSERT INTO tbaluno (nome,telefone,email,objetivo) VALUES ('{vnome}','{vfone}','{vemail}','{vobj}')"
        banco.dml(vquery)
        tb_nome.delete(0,END)
        tb_fone.delete(0,END)
        tb_email.delete(0,END)
        tb_obj.delete("1.0",END)
        print("Dados gravados")
    else:
        print("ERRO")

app=Tk()

app.title("CFB Cursos")
app.geometry("500x300")
app.configure(background="#dde")

# ANCORA : N (NORTE), S (SUL), E (LESTE), W (OESTE) --> PODEM SER COMBINADOS:
# NE (NOROESTE) SE (SUDESTE) SO (SUDOESTE) NO (NOROESTE)
Label(
    app, 
    text="Nome: ",
    background="#dde", 
    foreground="#009", 
    anchor=W).place(
        x=10,
        y=10,
        width=100,
        height=20
    )
tb_nome=Entry(app)
tb_nome.place(x=10,y=30,width=200,height=20)

Label(
    app, 
    text="Telefone: ",
    background="#dde", 
    foreground="#009", 
    anchor=W).place(
        x=10,
        y=60,
        width=100,
        height=20
    )
tb_fone=Entry(app)
tb_fone.place(x=10,y=80,width=100,height=20)

Label(
    app, 
    text="Email: ",
    background="#dde", 
    foreground="#009", 
    anchor=W).place(
        x=10,
        y=110,
        width=100,
        height=20
    )
tb_email=Entry(app)
tb_email.place(x=10,y=130,width=300,height=20)

Label(
    app, 
    text="Objetivo: ",
    background="#dde", 
    foreground="#009", 
    anchor=W).place(
        x=10,
        y=160,
        width=100,
        height=20
    )
tb_obj=Text(app)
tb_obj.place(x=10,y=180,width=300,height=80)

Button(
    app, 
    text="Gravar",
    command=gravarDados
    ).place(
        x=10,
        y=270,
        width=100,
        height=20
        )
    
app.mainloop()