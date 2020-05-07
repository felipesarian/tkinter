import tkinter as tk
import pickle

window = tk.Tk()
window.geometry('400x400')
window.title("TELA DE CADASTRO")



def getvalues(entry1, entry2, entry3):
    nomeusuario = entry1.get()
    senhausuario = entry2.get()
    confirmacaosenha = entry3.get()

    return [nomeusuario, senhausuario, confirmacaosenha]

def submit():
    print('Clicou submit')
    arquivo_users = open('users.pickle', 'wb')
    username, password, confirmpassword = getvalues(nomeescrever, senhaescrever, senhaconfirmar)
    if password == confirmpassword:
        print('ok')
        users = {'username': 'felipe', 'senha': '123'}
        pickle.dump(users, arquivo_users)
    else:
        print('as senhas nao sao iguais')
    arquivo_users.close()








titulo = tk.Label(window, text='Cadastro', font=('Arial Bold', 50))
titulo.grid(column = 1, row = 0)

nome = tk.Label(window, text='Nome de usuário:', font=('Arial Bold', 20))
nome.grid(column = 1, row = 3) 
nomeescrever = tk.Entry(window)
nomeescrever.grid(column = 1, row = 4) 

senha = tk.Label(window, text='Senha:', font=('Arial Bold', 20))
senha.grid(column = 1, row = 6)
senhaescrever = tk.Entry(window)
senhaescrever.config(show = '*')
senhaescrever.grid(column = 1, row = 7)

confirmarsenha = tk.Label(window, text='Confirmar Senha:', font=('Arial Bold', 20))
senha.grid(column = 1, row = 9)
senhaconfirmar = tk.Entry(window)
senhaescrever.config(show = '*')
senhaescrever.grid(column = 1, row = 10)


enter = tk.Button(window, text='Cadastrar-se', command = submit)
enter.grid(column = 1, row = 12)

window.mainloop()