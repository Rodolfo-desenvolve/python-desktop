# 0° passo : importar as bibliotecas
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import json

# 1° passo : criar janela
janela = Tk()

# 2° passo : criar a class
class Bitcoin:
    # 3° passo : construtor
    def __init__(self):
        self.janela = janela
        self.cores()
        self.config_tela()
        self.config_frames()
        self.config_widghts()
        self.config_funcao()
        self.janela.mainloop()

    # 4° passo : configuro tela
    def config_tela(self):
        self.janela.title('')
        self.janela.geometry('350x300')
        self.janela.configure(bg=self.cor2)
        self.janela.resizable(False, False)

    # 5° passo : configurar os 3 frame
    def config_frames(self):
        self.frame_cima = Frame(self.janela, width=280, height=70, bg=self.cor6, highlightbackground=self.cor7,
                                highlightthickness=1)
        self.frame_cima.grid(row=0, column=0)

        self.frame_baixo = Frame(self.janela, width=280, height=230, bg=self.cor3, highlightbackground=self.cor7,
                                highlightthickness=1)
        self.frame_baixo.grid(row=1, column=0)

        self.frame_esquerda = Frame(self.janela, width=70, height=300, bg=self.cor6,  highlightbackground=self.cor7,
                                highlightthickness=1)
        self.frame_esquerda.place(x=280, y=0)

    # 6° passo : criar os widghts
    def config_widghts(self):
        self.img = Image.open('conversor1.png')
        self.img = self.img.resize((50, 50))
        self.img = ImageTk.PhotoImage(self.img)
        self.l_img = Label(self.frame_esquerda, image=self.img, bg=self.cor6, relief=FLAT, font=('Arial 10 bold'))
        self.l_img.place(x=5, y=5)

        self.img1 = Image.open('bitcoin.png')
        self.img1 = self.img1.resize((60, 60))
        self.img1 = ImageTk.PhotoImage(self.img1)
        self.l_img1 = Label(self.frame_cima, image=self.img1, bg=self.cor6, relief=FLAT, font=('Arial 10 bold'))
        self.l_img1.place(x=5, y=3)

        self.img2 = Image.open('eurobit.png')
        self.img2 = self.img2.resize((60, 60))
        self.img2 = ImageTk.PhotoImage(self.img2)
        self.l_img2 = Label(self.frame_esquerda, image=self.img2, bg=self.cor6, relief=FLAT, font=('Arial 10 bold'))
        self.l_img2.place(x=2, y=80)

        self.img3 = Image.open('realbit.png')
        self.img3 = self.img3.resize((60, 60))
        self.img3 = ImageTk.PhotoImage(self.img3)
        self.l_img3 = Label(self.frame_esquerda, image=self.img3, bg=self.cor6, relief=FLAT, font=('Arial 10 bold'))
        self.l_img3.place(x=2, y=150)

        self.img4 = Image.open('frabit.png')
        self.img4 = self.img4.resize((60, 60))
        self.img4 = ImageTk.PhotoImage(self.img4)
        self.l_img4 = Label(self.frame_esquerda, image=self.img4, bg=self.cor6, relief=FLAT, font=('Arial 10 bold'))
        self.l_img4.place(x=2, y=220)

        self.l_nome = Label(self.frame_cima, text='PEÇO DO BITCOIN', bg=self.cor6, fg=self.cor5, font=('Arial 16 bold'),
                            relief=FLAT)
        self.l_nome.place(x=70, y=20)

        # frame baixo ---------------------
        self.l_dolar = Label(self.frame_baixo, text='', anchor='center', bg=self.cor3, fg=self.cor4, relief=RIDGE,
                             font=('Arial 13 bold'), highlightbackground=self.cor7, highlightthickness=1)
        self.l_dolar.place(x=5, y=100, width=270, height=30)

        self.l_real = Label(self.frame_baixo, text='', anchor='center', bg=self.cor3, fg=self.cor4, relief=RIDGE,
                            font=('Arial 13 bold'), highlightbackground=self.cor7, highlightthickness=1)
        self.l_real.place(x=5, y=130, width=270, height=30)

        self.l_franco = Label(self.frame_baixo, text='', anchor='center', bg=self.cor3, fg=self.cor4,
                              relief=RIDGE, font=('Arial 13 bold'), highlightbackground=self.cor7, highlightthickness=1)
        self.l_franco.place(x=5, y=160, width=270, height=30)

        self.l_euro = Label(self.frame_baixo, text='', anchor='center', bg=self.cor3, fg=self.cor4, relief=RIDGE,
                            font=('Arial 13 bold'), highlightbackground=self.cor7, highlightthickness=1)
        self.l_euro.place(x=5, y=190, width=270, height=30)

        self.l_bit = Label(self.frame_baixo, text='BICTCOIN = BTC 1 UNIDADE', bg=self.cor3, fg=self.cor4, relief=RIDGE,
                           font=('Arial 13 bold'), highlightbackground=self.cor7, highlightthickness=1)
        self.l_bit.place(x=5, y=10, width=270, height=70)

    # 7° passo : criar função
    def config_funcao(self):
        link = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CCHT%2CBRL'
        requisicao = requests.get(link)
        dados = requisicao.json()

        valor_usd = float(dados['USD'])
        self.formato = 'Dolares = ${:,.3f}'.format(valor_usd)
        self.l_dolar['text'] = self.formato

        valor_brl = float(dados['BRL'])
        self.formato1 ='Reais = R${:,.3f}'.format(valor_brl)
        self.l_real['text'] = self.formato1


        valor_eur = float(dados['EUR'])
        self.formato3= 'EURO = €{:,.3f}'.format(valor_eur)
        self.l_euro['text'] = self.formato3

        # self.frame_baixo.after(1000, self.config_funcao)

    # 8° passo : criar variavel de cores
    def cores(self):
        self.cor1 = '#3b3b3b'  # preto leve
        self.cor2 = '#333333'  # preto forte
        self.cor3 = '#ffffff'  # branco
        self.cor4 = '#fcc058'  # laganja
        self.cor5 = '#5C7CFA'  # azul
        self.cor6 = '#1e3743'  # azul
        self.cor7 = '#9900cc'  # roxo
        self.cor8 = '#e1f5fe'  # azul claro
        self.cor9 = '#ffca28'  # amarelo
        self.cor10 = '#9e9e9e'  # cinza


Bitcoin()

