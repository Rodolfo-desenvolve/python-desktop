# 0° passo : importa a biblioteca projeto 19:00
from tkinter import *
# from tkinter import ttk


# 1° passo : criar janela
janela = Tk()  # Projeto finalizado com sucesso!!!!!!!!!

# 2° passo : criar classe
class Tela_Imc:
    # 3° passo : criar construtor
    def __init__(self):
        self.janela = janela
        self.config_tela()
        self.frames_tela()
        self.widhgts_imc()
        janela.mainloop()

    # 4° passo : configurar janela
    def config_tela(self):
        self.janela.title('')
        self.janela.geometry('425x225')
        self.janela.config(bg='red')

    # 5° passo : configurar frames
    def frames_tela(self):
        self.frame_esquerda = Frame(self.janela, bg='#7986cb')
        self.frame_esquerda.place(x=0, y=0, width=213, height=180)

        self.frame_direita = Frame(self.janela, bg='#ba68c8')
        self.frame_direita.place(x=214, y=0, width=212, height=180)

        self.frame_baixo = Frame(self.janela, bg='#1e3743')
        self.frame_baixo.place(x=0, y=181, width=425, height=55)

    def calcular1(self):
        peso = float(self.entry_peso.get())
        altura = float(self.entry_altura.get())

        imc = peso / (altura ** 2)
        resultado = imc

        if resultado < 16:
            self.lb_res_texto['text'] = 'IMC : Abaixo do peso (GRAU I)'
        elif resultado >= 16 and resultado <= 16.99:
            self.lb_res_texto['text'] ='IMC : Abaixo do peso (GRAU II)'
        elif resultado >= 17 and resultado <= 18.49:
            self.lb_res_texto['text'] = 'IMC : Abaixo do peso (GRAU III)'
        elif resultado >= 18.50 and resultado <= 24.99:
            self.lb_res_texto['text'] = 'IMC : Peso adequado'
        elif resultado >= 25 and resultado <= 29.99:
            self.lb_res_texto['text'] = 'IMC : Sobrepeso'
        elif resultado >= 30 and resultado <= 34.99:
            self.lb_res_texto['text'] = 'IMC : Obesidade (GRAU I)'
        elif resultado >= 35 and resultado <= 39.99:
            self.lb_res_texto['text'] = 'IMC : Obesidade (GRAU II)'
        else:
            self.lb_res_texto['text'] = 'IMC : Obesidade (GRAU III)'

        self.lb_res['text'] = '{:.{}f}'.format(resultado, 2)
    def calcular2(self):
        peso = float(self.peso_entry.get())
        altura = float(self.altura_entry.get())
        imc = peso / (altura**2)
        resultado = imc
        if resultado < 16:
            self.lb_resul_texto['text'] = 'IMC : Abaixo do peso (GRAU I)'
        elif resultado >= 16 and resultado <=16.99:
            self.lb_resul_texto['text'] = 'IMC : Abaixo do peso (GRAU II)'
        elif resultado >= 17 and resultado <= 18.49:
            self.lb_resul_texto['text'] = 'IMC : Abaixo do peso (GRAU III)'
        elif resultado >= 18.50 and resultado <= 24.99:
            self.lb_resul_texto['text'] = 'IMC : Peso adequado'
        elif resultado >= 25 and resultado <= 29.99:
            self.lb_resul_texto['text'] = 'IMC : Sobrepeso'
        elif resultado >= 30 and resultado <= 34.99:
            self.lb_resul_texto['text'] = 'IMC : Obesidade (GRAU I)'
        elif resultado >= 35 and resultado <= 39.99:
            self.lb_resul_texto['text'] = 'IMC : Obesidade (GRAU II)'
        else:
            self.lb_resul_texto['text'] = 'IMC : Obesidade (GRAU III)'


        self.lb_resultado['text'] = '{:.{}f}'.format(resultado, 2)

    # 6° passo : criar widghts
    def widhgts_imc(self):
        self.lb_principal = Label(self.frame_baixo, text='CALCULADORA DE IMC', bg='#1e3743', fg='white',
                                  font=('Ivy 15 bold'))
        self.lb_principal.place(x=100, y=10, width=225, height=20)

        self.lb_masculino = Label(self.frame_esquerda, text='IMC MASCULINO', bd=2, bg='#7986cb',
                                  fg='#1e3743', font=('Ivy 10 bold'))
        self.lb_masculino.place(x=25, y=10, width=150, height=10)

        self.lb_feminino = Label(self.frame_direita, text='IMC FEMININO', bd=2, bg='#ba68c8', fg='#1e3743',
                                 font=('Ivy 10 bold'))
        self.lb_feminino.place(x=25, y=10, width=150, height=10)

        self.lb_peso = Label(self.frame_esquerda, text='Insira seu peso:', bd=2, bg='#7986cb', fg='#1e3743',
                             font=('Ivy 10 bold'))
        self.lb_peso.place(x=10, y=30, width=100, height=15)

        self.peso_entry = Entry(self.frame_esquerda, bd=2, bg='#7986cb', fg='#1e3743',
                                font=('Ivy 10 bold'))
        self.peso_entry.place(x=120, y=30, width=30, height=20)

        self.lb_altura = Label(self.frame_esquerda,text='Insira sua altura:', bd=2, bg='#7986cb', fg='#1e3743',
                               font=('Ivy 10 bold'))
        self.lb_altura.place(x=10, y=60, width=105, height=15)

        self.altura_entry = Entry(self.frame_esquerda, bd=2, bg='#7986cb', fg='#1e3743',
                                  font=('Ivy 10 bold'))
        self.altura_entry.place(x=120, y=60, width=30, height=20)

        self.lb_resultado = Label(self.frame_esquerda, text='00.00', bd=2, bg='#1e3743', fg='white',
                                  font=('Ivy 10 bold'))
        self.lb_resultado.place(x=155, y=30, width=50, height=50)

        self.lb_resul_texto = Label(self.frame_esquerda, text='', bd=2, bg='#7986cb', fg='yellow',
                                    font=('Ivy 9 bold'))
        self.lb_resul_texto.place(x=10, y=110, width=200, height=20)

        self.bt_calcular = Button(self.frame_esquerda, text='Calcular', bd=2, bg='#1e3743', fg='white',
                                  font=('Ivy 10 bold'),command=self.calcular2)
        self.bt_calcular.place(x=5, y=150, width=200, height=25)
        # -----------------------------------------------------------------------------------------------
        self.lb_pe = Label(self.frame_direita, text='Insira seu peso:', bd=2, bg='#ba68c8', fg='#1e3743',
                           font=('Ivy 10 bold'))
        self.lb_pe.place(x=10, y=30, width=100, height=20)

        self.entry_peso = Entry(self.frame_direita, bd=2, bg='#ba68c8', fg='#1e3743',
                                font=('Ivy 10 bold'))
        self.entry_peso.place(x=120, y=30, width=30, height=20)

        self.lb_al = Label(self.frame_direita, text='Insira sua altura:', bd=2, bg='#ba68c8', fg='#1e3743',
                           font=('Ivy 10 bold'))
        self.lb_al.place(x=10 , y=60, width=105, height=20)

        self.entry_altura = Entry(self.frame_direita, bd=2, bg='#ba68c8', fg='#1e3743', font=('Ivy 10 bold'))
        self.entry_altura.place(x=120, y=60, width=30, height=20)

        self.lb_res = Label(self.frame_direita, text='00.00', bd=2, bg='#1e3743', fg='white', font=('Ivy 10 bold'))
        self.lb_res.place(x=155, y=30, width=50, height=50)

        self.lb_res_texto = Label(self.frame_direita, text='', fg='yellow', bg='#ba68c8', bd=2,
                                  font=('Ivy 9 bold'))
        self.lb_res_texto.place(x=10, y=110, width=200, height=30)

        self.bt_calcul = Button(self.frame_direita, text='Calcular', bd=2, bg='#1e3743', fg='white',
                                font=('Ivy 10 bold'),command=self.calcular1)
        self.bt_calcul.place(x=5, y=150, width=200, height=25)

    # 8° passo : funções para calcular imc
Tela_Imc()

# serão 3 frames para esse projeto
