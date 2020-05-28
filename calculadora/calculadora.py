from tkinter import *

# começando a definição da classe calculadora
class Calculadora:
    #master é uma instancia de tkinter
    def __init__(self, master):
        self.master = master
        master.title('calculadora')

        # criação dos botões
        b1 = self.createButton(7)
        b2 = self.createButton(8)
        b3 = self.createButton(9)
        b4 = self.createButton(u"\u232B", None)
        b5 = self.createButton(4)
        b6 = self.createButton(5)
        b7 = self.createButton(6)
        b8 = self.createButton(u"\u00F7")
        b9 = self.createButton(1)
        b10 = self.createButton(2)
        b11 = self.createButton(3)
        b12 = self.createButton('*')
        b13 = self.createButton('.')
        b14 = self.createButton(0)
        b15 = self.createButton('+')
        b16 = self.createButton('-')
        b17 = self.createButton('=', None, 34)

    #função de criar botões
    def createButton(self, valor, write=True, width=7):    
        return Button(self.master, text=valor, command=self.click(), width=width)
        # return Button(self.master, text=valor, command=lambda: self.click(valor, write), width=width)

    def click(self):
        print('a')

root = Tk()
minhainterface = Calculadora(root)
root.mainloop()

