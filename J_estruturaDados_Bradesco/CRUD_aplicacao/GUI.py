from tkinter import *

class Gui():
    def __init__(self):
        self.x_pad = 5
        self.y_pad = 3
        self.width_entry = 30

        self.window = Tk()
        self.window.wm_title("PYSQL versão 1.0")

        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        Label(self.window, text="Nome").grid(row=0, column=0, padx=self.x_pad, pady=self.y_pad)
        Label(self.window, text="Sobrenome").grid(row=1, column=0, padx=self.x_pad, pady=self.y_pad)
        Label(self.window, text="Email").grid(row=2, column=0, padx=self.x_pad, pady=self.y_pad)
        Label(self.window, text="CPF").grid(row=3, column=0, padx=self.x_pad, pady=self.y_pad)

        self.entNome = Entry(self.window, textvariable=self.txtNome, width=self.width_entry)
        self.entNome.grid(row=0, column=1, padx=self.x_pad, pady=self.y_pad)
        self.entSobrenome = Entry(self.window, textvariable=self.txtSobrenome, width=self.width_entry)
        self.entSobrenome.grid(row=1, column=1, padx=self.x_pad, pady=self.y_pad)
        self.entEmail = Entry(self.window, textvariable=self.txtEmail, width=self.width_entry)
        self.entEmail.grid(row=2, column=1, padx=self.x_pad, pady=self.y_pad)
        self.entCPF = Entry(self.window, textvariable=self.txtCPF, width=self.width_entry)
        self.entCPF.grid(row=3, column=1, padx=self.x_pad, pady=self.y_pad)

        self.listClientes = Listbox(self.window, width=100)
        self.listClientes.grid(row=4, column=0, columnspan=2, padx=self.x_pad, pady=self.y_pad, sticky='WE')

        self.scrollClientes = Scrollbar(self.window)
        self.scrollClientes.grid(row=4, column=2, sticky='NS')
        self.listClientes.configure(yscrollcommand=self.scrollClientes.set)
        self.scrollClientes.configure(command=self.listClientes.yview)

        self.btnViewAll = Button(self.window, text="Ver todos")
        self.btnViewAll.grid(row=5, column=0, sticky='WE', padx=self.x_pad, pady=self.y_pad)
        self.btnBuscar = Button(self.window, text="Buscar")
        self.btnBuscar.grid(row=5, column=1, sticky='WE', padx=self.x_pad, pady=self.y_pad)
        self.btnInserir = Button(self.window, text="Inserir")
        self.btnInserir.grid(row=6, column=0, sticky='WE', padx=self.x_pad, pady=self.y_pad)
        self.btnUpdate = Button(self.window, text="Atualizar Selecionados")
        self.btnUpdate.grid(row=6, column=1, sticky='WE', padx=self.x_pad, pady=self.y_pad)
        self.btnDel = Button(self.window, text="Deletar Selecionados")
        self.btnDel.grid(row=7, column=0, sticky='WE', padx=self.x_pad, pady=self.y_pad)
        self.btnClose = Button(self.window, text="Fechar", command=self.window.destroy)
        self.btnClose.grid(row=7, column=1, sticky='WE', padx=self.x_pad, pady=self.y_pad)

    def run(self):
        self.window.mainloop()
