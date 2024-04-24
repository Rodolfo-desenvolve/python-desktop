# 0° passo : importar as bibliotecas
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import json

# 1° passo : criar janela
janela = Tk()

# 2° passo : criar classe

class Conversor:

    # 3° passo : criar construtor
    def __init__(self):
        self.janela = janela
        self.cores()
        self.config_tela()
        self.config_frames()
        self.config_widghts()
        self.janela.mainloop()

    def cores(self):
        self.cor1 = '#3b3b3b'  # preto leve
        self.cor2 = '#333333'  # preto forte
        self.cor3 = '#ffffff'  # branco
        self.cor4 = '#fcc058'  # laganja
        self.cor5 = '#5C7CFA'  # azul
        self.cor6 = '#1e3743'  # azul
        self.cor7 = '#9900cc' #roxo
        self.cor8 = '#e1f5fe' #azul claro
        self.cor9 = '#ffca28' #amarelo
        self.cor10 = '#9e9e9e' #

    # 4° passo : configurar tela
    def config_tela(self):
        self.janela.title('')
        self.janela.geometry('300x300')
        self.janela.configure(bg=self.cor1)
        self.janela.resizable(False, False)

    # 5° passo : dividir frames
    def config_frames(self):
        self.frame_cima = Frame(self.janela, width=225, height=70, bg=self.cor6, highlightbackground=self.cor7,
                                 highlightthickness=2)
        self.frame_cima.grid(row=0, column=0)

        self.frame_baixo = Frame(self.janela, width=225, height=230, bg=self.cor10, highlightbackground=self.cor7,
                                 highlightthickness=2)
        self.frame_baixo.grid(row=1, column=0)

        self.frame_esquerda = Frame(self.janela, width=75, height=300, bg=self.cor6, highlightbackground=self.cor7,
                                    highlightthickness=2)
        self.frame_esquerda.place(x=225, y=0)

    # 6° passo : widghts
    def config_widghts(self):

        self.l_nome = Label(self.frame_cima, text='Conversor de Moedas', bd=2, bg=self.cor6, fg=self.cor5,
                            font=('Arial 16 bold'), relief=FLAT)
        self.l_nome.place(x=-4, y=20)

        self.img1 = Image.open('conversor1.png')
        self.img1 = self.img1.resize((50, 50))
        self.img1 = ImageTk.PhotoImage(self.img1)
        self.l_img1 = Label(self.frame_esquerda, image=self.img1, bd=2, bg=self.cor6, relief=FLAT)
        self.l_img1.place(x=10, y=5)

        self.img2 = Image.open('iconeuro.png')
        self.img2 = self.img2.resize((50, 50))
        self.img2 = ImageTk.PhotoImage(self.img2)
        self.l_img2 = Label(self.frame_esquerda, image=self.img2, bd=2, bg=self.cor6, relief=RIDGE)
        self.l_img2.place(x=10, y=75)

        self.img3 = Image.open('iconsuico.png')
        self.img3 = self.img3.resize((50, 50))
        self.img3 = ImageTk.PhotoImage(self.img3)
        self.l_img3 = Label(self.frame_esquerda, image=self.img3, bd=2, bg=self.cor6, relief=RIDGE)
        self.l_img3.place(x=10, y=130)

        self.img4 = Image.open('icondolar.png')
        self.img4 = self.img4.resize((50, 50))
        self.img4 = ImageTk.PhotoImage(self.img4)
        self.l_img4 = Label(self.frame_esquerda, image=self.img4, bd=2, bg=self.cor6, relief=RIDGE)
        self.l_img4.place(x=10, y=185)

        self.img5 = Image.open('dolar.png')
        self.img5 = self.img5.resize((50, 50))
        self.img5 = ImageTk.PhotoImage(self.img5)
        self.l_img5 = Label(self.frame_esquerda, image=self.img5, bd=2, bg=self.cor6, relief=RIDGE)
        self.l_img5.place(x=10, y=240)

        self.lista = ['EUR', 'CHF', 'BRL', 'USD']

        self.l_resultado = Label(self.frame_baixo, text='', bd=2, bg=self.cor10, fg=self.cor6, font=('Ivy 15 bold'),
                                 relief=FLAT, anchor='center', highlightbackground=self.cor7, highlightthickness=1)
        self.l_resultado.place(x=25, y=25, width=175, height=40)

        self.l_de = Label(self.frame_baixo, text='De', bd=2, bg=self.cor10, fg=self.cor6, font=('Arial 10 bold'),
                          anchor=NW, relief=FLAT)
        self.l_de.place(x=25, y=70)

        self.combo_de = ttk.Combobox(self.frame_baixo, width=8, justify=CENTER, font=('Ivy 8 bold'))
        self.combo_de.place(x=25, y=90)
        self.combo_de['value'] = self.lista

        self.l_para = Label(self.frame_baixo, text='Para', bd=2, bg=self.cor10, fg=self.cor6, font=('Arial 10 bold'),
                            anchor=NW, relief=FLAT)
        self.l_para.place(x=130, y=70)

        self.combo_para = ttk.Combobox(self.frame_baixo, width=8, justify=CENTER, font=('Ivy 8 bold'))
        self.combo_para.place(x=130, y=90)
        self.combo_para['value'] = self.lista

        self.e_valor = Entry(self.frame_baixo, bd=2, bg=self.cor10, fg=self.cor6, relief=FLAT, justify=CENTER,
                             font=('Ivy 10 bold'), highlightbackground=self.cor7, highlightthickness=1)
        self.e_valor.place(x=25, y=140, width=175, height=30)

        self.b_calcular = Button(self.frame_baixo,command=self.config_calcular, text='CALCULAR', bd=2, bg=self.cor6,
                                 fg=self.cor3, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
        self.b_calcular.place(x=25, y=180, width=175, height=35)

    # 7° passo : funções
    def config_calcular(self):
        moeda_de = self.combo_de.get()
        moeda_para = self.combo_para.get()
        valor = self.e_valor.get()
        self.link = 'https://api.exchangerate-api.com/v4/latest/{}'.format(moeda_de)

        requisicao = requests.get(self.link)
        mostrar = json.loads(requisicao.text)
        cambio = mostrar['rates'][moeda_para]

        resulta = float(valor) * float(cambio)
        if moeda_para == 'EUR':
            simbulo = '€'
        elif moeda_para == 'CHF':
            simbulo = 'Fr'
        elif moeda_para == 'USD':
            simbulo = '$'
        else:
            simbulo = 'R$'

        moeda_formatada = simbulo + '{:,.2f}'.format(resulta)
        self.l_resultado['text'] = moeda_formatada


Conversor()













