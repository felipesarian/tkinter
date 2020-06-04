from tkinter import *

# começando a definição da classe calculadora
class Calculadora:
    #master é uma instancia de tkinter
    def __init__(self, master):
        self.master = master
        master.title('calculadora')
        self.screen = Text(master, state = "disabled", width = 30, height = 3, background = 'black', foreground = 'white')
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.screen.configure(state='normal')
        self.equation = ''

        # criação dos botões
        b1 = self.createButton(7)
        b2 = self.createButton(8)
        b3 = self.createButton(9)
        b4 = self.createButton(u"\u232B", None) #apagar
        b5 = self.createButton(4)
        b6 = self.createButton(5)
        b7 = self.createButton(6)
        b8 = self.createButton(u"\u00F7") #dividir
        b9 = self.createButton(1)
        b10 = self.createButton(2)
        b11 = self.createButton(3)
        b12 = self.createButton('*')
        b13 = self.createButton('.')
        b14 = self.createButton(0)
        b15 = self.createButton('+')
        b16 = self.createButton('-')
        b17 = self.createButton('=', None, 34)

        botoes = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17]
        contador = 0

        for row in range(1,5):
            for column in range(4):
                botoes[contador].grid(row=row, column=column)
                contador += 1
        b17.grid(row=6, column=0, columnspan=4)

    #função de criar botões
    def createButton(self, valor, write=True, width=7):    
        return Button(self.master, text=valor, command=lambda: self.click(valor, write), width=width)

    def click(self, text, write):
        if write == None:
            if text == '=' and self.equation:
                self.equation = re.sub(u'\u00F7', '/', self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer, newline=True)
            elif text == u'\u232B':
                self.clear_screen()
        else:
            self.insert_screen(text)

    def clear_screen(self):
        self.equation = ''
        self.screen.configure(state='normal')
        self.screen.delete('1.0', END)

    def insert_screen(self, value, newline=False):
        self.screen.configure(state='normal')
        self.screen.insert(END, value)
        self.equation += str(value)
        self.screen.configure(state='disabled')

root = Tk()
minhainterface = Calculadora(root)
root.mainloop()