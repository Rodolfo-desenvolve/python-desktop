# tela de bloqueio
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import sleep
from PIL import Image, ImageTk
# 1° passo : tela
bloqueio = Tk()

# 2° passo : classe para orgnizar
class Bloqueio:
    # 3° passo : construtor
    def __init__(self):
        self.tela = bloqueio
        self.cores()
        self.config_bloq()
        self.frames_bloqueio()
        self.texto_login()
        self.contador()
        self.entradas_bloq()
        self.varia()
        self.imagens_tela()
        self.tela.mainloop()


    def cores(self):
        self.cor1 = '#3b3b3b'  # preto leve
        self.cor2 = '#333333'  # preto forte
        self.cor3 = '#ffffff'  # branco
        self.cor4 = '#fcc058'  # laganja

    # 4° passo : configurar tela
    def config_bloq(self):
        self.tela.title('')
        self.tela.geometry('250x300')
        self.tela.config(bg='#1e3743')
        self.tela.resizable(False, False)

    # 5° passo : frames tela
    def frames_bloqueio(self):
        self.frame_cima = Frame(self.tela, bd=2, bg=self.cor2)
        self.frame_cima.place(x=0, y=0, width=250, height=50)

        self.frame_baixo = Frame(self.tela, bd=2, bg=self.cor1)
        self.frame_baixo.place(x=0, y=50, width=250, height=250)

    def entradas_bloq(self):
        self.lb_login= Label(self.frame_cima, text='LOGIN', bd=2, bg=self.cor2, fg=self.cor4,
                             font=('Ivy 18 bold'))
        self.lb_login.place(x=10, y=15, width=100, height=20)

        self.linha1 = Label(self.frame_cima, text='', bg=self.cor4)
        self.linha1.place(x=0, y=45, width=180, height=2)

        self.lb_nome = Label(self.frame_baixo, text='NOME USUARIO', bd=2, fg=self.cor4, bg=self.cor1,
                             font=('Ivy 10 bold'))
        self.lb_nome.place(x=70, y=80, width=110, height=20)

        self.entry_nome = Entry(self.frame_baixo, relief=SOLID, justify='center', bg=self.cor3, fg=self.cor2,
                                font=('Ivy 10 bold'))
        self.entry_nome.place(x=25, y=110, width=200, height=20)

        self.lb_senha = Label(self.frame_baixo, text='Senha', bd=2, bg=self.cor1, fg=self.cor4,
                              font=('Ivy 10 bold'))
        self.lb_senha.place(x=100, y=150, width=50, height=20)

        self.entry_senha = Entry(self.frame_baixo,show='*', relief=SOLID, justify='center', bg=self.cor3, fg=self.cor2,
                                 font=('Ivy 10 bold'))
        self.entry_senha.place(x=25, y=180, width=150, height=20)

        self.bt_entrar = Button(self.frame_baixo, text='ENTRAR', bd=4, bg=self.cor2, fg=self.cor3,
                                font=('Ivy 8 bold'),command=self.config_entrada)
        self.bt_entrar.place(x=175, y=180, width=50, height=20)

    def varia(self):
        self.lista = ['Rodolfo', '12345']
        self.nome1 = self.entry_nome.get()
        self.senha1 = self.entry_senha.get()

    # 7° passo : funções de login
    def texto_login(self):
        self.texto1 = Label(self.frame_baixo, text='', bd=2, bg=self.cor1, fg='red',
                            font=('verdana 8 bold'))
        self.texto1.place(x=75, y=130, width=100, height=20)

        self.texto2 = Label(self.frame_baixo, text='', bd=2, bg=self.cor1, fg='red',
                            font=('verdana 8 bold'))
        self.texto2.place(x=70, y=210, width=110, height=20)

    def contador(self):
        self.contado = 5

    def config_entrada(self):
        self.varia()
        self.texto_login()
        self.contador()
        if self.nome1 == self.lista[0] and self.senha1 != self.lista[1]:
            self.texto2['text'] = '*SENHA ERRADA*'
        elif self.nome1 != self.lista[0] and self.senha1 == self.lista[1]:
            self.texto1['text'] = '*NOME ERRADO*'
        elif self.nome1 != self.lista[0] and self.senha1 != self.lista[1]:
            self.texto1['text'] = '*NOME ERRADO*'
            self.texto2['text'] = '*SENHA ERRADA*'
        else:
            sleep(4)
            self.tela.destroy()
            messagebox.showinfo('Login', f'Seja  bem-vindo {self.nome1}')

    def imagens_tela(self):
        self.icon_1 = Image.open('login.png')
        self.icon_1 = self.icon_1.resize((50, 50))
        self.icon_1 = ImageTk.PhotoImage(self.icon_1)
        self.l_icon1 = Label(self.frame_baixo, image=self.icon_1, bd=2, bg=self.cor1, fg=self.cor4)
        self.l_icon1.place(x=75, y=-20, width=100, height=100)

Bloqueio()
