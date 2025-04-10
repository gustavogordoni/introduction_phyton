from GUI import Gui
import Backend as core
from tkinter import END

app = Gui()
core.initDB()

selected = None

def getSelectedRow(event):
    global selected
    if not app.listClientes.curselection():
        return
    index = app.listClientes.curselection()[0]
    selected = app.listClientes.get(index)

    app.entNome.delete(0, END)
    app.entNome.insert(0, selected[1])
    app.entSobrenome.delete(0, END)
    app.entSobrenome.insert(0, selected[2])
    app.entEmail.delete(0, END)
    app.entEmail.insert(0, selected[3])
    app.entCPF.delete(0, END)
    app.entCPF.insert(0, selected[4])

def view_command():
    app.listClientes.delete(0, END)
    for row in core.view():
        app.listClientes.insert(END, row)

def insert_command():
    core.insert(
        app.txtNome.get(),
        app.txtSobrenome.get(),
        app.txtEmail.get(),
        app.txtCPF.get()
    )
    view_command()

def search_command():
    app.listClientes.delete(0, END)
    for row in core.search(
        app.txtNome.get(),
        app.txtSobrenome.get(),
        app.txtEmail.get(),
        app.txtCPF.get()
    ):
        app.listClientes.insert(END, row)

def update_command():
    if selected:
        core.update(
            selected[0],
            app.txtNome.get(),
            app.txtSobrenome.get(),
            app.txtEmail.get(),
            app.txtCPF.get()
        )
        view_command()

def delete_command():
    if selected:
        core.delete(selected[0])
        view_command()

# Ligar botões
app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)
app.btnViewAll.config(command=view_command)
app.btnInserir.config(command=insert_command)
app.btnBuscar.config(command=search_command)
app.btnUpdate.config(command=update_command)
app.btnDel.config(command=delete_command)

app.run()
