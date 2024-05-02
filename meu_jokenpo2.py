#  meu projeto jokenpoo das 19:00
cor1 = '#f44336' #vermelho
cor2 = '#8cb34a' #verde
cor3 = '#ffee58' # amarelo
cor4 = '#607d8b' # fundo
cor5 = '#004d40' #verde escuro
cor6 = '#f5f5f5' # branco
cor7 = '#fcc058'  # laganja
cor8 = '#333333'  # preto forte
cor9 = '#34eb3d' # + verda

# 0° passo : importar as bibliotecas
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from random import choice

# 1° passo : criar uma janela
janela = Tk()


# 4° passo : configurar a tela
janela.title('')
janela.geometry('300x300')
janela.configure(background=cor6)
janela.resizable(False, False)

# 5° passo : dividir frames
frame_titulo = Frame(janela, bd=2, bg=cor8)
frame_titulo.place(x=0, y=0, width=300, height=50)

frame_cima = Frame(janela, bd=2, bg=cor5)
frame_cima.place(x=0, y=50, width=300, height=70)

frame_baixo = Frame(janela, bd=2, bg=cor4)
frame_baixo.place(x=0, y=120, width=300, height=180)

# 6° passo : configurar widghts
l_titulo = Label(frame_titulo, text='JOKENPÔ', bd=2, bg=cor8, fg=cor7,
                          font=('Ivy 20 bold'), anchor='center', relief=RIDGE)
l_titulo.place(x=75, y=5, width=150, height=40)

pedra = Image.open('pedra.png')
pedra = pedra.resize((50, 40))
pedra = ImageTk.PhotoImage(pedra)
l_pedra = Label(frame_titulo, image=pedra, bg=cor8, fg=cor7,
                font=('Ivy 10 bold'), relief=FLAT)
l_pedra.place(x=10, y=0)

papel = Image.open('papel.png')
papel = papel.resize((50, 40))
papel = ImageTk.PhotoImage(papel)
l_papel = Label(frame_titulo, image=papel, bg=cor8, fg=cor7, font=('Ivy 10 bold'), relief=FLAT)
l_papel.place(x=230, y=0)

linha_verde = Label(frame_cima, text='', bd=2, bg=cor6)
linha_verde.place(x=-2, y=65, width=103, height=20)

linha_amarela = Label(frame_cima, text='', bd=2, bg=cor6)
linha_amarela.place(x=93, y=65, width=103, height=5)

linha_vermelha = Label(frame_cima, text='', bd=2, bg=cor6)
linha_vermelha.place(x=196, y=65, width=102, height=5)

l_voce = Label(frame_cima, text='VOCÊ', bd=2, bg=cor5, fg=cor6)
l_voce.place(x=10, y=45, width=30, height=15)

voce_pontos = Label(frame_cima, text='0', bd=2, bg=cor5, fg=cor6,
                         font=('verdana 25 bold'))
voce_pontos.place(x=80, y=10, width=50, height=30)

l_boot = Label(frame_cima, text='BOOT', bd=2, bg=cor5, fg=cor6)
l_boot.place(x=250, y=45, width=35, height=15)

pc_pontos = Label(frame_cima, text='0', bd=2, bg=cor5, fg=cor6,
                       font=('verdana 25 bold'))
pc_pontos.place(x=190, y=10, width=50, height=30)

l_separar = Label(frame_cima, text=':', bd=2, bg=cor5, fg=cor6,
                       font=('Ivy 25 bold'))
l_separar.place(x=145, y=10, width=10, height=25)

l_pc = Label(frame_baixo, text='', bg=cor4, fg=cor4)
l_pc.place(x=220, y=10)

global voce
global pc
global rondadas
global pontos_voce
global pontos_pc

pontos_voce = 0
pontos_pc = 0
rodadas = 5


def jogar(chute):
    global pontos_pc
    global pontos_voce
    global rodadas

    if rodadas > 0:
        opcao = ['PEDRA', 'PAPEL', 'TESOURA']
        pc = choice(opcao)
        voce = chute

        l_pc['text'] = pc
        l_pc['fg'] = cor8

        # empate ----------------
        if voce == 'PEDRA' and pc == 'PEDRA':
            print('EMPATE')
            linha_amarela['bg'] = cor3
            linha_verde['bg'] = cor6
            linha_vermelha['bg'] = cor6
        elif voce == 'PAPEL' and pc == 'PAPEL':
            print('EMPATE')
            linha_amarela['bg'] = cor3
            linha_verde['bg'] = cor6
            linha_vermelha['bg'] = cor6
        elif voce == 'TESOURA' and pc == 'TESOURA':
            print('EMPATE')
            linha_amarela['bg'] = cor3
            linha_verde['bg'] = cor6
            linha_vermelha['bg'] = cor6

        # 'PEDRA', 'PAPEL', 'TESOURA'
        elif voce == 'PEDRA' and pc == 'PAPEL':
            print('pc ganhou')
            linha_amarela['bg'] = cor6
            linha_verde['bg'] = cor6
            linha_vermelha['bg'] = cor1
            pontos_pc += 10

        elif voce == 'PEDRA' and pc == 'TESOURA':
            print('voce ganhou')
            linha_amarela['bg'] = cor6
            linha_verde['bg'] = cor2
            linha_vermelha['bg'] = cor6
            pontos_voce += 10

        elif voce == 'PAPEL' and pc == 'TESOURA':
            print('pc ganhou')
            linha_amarela['bg'] = cor6
            linha_verde['bg'] = cor6
            linha_vermelha['bg'] = cor1
            pontos_pc += 10

        #'TESOURA' 'PAPEL' 'PEDRA'
        elif voce == 'TESOURA' and pc == 'PAPEL':
            print('Você venceu')
            linha_amarela['bg'] = cor6
            linha_verde['bg'] = cor2
            linha_vermelha['bg'] = cor6
            pontos_voce += 10

        elif voce == 'TESOURA' and pc == 'PEDRA':
            print('pc ganhou')
            linha_amarela['bg'] = cor6
            linha_verde['bg'] = cor6
            linha_vermelha['bg'] = cor1
            pontos_pc += 10

        elif voce == 'PAPEL' and pc == 'PEDRA':
            print('vc ganhou')
            linha_amarela['bg'] =cor6
            linha_verde['bg'] = cor2
            linha_vermelha['bg'] = cor6
            pontos_voce += 10

        rodadas -= 1

        voce_pontos['text'] = pontos_voce
        pc_pontos['text'] = pontos_pc

    else:
        fim_jogo()


# 7° passo : criar função jogar
def iniciar_jogo():
    global bt_pedra
    global bt_papel
    global bt_tesoura
    bt_pedra = Button(frame_baixo, command=lambda: jogar('PEDRA'), text='PEDRA', bg=cor6,
                           font=('Ivy 10'), relief=RIDGE)
    bt_pedra.place(x=22.5, y=70, width=70, height=60)

    bt_papel = Button(frame_baixo,command=lambda: jogar('PAPEL'), text='PAPEL', bg=cor6,
                           font=('Ivy 10'), relief=RIDGE)
    bt_papel.place(x=115, y=70, width=70, height=60)

    bt_tesoura = Button(frame_baixo, command=lambda: jogar('TESOURA'), text='TESOURA', bg=cor6,
                             font=('Ivy 10'), relief=RIDGE)
    bt_tesoura.place(x=207.5, y=70, width=70, height=60)

def fim_jogo():
    global rodadas
    global pontos_voce
    global pontos_pc
    print('Jogo terminou!')

    rodadas = 5
    pontos_voce = 0
    pontos_pc = 0

    bt_pedra.destroy()
    bt_papel.destroy()
    bt_tesoura.destroy()

    jogador_voce = int(voce_pontos['text'])
    jogador_pc = int(pc_pontos['text'])

    print(jogador_pc)
    print(jogador_voce)

    if jogador_voce == jogador_pc:
        app_vencedor = Label(frame_baixo, text='FOI EMPATE!!!', height=1, anchor='center',
                             font=('Ivy 10 bold'), fg=cor3, bg=cor4)
        app_vencedor.place(x=5, y=60)
    elif jogador_voce < jogador_pc:
        app_vencedor = Label(frame_baixo, text='INFELIZMENTE O BOOT GANHOU!!!', height=1, anchor='center',
                             font=('Ivy 10 bold'), fg=cor1, bg=cor4)
        app_vencedor.place(x=5, y=60)
    else:
        app_vencedor = Label(frame_baixo, text='PARABÉNS VOCE GANHOU !!!', height=1, anchor='center',
                             font=('Ivy 10 bold'), fg=cor9, bg=cor4)
        app_vencedor.place(x=5, y=60)

    def jogar_denovo():
        pc_pontos['text'] = '0'
        voce_pontos['text'] = '0'
        app_vencedor.destroy()

        b_novo.destroy()

        iniciar_jogo()

    b_novo = Button(frame_baixo, command=jogar_denovo, text='JOGAR NOVAMENTE', bd=2, bg=cor8, fg=cor6,
                         font=('Ivy 10 bold'), relief=SOLID)
    b_novo.place(x=22.5, y=140, width=250, height=30)




# 6° passo : configurar widghts

bt_calcular = Button(frame_baixo,command=iniciar_jogo, text='JOGAR', bd=2, bg=cor8, fg=cor6,
                          font=('Ivy 10 bold'),relief=SOLID)
bt_calcular.place(x=22.5, y=140, width=250, height=30)


janela.mainloop()
