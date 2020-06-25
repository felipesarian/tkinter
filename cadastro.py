from tkinter import *
import pickle
from user import User

class Cadastro:
    def __init__(self, master):
        window_cadastro = master
        window_cadastro.geometry('400x600')
        window_cadastro.title("TELA DE CADASTRO")

        titulo = Label(window_cadastro, text='Cadastro', font=('Arial Bold', 50))
        titulo.grid(column=1, row=0)

        nome = Label(window_cadastro, text='Nome de usuário:', font=('Arial Bold', 20))
        nome.grid(column=1, row=3)
        self.nomeescrever = Entry(window_cadastro)
        self.nomeescrever.grid(column=1, row=4)

        senha = Label(window_cadastro, text='Senha:', font=('Arial Bold', 20))
        senha.grid(column=1, row=6)
        self.senhaescrever = Entry(window_cadastro)
        self.senhaescrever.config(show='*')
        self.senhaescrever.grid(column=1, row=7)

        confirmarsenha = Label(window_cadastro, text='Confirmar Senha:', font=('Arial Bold', 20))
        confirmarsenha.grid(column=1, row=9)
        self.senhaconfirmar = Entry(window_cadastro)
        self.senhaconfirmar.config(show='*')
        self.senhaconfirmar.grid(column=1, row=10)

        email = Label(window_cadastro, text='Email:', font=('Arial Bold', 20))
        email.grid(column=1, row=12)
        self.emailescrever = Entry(window_cadastro)
        self.emailescrever.grid(column=1, row=13)

        cpf = Label(window_cadastro, text='CPF:', font=('Arial Bold', 20))
        cpf.grid(column=1, row=15)
        self.cpfescrever = Entry(window_cadastro)
        self.cpfescrever.grid(column=1, row=16)

        telefone = Label(window_cadastro, text='Número de telefone:', font=('Arial Bold', 20))
        telefone.grid(column=1, row=18)
        self.telefoneescrever = Entry(window_cadastro)
        self.telefoneescrever.grid(column=1, row=19)

        enter = Button(window_cadastro, text='Cadastrar-se', command=self.submit)
        enter.grid(column=1, row=21)

    def getvalues(self):
        nomeusuario = self.nomeescrever.get()
        senhausuario = self.senhaescrever.get()
        confirmacaosenha = self.senhaconfirmar.get()
        email = self.emailescrever.get()
        cpf = self.cpfescrever.get()
        telefone = self.telefoneescrever.get()
        return [nomeusuario, senhausuario, confirmacaosenha, email, cpf, telefone]


    def submit(self):
        arquivo_users_leitura = open('users.pickle', 'rb')
        users = pickle.load(arquivo_users_leitura)
        # print(users)
        arquivo_users_leitura.close()
        arquivo_users = open('users.pickle', 'wb')
        username, password, confirmpassword, email, cpf, telefone = self.getvalues()
        if password == confirmpassword:
            print('ok')
            user = User(username, password, email, cpf, telefone)
            users.append(user)
            pickle.dump(users, arquivo_users)
        else:
            print('as senhas nao sao iguais')

        # CODE SNIPPET TO REMAKE CORRUPTED .PICKLE FILE
        # arquivo_users = open('users.pickle', 'wb')
        # user = User("Warlen", "123", "warlen@eu.com", "1234567890", "11987022199")
        # users = [user]
        # pickle.dump(users, arquivo_users)

        arquivo_users.close()


root = Tk()
minhainterface = Cadastro(root)
root.mainloop()
