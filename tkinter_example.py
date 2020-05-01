import tkinter as tk

users = {'felipe': '12345'}

window = tk.Tk()
window.geometry('400x400')
window.title("Welcome TKInter")

nomeescrever = tk.Entry(window)
nomeescrever.grid(column = 0, row = 4)

senhaescrever = tk.Entry(window)
senhaescrever.config(show = '*')
senhaescrever.grid(column = 0, row = 7)

def getvalues(entry1, entry2):
    nomeusuario = entry1.get()
    senhausuario = entry2.get()
    return [nomeusuario, senhausuario]

def submit():
    print('Clicou submit')
    username, password = getvalues(nomeescrever, senhaescrever)
    if username in users:
        if password == users[username]:
            print('ok')
        else:
            print('senha não corresponde eo usuario')
    else:
        print('usuario invalido')
    

titulo = tk.Label(window, text='Log-in', font=('Arial Bold', 50))
titulo.grid(column = 0, row = 0)

nome = tk.Label(window, text='Nome de usuário:', font=('Arial Bold', 20))
nome.grid(column = 0, row = 3)  

senha = tk.Label(window, text='Senha:', font=('Arial Bold', 20))
senha.grid(column = 0, row = 6)

enter = tk.Button(window, text='Enter', command = submit)
enter.grid(column = 0, row = 9)

window.mainloop()
