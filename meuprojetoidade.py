# 0° passo : importa bibliteca tkinter Projeto das 19:00
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date

# 1° passo : criar janela
janela = Tk() # projeto finalizado !!!!!!!!!!!!!

# 2° passo : classe para organização
class Calculadora_Idade:
    # 3° passo : criar construtor
    def __init__(self):
        self.janela = janela
        self.cores()
        self.config_tela()
        self.frames_tela()
        self.widhgts()
        janela.mainloop()

    # 4° passo : configura tela
    def config_tela(self):
        self.janela.title('')
        self.janela.geometry('300x400')
        self.janela.config(bg='black')
        self.janela.resizable(False, False)

    # 5° passo : frames de tela
    def frames_tela(self):
        self.frame_topo = Frame(self.janela, bd=2, bg=self.cor1)
        self.frame_topo.place(relx=0, rely=0, relwidth=100,relheight=0.35)

        self.frame_meio = Frame(self.janela, bd=2, bg=self.cor2)
        self.frame_meio.place(relx=0, rely=0.35, relwidth=100, relheight=0.30)

        self.frame_baixo = Frame(self.janela, bd=2, bg=self.cor1)
        self.frame_baixo.place(relx=0, rely=0.65, relwidth=100, relheight=0.35)

    def cores(self):
        self.cor1 = '#3b3b3b'  # preto leve
        self.cor2 = '#333333'  # preto forte
        self.cor3 = '#ffffff'  # branco
        self.cor4 = '#fcc058'  # laganja
    # 6° passo : labels da tela
    def widhgts(self):
        l_linha = Label(self.frame_topo, text='', bd=2, bg=self.cor4,)
        l_linha.place(relx=0, rely=0.98, relwidth=0.6, relheight=0.02)
        l_linha2 = Label(self.frame_meio, text='', bd=2, bg=self.cor4)
        l_linha2.place(relx=0, rely=0.98, relwidth=0.6, relheight=0.02)

        l_atual = Label(self.frame_topo, text='Data Atual :', bd=2, bg=self.cor1, fg=self.cor4,
                        font=('Arial 8 bold'))
        l_atual.place(x=10, y=30, width=100, height=20)
        self.l_calendario1 = DateEntry(self.frame_topo, bg='darkblue', fg=self.cor3, borderwidth=2,
                                       date_pattern='dd/mm/y',y=2023)
        self.l_calendario1.place(x=160, y=30, width=80, height=20)

        l_nascimento = Label(self.frame_topo, text='Data de Nascimento :', bd=2, bg=self.cor1, fg=self.cor4,
                             font=('Arial 8 bold'))
        l_nascimento.place(x=10, y=60, width=120, height=20)
        self.l_calendario2 = DateEntry(self.frame_topo, bg='darkblue', fg=self.cor3, borderwidth=2,
                                       date_pattern='dd/mm/y', y=2023)
        self.l_calendario2.place(x=160, y=60, width=80, height=20)

        l_nome = Label(self.frame_meio, text='CALCULADORA',bd=2, bg=self.cor2, fg=self.cor4,
                       font=('Ivy 20 bold'))
        l_nome.place(x=35, y=0, width=230, height=30)

        l_idade = Label(self.frame_meio, text='DE IDADE', bd=2, bg=self.cor2, fg=self.cor4,
                        font=('Ivy 25 bold'))
        l_idade.place(x=30, y=60, width=250, height=40)

        self.l_anos = Label(self.frame_baixo, text='----', bd=2, bg=self.cor1, fg=self.cor3,
                      font=('Arial 15 bold'))
        self.l_anos.place(x=50, y=30, width=80, height=30)

        l_ano = Label(self.frame_baixo, text='Anos', bd=2, bg=self.cor1, fg=self.cor3,
                      font=('Arial 15 bold'))
        l_ano.place(x=35, y=70, width=50, height=30)

        self.l_meses = Label(self.frame_baixo, text='--', bd=2, bg=self.cor1, fg=self.cor3,
                        font=('Arial 15 bold'))
        self.l_meses.place(x=130, y=30, width=50, height=30)

        l_mes = Label(self.frame_baixo, text='Meses', bd=2, bg=self.cor1, fg=self.cor3,
                      font=('Arial 15 bold'))
        l_mes.place(x=120, y=70, width=60, height=30)

        self.l_dias = Label(self.frame_baixo, text='--', bd=2, bg=self.cor1, fg=self.cor3,
                            font=('Arial 15 bold'))
        self.l_dias.place(x=220, y=30, width=50, height=30)

        l_dia = Label(self.frame_baixo, text='Dias', bd=2, bg=self.cor1, fg=self.cor3,
                      font=('Arial 15 bold'))
        l_dia.place(x=210, y=70, width=50, height=30)
        # 7° passo : botão ta tela
        self.bt_calcular = Button(self.frame_topo, text='Calcular', bd=2, bg=self.cor4, fg=self.cor3,
                                  font=('Arial 10 bold'),command=self.funcoes)
        self.bt_calcular.place(x=20, y=100, width=260, height=30)

    # 8° passo : funções para o botão
    def funcoes(self):
        ano_atual = self.l_calendario1.get()
        nascimento = self.l_calendario2.get()

        dia, mes, ano = [int(f)for f in ano_atual.split('/')]
        data_atual = date(ano,mes, dia)

        dia_2, mes_2, ano_2 = [int(i) for i in nascimento.split('/')]
        data_final = date(ano_2, mes_2, dia_2)

        ano = relativedelta(data_atual, data_final).years
        mes = relativedelta(data_atual, data_final).months
        dia = relativedelta(data_atual, data_final).days

        self.l_anos['text'] = ano
        self.l_meses['text'] = mes
        self.l_dias['text'] = dia


Calculadora_Idade()