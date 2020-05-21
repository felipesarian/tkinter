import tkinter as tk
import pickle
from user import User

window = tk.Tk()
window.geometry('400x400')
window.title("Welcome TKInter")

nomeescrever = tk.Entry(window)
nomeescrever.grid(column=1, row=4)

senhaescrever = tk.Entry(window)
senhaescrever.config(show='*')
senhaescrever.grid(column=1, row=7)


def getvalues(entry1, entry2):
    nomeusuario = entry1.get()
    senhausuario = entry2.get()
    return [nomeusuario, senhausuario]


def submit():
    print('Clicou submit')
    username, password = getvalues(nomeescrever, senhaescrever)
    arquivo_users = open('users.pickle', 'rb')
    users = pickle.load(arquivo_users)
    arquivo_users.close()
    print(users)
    validusername = False
    print(users)
    for user in users:
        if user.username == username:
            print("AAAA")
            validusername = True
            if user.senha == password:
                print(user.username, '\n', user.senha, '\n', user.email, '\n', user.cpf, '\n', user.telefone)
            else:
                print('senha não corresponde eo usuario')
    if not validusername:
        print('usuario invalido')


titulo = tk.Label(window, text='Log-in', font=('Arial Bold', 50))
titulo.grid(column=1, row=0)

nome = tk.Label(window, text='Nome de usuário:', font=('Arial Bold', 20))
nome.grid(column=1, row=3)

senha = tk.Label(window, text='Senha:', font=('Arial Bold', 20))
senha.grid(column=1, row=6)

enter = tk.Button(window, text='Enter', command=submit)
enter.grid(column=1, row=9)

window.mainloop()
