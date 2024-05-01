# 0° passo : importa biblitecas
from tkinter import *


# 1° passo : criar janela
janela = Tk()


# 2° passo : criar classe para organização
class Patrimonio:
    # 3° passo : criar construtor
    def __init__(self):
        self.janela = janela
        self.cores()
        self.config_tela()
        self.frames_tela()
        self.widghts_tela()
        janela.mainloop()

    # 4° passo : configurações da tela
    def config_tela(self):
        self.janela.title('')
        self.janela.geometry('500x300')
        self.janela.config(background=self.cor4)
        self.janela.resizable(False, False)

    # 5° passo : frames tela
    def frames_tela(self):
        self.frame_cima = Frame(self.janela, bd=2, bg=self.cor3)
        self.frame_cima.place(x=0, y=0, width=500, height=50)

        self.frame_esquerda = Frame(self.janela, bd=2, bg=self.cor3)
        self.frame_esquerda.place(x=0, y=100, width=248, height=250)

        self.frame_direita = Frame(self.janela, bd=2, bg=self.cor3)
        self.frame_direita.place(x=252, y=100, width=248, height=200)

        self.frame_resposta = Frame(self.janela, bd=2, bg='#1e3743')
        self.frame_resposta.place(x=125, y=50, width=375, height=50)

        self.frame_botao = Frame(self.janela,bd=2, bg=self.cor3)
        self.frame_botao.place(x=0, y=50, width=125, height=50)

    # 6° passo : widghts
    def widghts_tela(self):
        self.l_nome = Label(self.frame_cima, text='Calculadora De Patrimonio Liquído',
                            bg=self.cor3, fg=self.cor2, font=('verdana 15 bold'))
        self.l_nome.place(x=50, y=0, width=400, height=40)

        self.l_ativos = Label(self.frame_esquerda, text='Ativos', bg='#66cc00', fg=self.cor3,
                              font=('verdana 15 bold'))
        self.l_ativos.place(x=0, y=0, width=246, height=30)

        self.l_passivos = Label(self.frame_direita, text='Passivos', bg='#cc0000', fg=self.cor3,
                                font=('verdana 15 bold'))
        self.l_passivos.place(x=0, y=0, width=246, height=30)

        # frame resposta --------------------------------
        self.l_resposta = Label(self.frame_resposta, text='R${:,.2f}'.format(00), padx=10, width=15, anchor=NE,
                                font=('verdana 25 bold'), bg='#1e3743', fg='white')
        self.l_resposta.place(x=0, y=7)

        self.bt_calcular = Button(self.frame_botao, command=self.calcular, text='CALCULAR', bd=3, font=('Ivy 11 bold'), bg='#1e3743', fg='white')
        self.bt_calcular.place(x=5, y=10, width=105, height=30)

        # frame esquerdo ----------------------------
        self.l_casa = Label(self.frame_esquerda, text='CASAS:', font=('verdana 10 bold'),
                            bd=2, bg=self.cor3, fg=self.cor2)
        self.l_casa.place(x=10, y=45, width=70, height=20)

        self.e_casa = Entry(self.frame_esquerda, font=('verdana 10'), justify='center',relief=SOLID)
        self.e_casa.place(x=150, y=45, width=90, height=20)

        self.l_imoveis = Label(self.frame_esquerda, text='IMOVEIS:', font=('verdana 10 bold'), bg=self.cor3, fg=self.cor2)
        self.l_imoveis.place(x=10, y=70, width=70, height=20)

        self.e_imoveis = Entry(self.frame_esquerda, font=('verdana 10'), justify='center', relief=SOLID)
        self.e_imoveis.place(x=150, y=70, width=90, height=20)

        self.l_veiculos = Label(self.frame_esquerda, text='VEICULOS:', font=('verdana 10 bold'), bg=self.cor3, fg=self.cor2)
        self.l_veiculos.place(x=10, y=100, width=80, height=20)

        self.e_veiculos = Entry(self.frame_esquerda, font=('verdana 10'), justify='center', relief=SOLID)
        self.e_veiculos.place(x=150, y=100, width=90, height=20)

        self.l_investimentos = Label(self.frame_esquerda, text='INVESTIMENTOS:', font=('verdana 10 bold'), bg=self.cor3,
                                     fg=self.cor2)
        self.l_investimentos.place(x=10, y=130, width=120, height=20)

        self.e_investimentos = Entry(self.frame_esquerda, font=('verdana 10'), justify='center', relief=SOLID)
        self.e_investimentos.place(x=150, y=130, width=90, height=20)

        self.L_outros = Label(self.frame_esquerda, text='OUTROS ATIVOS:', font=('verdana 10 bold'), bg=self.cor3,
                              fg=self.cor2)
        self.L_outros.place(x=10, y=160, width=120, height=20)

        self.e_outros = Entry(self.frame_esquerda, font=('verdana 10'), justify='center', relief=SOLID)
        self.e_outros.place(x=150, y=160, width=90, height=20)

        # frame direito ----------------------------
        self.l_hipoteca = Label(self.frame_direita, text='HIPOTECA:', font=('verdana 10 bold'), bg=self.cor3, fg=self.cor2)
        self.l_hipoteca.place(x=10, y=45,width=80, height=20)

        self.e_hipoteca = Entry(self.frame_direita, font=('verdana 10'), justify='center', relief=SOLID)
        self.e_hipoteca.place(x=150, y=45, width=90, height=20)

        self.l_emprestimo_carro = Label(self.frame_direita, text='EMPRESTIMO CARRO',font=('verdana 9 bold'),
                                        bg=self.cor3, fg=self.cor2)
        self.l_emprestimo_carro.place(x=5, y=70,width=140, height=20)

        self.e_emprestimo_carro = Entry(self.frame_direita, font=('verdana 10'), justify='center', relief=SOLID)
        self.e_emprestimo_carro.place(x=150, y=70, width=90, height=20)

        self.l_estudantil = Label(self.frame_direita, text='DIVIDA ESTUDANTIL', font=('verdana 9 bold'),
                                  bg=self.cor3, fg=self.cor2)
        self.l_estudantil.place(x=5, y=100, width=140, height=20)

        self.e_estudantil = Entry(self.frame_direita, font=('verdana 10'), justify='center', relief=SOLID)
        self.e_estudantil.place(x=150, y=100, width=90, height=20)

        self.l_dividas = Label(self.frame_direita, text='OUTRAS DIVIDAS', font=('verdana 9 bold'),
                                  bg=self.cor3, fg=self.cor2)
        self.l_dividas.place(x=5, y=125, width=120, height=20)

        self.e_dividas = Entry(self.frame_direita, font=('verdana 10'), justify='center', relief=SOLID)
        self.e_dividas.place(x=150, y=125, width=90, height=20)
    # 7° passo : criar a função de calculo

    def variaveis(self):
        #variaveis dos ativos -----------
        self.casa = self.e_casa.get()
        self.imoveis = self.e_imoveis.get()
        self.veiculos = self.e_veiculos.get()
        self.investimentos = self.e_investimentos.get()
        self.outros_ativ = self.e_outros.get()
        #variaveis dos passivos ------------
        self.hipoteca = self.e_hipoteca.get()
        self.emp_carro = self.e_emprestimo_carro.get()
        self.estudantil = self.e_estudantil.get()
        self.divida = self.e_dividas.get()

    def calcular(self):
        self.variaveis()

        if self.casa == '' or self.imoveis == '' or self.veiculos == '' or self.investimentos == ''or self.outros_ativ == ''\
                or self.hipoteca == '' or self.emp_carro == ''or self.estudantil == '' or self.divida== '':
            return
        else:
            # total de valores ativos ----------
            total_ativo = float(self.casa) + float(self.imoveis) + float(self.veiculos) + float(self.investimentos) + float(self.outros_ativ)

            # total de valores passivos------------
            total_passivo = float(self.hipoteca) + float(self.emp_carro) + float(self.estudantil) + float(self.divida)

        liquido = total_ativo + total_passivo

        self.l_resposta['text'] = 'R${:,.2f}'.format(liquido)


    def cores(self):
        self.cor1 = '#3b3b3b'  # preto leve
        self.cor2 = '#333333'  # preto forte
        self.cor3 = '#ffffff'  # branco
        self.cor4 = '#fcc058'  # laganja


Patrimonio()




















