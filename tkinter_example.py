import tkinter as tk

window = tk.Tk()
window.geometry('400x400')
window.title("Welcome TKInter")

titulo = tk.Label(window, text='Log-in', font=('Arial Bold', 50))
titulo.grid(column = 0, row = 0)

nome = tk.Label(window, text='Nome de usuário:', font=('Arial Bold', 20))
nome.grid(column = 0, row = 3)  

nomeescrever = tk.Entry(window)
nomeescrever.grid(column = 0, row = 4)


senha = tk.Label(window, text='Senha:', font=('Arial Bold', 20))
senha.grid(column = 0, row = 6)

senhaescrever = tk.Entry(window)
senhaescrever.grid(column = 0, row = 7)

enter = tk.Button(window, text='Enter')
enter.grid(column = 0, row = 9)

window.mainloop()
