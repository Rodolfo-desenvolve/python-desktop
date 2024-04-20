# 0° passo : importar as bibliotecas
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from pygame import mixer
from datetime import datetime
from time import sleep
from threading import Thread
from tkinter import messagebox

# 1° passo : criar janelas
janela = Tk()

# 2° passo : criar classe
class Alarme:
    # 3° passo : criar construtor
    def __init__(self):
        self.janela = janela
        self.cores()
        self.config_tela()
        self.config_frames()
        self.config_widghts()
        self.variaveis()
        self.janela.mainloop()

    # 4° passo : configurar tela
    def config_tela(self):
        self.janela.title('')
        self.janela.geometry('400x200')
        self.janela.configure(bg=self.cor3)
        self.janela.resizable(False, False)

    # 5° passo : configurar frames
    def config_frames(self):
        self.frame_top = Frame(self.janela, width=400, height=75, bg=self.cor1)
        self.frame_top.grid(row=0, column=0)

        self.frame_corpo = Frame(self.janela, width=400, height=90, bg=self.cor2)
        self.frame_corpo.grid(row=1, column=0)

        self.frame_rodape = Frame(self.janela, width=400, height=40, bg=self.cor3)
        self.frame_rodape.grid(row=2, column=0)


    # 6° passo : configurar widghts
    def config_widghts(self):
        self.img = Image.open('rel1.png')
        self.img = self.img.resize((70, 70))
        self.img = ImageTk.PhotoImage(self.img)
        self.l_img = Label(self.frame_top, image=self.img, bg=self.cor1, relief=FLAT)
        self.l_img.place(x=5, y=0)

        self.img1 = Image.open('rel2.png')
        self.img1 = self.img1.resize((70, 70))
        self.img1 = ImageTk.PhotoImage(self.img1)
        self.l_img1 = Label(self.frame_top, image=self.img1, bg=self.cor1, relief=FLAT)
        self.l_img1.place(x=320, y=0)

        self.l_nome = Label(self.frame_top, text='GELOGIO', bg=self.cor1, fg=self.cor3, relief=FLAT,
                            font=('Arial 25 bold'))
        self.l_nome.place(x=125, y=0)

        self.l_nome = Label(self.frame_top, text='ALARME', bg=self.cor1, fg='#f9004d', relief=FLAT,
                            font=('Arial 25 bold'))
        self.l_nome.place(x=125, y=35)

        self.l_linha = Label(self.frame_corpo, text='', bg=self.cor4, relief=FLAT)
        self.l_linha.place(x=0, y=0, width=400, height=5)

        self.l_horas = Label(self.frame_corpo, text='Horas', bg=self.cor2, fg=self.cor3, font=('Arial 10 bold'),
                             relief=FLAT)
        self.l_horas.place(x=65, y=15)

        self.c_horas = ttk.Combobox(self.frame_corpo, width=2, height=2, font=('Arial 15 bold'))
        self.c_horas['value'] = ('00', '01', '03', '04', '05', '06',
                                 '07', '08', '09', '10', '11', '12')
        self.c_horas.current(0)
        self.c_horas.place(x=70, y=40)

        self.l_pontos1 = Label(self.frame_corpo, text=':', bg=self.cor2, fg=self.cor3, font=('Arial 17 bold'),
                               relief=FLAT)
        self.l_pontos1.place(x=120, y=40)

        self.l_minutos = Label(self.frame_corpo, text='Minutos', bg=self.cor2, fg=self.cor3, font=('Arial 10 bold'),
                               relief=FLAT)
        self.l_minutos.place(x=135, y=15)

        self.c_minutos = ttk.Combobox(self.frame_corpo, width=2, height=2, font=('Arial 15 bold'))
        self.c_minutos['value'] = ('00', '01', '03', '04', '05', '06', '07', '08', '09',
                                   '10', '11', '12', '13', '14', '15', '16', '17', '18',
                                   '19', '20', '21', '22', '23', '24', '25', '26', '27',
                                   '28', '29', '30', '31', '32', '33', '34', '35', '36',
                                   '37', '38', '39', '40', '41', '42', '43', '44', '45',
                                   '46', '47', '48', '49', '50', '51', '52', '53', '54',
                                   '56', '57', '58', '59'
                                   )
        self.c_minutos.current(0)
        self.c_minutos.place(x=140, y=40)

        self.l_pontos2 = Label(self.frame_corpo, text=':', bg=self.cor2, fg=self.cor3, font=('Arial 17 bold'),
                               relief=FLAT)
        self.l_pontos2.place(x=190, y=40)

        self.l_segundos = Label(self.frame_corpo, text='Segundos', bg=self.cor2, fg=self.cor3, font=('Arial 10 bold'),
                                relief=FLAT)
        self.l_segundos.place(x=205, y=15)

        self.c_segundos = ttk.Combobox(self.frame_corpo, width=2, height=2, font=('Arial 15 bold'))
        self.c_segundos['value'] = ('00', '01', '03', '04', '05', '06', '07', '08', '09',
                                    '10', '11', '12', '13', '14', '15', '16', '17', '18',
                                    '19', '20', '21', '22', '23', '24', '25', '26', '27',
                                    '28', '29', '30', '31', '32', '33', '34', '35', '36',
                                    '37', '38', '39', '40', '41', '42', '43', '44', '45',
                                    '46', '47', '48', '49', '50', '51', '52', '53', '54',
                                    '56', '57', '58', '59')
        self.c_segundos.current(0)
        self.c_segundos.place(x=210, y=40)

        self.l_periodo = Label(self.frame_corpo, text='Periodo', bg=self.cor2, fg=self.cor3, relief=FLAT,
                               font=('Arial 10 bold'))
        self.l_periodo.place(x=275, y=15)

        self.c_periodo = ttk.Combobox(self.frame_corpo, width=3, height=2, font=('Arial 15 bold'))
        self.c_periodo['value'] = ('AM', 'PM')
        self.c_periodo.current(0)
        self.c_periodo.place(x=280, y=40)

        self.l_linha1 = Label(self.frame_corpo, text='', bg=self.cor4, relief=FLAT)
        self.l_linha1.place(x=0, y=85, width=400, height=5)

        self.selecionar = IntVar()
        self.radio = Radiobutton(self.frame_rodape, command=self.aticar_alarme, text='Ativado', value=1, variable=self.selecionar, font=('Arial 12 bold'),
                                 bg=self.cor3, fg=self.cor2)
        self.radio.place(x=90, y=0)

    # 7° passo : criar funções
    def aticar_alarme(self):
        if self.selecionar.get() == 1:
            print('Ativado ', self.selecionar.get())
        else:
            self.t1 = Thread(target=self.alarme)

            self.t1.start()

    def desativar_alarme(self):
        print('Alarme Desativado: ', self.selecionar.get())
        mixer.music.stop()
        self.selecionar.set(0)

    def tocar_alarme(self):
        mixer.music.load('alarme.mp3')
        mixer.music.play(loops=10)

        self.desativar = Radiobutton(self.frame_rodape, command=self.desativar_alarme, text='Desativado', value=0, variable=self.selecionar,
                                     font=('Arial 12 bold'),
                                     bg=self.cor3, fg=self.cor2)
        self.desativar.place(x=180, y=0)
        sleep(10)

        if self.selecionar != 0:
            mixer.music.load('alarme.mp3')
            mixer.music.play(loops=10)

    def alarme(self):
        while True:
            self.controle = self.selecionar.get()
            h_hora = self.c_horas.get()
            m_minuto = self.c_minutos.get()
            s_segundo = self.c_segundos.get()
            p_periodo = self.c_periodo.get()

            self.hora_atual = datetime.now()

            hora = self.hora_atual.strftime('%I')
            minuto = self.hora_atual.strftime('%M')
            segundo = self.hora_atual.strftime('%S')
            periodo = self.hora_atual.strftime('%p')

            if self.controle == 1:
                if p_periodo == periodo:
                    if h_hora == hora:
                        if m_minuto == minuto:
                            if s_segundo == segundo:
                                self.tocar_alarme()
                                self.aticar_alarme()
                                messagebox.showinfo('Pausa', 'Hora de vazer uma pausa')
            sleep(0.5)

    def variaveis(self):
        self.t1 = Thread(target=self.alarme)
        self.t1.start()
        mixer.init()




    # 8° passo : cores
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
        self.cor10 = '#9e9e9e'  #
        self.cor11 = '#00cc99'  # verde tela
        self.cor12 = "#f04141"  # vermelho
        self.cor13 = "#59b356"  # verde
        self.cor14 = "#cdd1cd"  # cizenta

Alarme()






















