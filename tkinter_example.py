from tkinter import *

window = Tk()
window.geometry('450x400')

window.title("Welcome TKInter")
lbl = Label(window, text='hello', font=('Arial Bold', 50))
lbl.grid(column = 0, row = 0)
btn = Button(window, text='clique em mim')
btn.grid(column = 1, row = 1)

window.mainloop()
