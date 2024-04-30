# importação de biblioteca
from tkinter import *

janela = Tk()

# cria classe
class Calculadora:
    # criar construtor
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frame_tela()
        self.variavel()
        self.conecta_valores()
        self.botoes()
        janela.mainloop()

    # configurações da tela
    def tela(self):
        self.janela.title('Calculadora')
        self.janela.geometry('200x315')
        self.janela.config(bg='#1e3743')
        self.janela.resizable(False, False)

    # criar frames da tela
    def frame_tela(self):
        self.frame = Frame(self.janela, bd=2, bg='silver')
        self.frame.place(relx=0, rely=0, relheight=0.2, relwidth=100)

        self.frame_02 = Frame(self.janela, bd=2, bg='Silver')
        self.frame_02.place(relx=0, rely=0.2, relwidth=100, relheight=0.8)

    def variavel(self):
        self.valor_texto = StringVar()
        self.valores = ''

    def conecta_valores(self, valor=''):

        self.valores += valor
        print(self.valores)

        self.valor_texto.set(self.valores)

    def calcular(self):
        self.resultado = eval(self.valores)
        print(self.resultado)

        self.valor_texto.set(self.resultado)

    def funcao_limpar(self):
        self.valores = ""
        self.valor_texto.set("")

    # criar botoes
    def botoes(self):
        self.texto_label = Label(self.frame, textvariable=self.valor_texto, padx=7,
                                 relief=FLAT, fg='white', anchor="e", justify=RIGHT, font=('verdana', 18), bg='#1e3743')
        self.texto_label.place(x=0, y=0, width=200, height=60)

        self.bt_c = Button(self.frame_02, command=lambda: self.funcao_limpar(), text='C',
                           fg='white', bg='#FF7F00', bd=4, font=('verdana', 13))
        self.bt_c.place(x=0, y=0, width=100, height=50)

        self.bt_modulo = Button(self.frame_02,command=lambda:self.conecta_valores('%'),text='%',
                                bg='#FF7F00', bd=4, fg='white', font=('verdana', 13))
        self.bt_modulo.place(x=100, y=0, width=50, height=50)

        self.bt_dv = Button(self.frame_02,command=lambda:self.conecta_valores('/') ,text='/',
                            bg='#FF7F00', bd=4, fg='white', font=('verdana', 13))
        self.bt_dv.place(x=150, y=0, width=50, height=50)

        self.bt_9 = Button(self.frame_02,command=lambda:self.conecta_valores('9'), text='9',
                                                       bg='#EEE9BF', bd=4, font=('verdana', 13))
        self.bt_9.place(x=100, y=50, width=50, height=50)

        self.bt_8 = Button(self.frame_02,command=lambda:self.conecta_valores('8'), text='8',
                           bg='#EEE9BF', bd=4, font=('verdana', 13))
        self.bt_8.place(x=50, y=50, width=50, height=50)

        self.bt_7 = Button(self.frame_02,command=lambda:self.conecta_valores('7'), text='7',
                           bg='#EEE9BF', bd=4, font=('verdana', 13))
        self.bt_7.place(x=0, y=50, width=50, height=50)

        self.bt_mul = Button(self.frame_02, command=lambda:self.conecta_valores('*'),text='*',
                             bg='#FF7F00', bd=4, fg='white',
                             font=('verdana', 13))
        self.bt_mul.place(x=150, y=50, width=50, height=50)

        self.bt_4 = Button(self.frame_02,command=lambda:self.conecta_valores('4'), text='4',
                           bg='#EEE9BF', bd=4, font=('verdana', 13))
        self.bt_4.place(x=0, y=100, width=50, height=50)

        self.bt_5 = Button(self.frame_02,command=lambda:self.conecta_valores('5'),text='5',
                           bd=4, bg='#EEE9BF', font=('verdana', 13))
        self.bt_5.place(x=50, y=100, width=50, height=50)

        self.bt_6 = Button(self.frame_02,command=lambda:self.conecta_valores('6'), text='6',
                           bd=4, bg='#EEE9BF', font=('verdana', 13))
        self.bt_6.place(x=100, y=100, width=50, height=50)

        self.bt_menos = Button(self.frame_02,command=lambda:self.conecta_valores('-'), text='-',
                               bd=4, bg='#FF7F00', fg='white',
                               font=('verdana', 13))
        self.bt_menos.place(x=150, y=100, width=50, height=50)

        self.bt_1 = Button(self.frame_02,command=lambda:self.conecta_valores('1'), text='1',
                           bd=4, bg='#EEE9BF', font=('verdana', 13))
        self.bt_1.place(x=0, y=150, width=50, height=50)

        self.bt_2 = Button(self.frame_02,command=lambda:self.conecta_valores('2'), text='2',
                           bd=4, bg='#EEE9BF', font=('verdana', 13))
        self.bt_2.place(x=50, y=150, width=50, height=50)

        self.bt_3 = Button(self.frame_02,command=lambda:self.conecta_valores('3'), text='3',
                           bd=4, bg='#EEE9BF', font=('verdana', 13))
        self.bt_3.place(x=100, y=150, width=50, height=50)

        self.bt_mais = Button(self.frame_02,command=lambda:self.conecta_valores('+'), text='+',
                              bd=4, bg='#FF7F00', fg='white', font=('verdana', 13))
        self.bt_mais.place(x=150, y=150, width=50, height=50)

        self.bt_0 = Button(self.frame_02,command=lambda:self.conecta_valores('0'), text='0',
                           bd=4, bg='#EEE9BF', font=('verdana', 13))
        self.bt_0.place(x=50, y=200, width=50, height=50)

        self.bt_ponto = Button(self.frame_02,command=lambda:self.conecta_valores('.'), text='.',
                               bd=4, bg='#FF7F00', fg='white', font=('verdana', 13))
        self.bt_ponto.place(x=0, y=200, width=50, height=50)

        self.bt_igual = Button(self.frame_02,command=lambda: self.calcular(), text='=',
                               bd=4, bg='#008B8B', fg='white', font=('verdana', 13))
        self.bt_igual.place(x=100, y=200, width=100, height=50)


Calculadora()

