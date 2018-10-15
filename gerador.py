from tkinter import *
import clipboard
#O.S, utilizar a do copy da area de transferência
class Aplicacao:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10", 'bold')
        self.primeiroContainer = Frame(master)
        self.primeiroContainer['bg'] = '#696969'
        self.primeiroContainer.pack(side=LEFT)

        # botão gerar

        self.gerar = Button(self.primeiroContainer)
        self.gerar["text"] = "Gerar"
        self.gerar["font"] = ("Calibri", "12", "bold")
        self.gerar["width"] = 20
        self.gerar['bg'] = '#00cc4c'
        self.gerar['fg'] = '#191919'
        self.gerar["command"] = self.capturaTexto
        self.gerar.pack(side=TOP)

        #botão apagar

        self.apagar = Button(self.primeiroContainer)
        self.apagar["text"] = "Apagar"
        self.apagar["font"] = ("Calibri", "12", "bold")
        self.apagar["width"] = 20
        self.apagar['bg'] = '#e61919'
        self.apagar['fg'] = '#191919'
        self.apagar["command"] = self.apagaTexto
        self.apagar.pack(side=TOP)

        #botão copiar
        self.copiar = Button(self.primeiroContainer)
        self.copiar["text"] = "Copiar"
        self.copiar["font"] = ("Calibri", "12", "bold")
        self.copiar["width"] = 20
        self.copiar['bg'] = '#ffdf00'
        self.copiar['fg'] = '#191919'
        self.copiar["command"] = self.copiaTexto
        self.copiar.pack(side=TOP)

        self.text2 = Text(master, height=32, width=60)
        self.scroll = Scrollbar(master, command=self.text2.yview)
        self.text2.configure(yscrollcommand=self.scroll.set)

        self.text2.tag_configure('color', foreground='#000')
        self.text2.insert(END, '#Feito por Igor Ramos de Oliveira, 03-09-2018.\n')
        self.quote = '#Digite os atributos separados por enter\n'
        self.text2.insert(END, self.quote, 'color')
        self.text2.pack(side=LEFT)
        self.scroll.pack(side=RIGHT, fill=Y)

    def capturaTexto(self):
        #self.apagaTexto()
        texto = self.text2.get(3.0,END)
        #tratando a string de leitura
        texto=texto.strip()
        texto=texto.replace("\n"," ")
        texto=texto.split(" ")
        #fim do tratamento
        #inicio codigo gerador
        mae=''
        for i in range(len(texto)):
            if len(texto[i])>0:
                gete = ''
                sete = ''
                gete = "\n@property\ndef " + texto[i] + "(self):\n\treturn self.__" + texto[i]
                sete = "\n@"+texto[i]+".setter\ndef " + texto[i] + "(self,valor):\n\tself.__" + texto[i] + " = valor"
                mae=mae+(gete+sete)
            else:
                pass
        #fim gerador
        self.apagaTexto2()
        self.text2.insert(END,"#Propertys Geradas com Sucesso! por Igor Ramos de Oliveira:  #2018-09/03\n\n")
        self.text2.insert(END,mae)
    def apagaTexto(self):
        self.text2.delete(1.0, END)
        self.text2.insert(END, '#Feito por Igor Ramos de Oliveira, 03-09-2018.\n')
        self.quote = '#Digite os atributos separados por enter\n'
        self.text2.insert(END, self.quote, 'color')
    def apagaTexto2(self):
        self.text2.delete(1.0, END)
    def copiaTexto(self):
        texto = self.text2.get(1.0, END)
        clipboard.copy(texto)

def centralizar(janela):
    x = (janela.winfo_screenwidth() - janela.winfo_reqwidth()) / 6
    y = (janela.winfo_screenheight() - janela.winfo_reqheight()) / 6
    janela.geometry("+%d+%d" % (x, y))

root = Tk()
root.title("Gerador Get Set versão : 1.0")
root.resizable(0,0)
root['bg']='#545454'
centralizar(root)
Aplicacao(root)
root.mainloop()
#aqui é  fim do código
#fim :)
