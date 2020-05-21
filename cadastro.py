import tkinter as tk
import pickle
from user import User

window = tk.Tk()
window.geometry('400x600')
window.title("TELA DE CADASTRO")


def getvalues(nome, senha, confirmsenha, email, cpf, telefone):
    nomeusuario = nome.get()
    senhausuario = senha.get()
    confirmacaosenha = confirmsenha.get()
    email = email.get()
    cpf = cpf.get()
    telefone = telefone.get()


    return [nomeusuario, senhausuario, confirmacaosenha, email, cpf, telefone]


def submit():
    print('Clicou submit')
    arquivo_users_leitura = open('users.pickle', 'rb')
    users = pickle.load(arquivo_users_leitura)
    arquivo_users_leitura.close()
    arquivo_users = open('users.pickle', 'wb')
    username, password, confirmpassword, email, cpf, telefone = getvalues(
        nomeescrever, senhaescrever, senhaconfirmar, emailescrever, cpfescrever, telefoneescrever)
    if password == confirmpassword:
        print('ok')
        user = User(username, password, email, cpf, telefone)
        users.append(user)
        pickle.dump(users, arquivo_users)
    else:
        print('as senhas nao sao iguais')
    arquivo_users.close()


titulo = tk.Label(window, text='Cadastro', font=('Arial Bold', 50))
titulo.grid(column=1, row=0)

nome = tk.Label(window, text='Nome de usuário:', font=('Arial Bold', 20))
nome.grid(column=1, row=3)
nomeescrever = tk.Entry(window)
nomeescrever.grid(column=1, row=4)

senha = tk.Label(window, text='Senha:', font=('Arial Bold', 20))
senha.grid(column=1, row=6)
senhaescrever = tk.Entry(window)
senhaescrever.config(show='*')
senhaescrever.grid(column=1, row=7)

confirmarsenha = tk.Label(
    window, text='Confirmar Senha:', font=('Arial Bold', 20))
confirmarsenha.grid(column=1, row=9)
senhaconfirmar = tk.Entry(window)
senhaconfirmar.config(show='*')
senhaconfirmar.grid(column=1, row=10)

email = tk.Label(window, text='Email:', font=('Arial Bold', 20))
email.grid(column=1, row=12)
emailescrever = tk.Entry(window)
emailescrever.grid(column=1, row=13)

cpf = tk.Label(window, text='CPF:', font=('Arial Bold', 20))
cpf.grid(column=1, row=15)
cpfescrever = tk.Entry(window)
cpfescrever.grid(column=1, row=16)

telefone = tk.Label(window, text='Número de telefone:', font=('Arial Bold', 20))
telefone.grid(column=1, row=18)
telefoneescrever = tk.Entry(window)
telefoneescrever.grid(column=1, row=19)


enter = tk.Button(window, text='Cadastrar-se', command=submit)
enter.grid(column=1, row=21)
window.mainloop()
