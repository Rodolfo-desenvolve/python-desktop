# 0° passo : importar bibliotecas
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random


cor1 = '#3b3b3b'  # preto leve
cor2 = '#333333'  # preto forte
cor3 = '#ffffff'  # branco
cor4 = '#fcc058'  # laganja
cor5 = '#5C7CFA'  # azul
cor6 = '#1e3743'  # azul
cor7 = '#9900cc'  # roxo
cor8 = '#e1f5fe'  # azul claro
cor9 = '#ffca28'  # amarelo
cor10 = '#9e9e9e'  # cinza
co0 = '#444466'  # preta
co1 = '#feffff'  # branca
co2 = '#6f9fbd'  # azul
co3 = '#38576b'  # valor
co4 = '#403d3d'  # letra
co5 = '#e06636'  # - profit
co6 = '#6dd695'  # + profit
co7 = '#ef5350'  # vermelho
fundo = '#3b3b3b'
co10 = '#fcfbf7'
ccor1 = '#f58b5b'
ccor2 = '#ff333a'
ccor3 = '#6bd66f'
ccor4 = '#ab8918'

# 1° passo : criar janela


janela = Tk()

janela.title('')
janela.geometry('525x277')
janela.configure(bg=cor3)
janela.resizable(False, False)

frame_top = Frame(janela, width=375, height=50, bg=cor6)
frame_top.place(x=75, y=0)

frame_corpo = Frame(janela, width=375, height=227, bg='lightgray')
frame_corpo.place(x=75, y=50)

frame_esquerda = Frame(janela, width=75, height=277, bg=ccor3, highlightbackground=co7,
                       highlightthickness=2)
frame_esquerda.place(x=0, y=0)

frame_direita = Frame(janela, width=75, height=277, bg=ccor3,highlightbackground=co7,
                       highlightthickness=2)
frame_direita.place(x=450, y=0)


l_nome = Label(frame_top, text='ADIVINHANDO ANIMAL', bg=cor6, fg=cor3, relief=RIDGE,
                font=('Ivy 16 bold'))
l_nome.place(x=65, y=10, width=250)


tentativas = 5
pontuacao = 0


# 7° passo : criar funções
def config_funcoes():
    l_regra['text'] = ''
    l_regra1['text'] = ''
    l_regra2['text'] = ''

    lista_computador = ['CAMALEÃO', 'FLAMINGO', 'BEIJA-FLOR', 'GATO', 'CACHORRO',
                             'GOLFINHO', 'ABELHA', 'URSO-POLAR', 'ELEFANTE', 'LONTRA']
    resposta = random.choice(lista_computador)
    l_computador['text'] = resposta

    def valores_botoes(i):
        lista_computador = ['CAMALEÃO', 'FLAMINGO', 'BEIJA-FLOR', 'GATO', 'CACHORRO',
                                 'GOLFINHO', 'ABELHA', 'URSO-POLAR', 'ELEFANTE', 'LONTRA']
        resposta = [random.choice(lista_computador)]
        l_computador['text'] = resposta

        global tentativas
        global pontuacao

        for e in resposta:
            if i == e:
                tentativas += 2
                pontuacao += 10
                l_tentativa['text'] = str(tentativas) + 'Tentativas: '
                l_pontos['text'] = str(pontuacao) + 'Pontuação: '
            else:
                tentativas -= 1
                l_tentativa['text'] = str(tentativas) + 'Tentativas'
                if tentativas <= 0:
                    b_img1['state'] = 'disable'
                    b_img2['state'] = 'disable'
                    b_img3['state'] = 'disable'
                    b_img4['state'] = 'disable'
                    b_img5['state'] = 'disable'
                    b_img6['state'] = 'disable'
                    b_img7['state'] = 'disable'
                    b_img8['state'] = 'disable'
                    b_img9['state'] = 'disable'
                    b_img10['state'] = 'disable'

                    b_img1['text'] = ''
                    b_img2['text'] = ''
                    b_img3['text'] = ''
                    b_img4['text'] = ''
                    b_img5['text'] = ''
                    b_img6['text'] = ''
                    b_img7['text'] = ''
                    b_img8['text'] = ''
                    b_img9['text'] = ''
                    b_img10['text'] = ''

                    game_over()

                else:
                    pass

    b_img1 = Button(frame_corpo, text='CAMALEÃO', bg=cor5, relief=RIDGE, overrelief=RIDGE,
                         font=('Ivy 8 bold'), command=lambda: valores_botoes('CAMALEÃO'))
    b_img1.place(x=10, y=55, width=70, height=50)

    b_img2 = Button(frame_corpo, text='FLAMINGO', bg=cor5, relief=RIDGE, overrelief=RIDGE,
                         font=('Ivy 8 bold'), command=lambda: valores_botoes('FLAMINGO'))
    b_img2.place(x=80, y=55,  width=70, height=50)

    b_img3 = Button(frame_corpo, text='BEIJA-FLOR', bg=cor5, relief=RIDGE, overrelief=RIDGE,
                         font=('Ivy 8 bold'), command=lambda: valores_botoes('BEIJA-FLOR'))
    b_img3.place(x=150, y=55,  width=75, height=50)

    b_img4 = Button(frame_corpo, text='GATO', bg=cor5, relief=RIDGE, overrelief=RIDGE,
                         font=('Ivy 8 bold'), command=lambda: valores_botoes('GATO'))
    b_img4.place(x=225, y=55,  width=70, height=50)

    b_img5 = Button(frame_corpo, text='CACHORRO', bg=cor5, relief=RIDGE, overrelief=RIDGE,
                         font=('Ivy 8 bold'), command=lambda: valores_botoes('CACHORRO'))
    b_img5.place(x=295, y=55,  width=70, height=50)

    b_img6 = Button(frame_corpo, text='GOLFINHO', bg=cor5, relief=RIDGE, overrelief=RIDGE,
                         font=('Ivy 8 bold'), command=lambda: valores_botoes('GOLFINHO'))
    b_img6.place(x=10, y=105,  width=70, height=50)

    b_img7 = Button(frame_corpo, text='ABELHA', bg=cor5, relief=RIDGE, overrelief=RIDGE,
                         font=('Ivy 8 bold'), command=lambda: valores_botoes('ABELHA'))
    b_img7.place(x=80, y=105,  width=70, height=50)

    b_img8 = Button(frame_corpo, text='URSO-POLAR', bg=cor5, relief=RIDGE, overrelief=RIDGE,
                         font=('Ivy 8 bold'), command=lambda: valores_botoes('URSO-POLAR'))
    b_img8.place(x=150, y=105, width=75, height=50)

    b_img9 = Button(frame_corpo, text='ELEFANTE', bg=cor5, relief=RIDGE, overrelief=RIDGE,
                         font=('Ivy 8 bold'), command=lambda: valores_botoes('ELEFANTE'))
    b_img9.place(x=225, y=105,  width=70, height=50)

    b_img10 = Button(frame_corpo, text='LONTRA', bg=cor5, relief=RIDGE, overrelief=RIDGE,
                          font=('Ivy 8 bold'), command=lambda: valores_botoes('LONTRA'))
    b_img10.place(x=295, y=105,  width=70, height=50)

def game_over():
    global tentativas
    global pontuacao
    l_pontuo = Label(frame_corpo, text='Você pontuou :' + str(pontuacao) + 'Pontos', bg=cor1, fg=cor5, relief=FLAT,
                     font=('Ivy 12 bold'))
    l_pontuo.place(x=95, y=90)

    l_tenta = Label(frame_corpo, text='GAME OVER', bg=cor1, fg=cor5, relief=FLAT,
                        font=('Ivy 12 bold'))
    l_tenta.place(x=140, y=120)

    pontuacao = 0
    tentativas = 5

    l_tentativa['text'] = str(tentativas) + 'Tentativas: '
    l_pontos['text'] = 'Pontuação' + str(pontuacao)

    b_jogar = Button(frame_corpo, command=config_funcoes, text='TENTAR NOVAMENTE', bg=cor6, fg=cor3, relief=RAISED,
                     overrelief=RIDGE, font=('Ivy 12 bold'))
    b_jogar.place(x=25, y=170, width=325, height=30)


l_pontos = Label(frame_corpo, text='Pontuação :', bg='lightgray', fg=cor5, relief=FLAT,
                      font=('Ivy 12 bold'))
l_pontos.place(x=10, y=15)

l_tentativa = Label(frame_corpo, text='Tentativas :', bg='lightgray', fg=cor5, relief=FLAT,
                         font=('Ivy 12 bold'))
l_tentativa.place(x=250, y=15)

regra1 = '1 - Tenta adivinhar o ANIMAL para pontuar.'
l_regra = Label(frame_corpo, text=regra1, bg='lightgray', fg=cor6, relief=RIDGE,
                     font=('verdana 10 bold'))
l_regra.place(x=10, y=60, width=355)

regra2 = '2 - Se você acertar, você ganhará + 3 pontos.'
l_regra1 = Label(frame_corpo, text=regra2, bg='lightgray', fg=cor6, relief=RIDGE,
                      font=('verdana 10 bold'))
l_regra1.place(x=10, y=90, width=355)

regra3 = '3 - Se você errar, as suas chances ira reduzir.'
l_regra2 = Label(frame_corpo, text=regra3, bg='lightgray', fg=cor6, relief=RIDGE,
                      font=('verdana 10 bold'))
l_regra2.place(x=10, y=120, width=355)

l_linha = Label(frame_corpo, text='', bg=ccor3, relief=FLAT, font=('Ivy 4 bold'))
l_linha.place(x=10, y=40, width=355)

l_computador = Label(frame_corpo, text='Computador', bg='lightgray', fg=cor5, relief=FLAT, font=('Ivy 10 bold'))
l_computador.place(x=150, y=15)

b_jogar = Button(frame_corpo, command=config_funcoes, text='JOGAR', bg=cor6, fg=cor3, relief=RAISED, overrelief=RIDGE,
                      font=('Ivy 12 bold'))
b_jogar.place(x=25, y=170, width=325, height=30)

img1 = Image.open('animal1.png')
img1 = img1.resize((60, 50))
img1 = ImageTk.PhotoImage(img1)
b_img1 = Label(frame_esquerda, image=img1, bg='lightgray', relief=RIDGE,
                     font=('Ivy 8 bold'))
b_img1.place(x=5, y=2)

img2 = Image.open('animal2.png')
img2 = img2.resize((60, 50))
img2 = ImageTk.PhotoImage(img2)
b_img2 = Label(frame_esquerda, image=img2, bg='lightgray', relief=RIDGE,
                     font=('Ivy 8 bold'))
b_img2.place(x=5, y=55)

img3 = Image.open('animal3.png')
img3 = img3.resize((60, 50))
img3 = ImageTk.PhotoImage(img3)
b_img3 = Label(frame_esquerda, image=img3, bg='lightgray', relief=RIDGE,
                     font=('Ivy 8 bold'))
b_img3.place(x=5, y=108)
#
img4 = Image.open('animal4.png')
img4 = img4.resize((60, 50))
img4 = ImageTk.PhotoImage(img4)
b_img4 = Label(frame_esquerda, image=img4, bg='lightgray', relief=RIDGE,
                     font=('Ivy 8 bold'))
b_img4.place(x=5, y=160)

img5 = Image.open('animal5.png')
img5 = img5.resize((60, 50))
img5 = ImageTk.PhotoImage(img5)
b_img5 = Label(frame_esquerda, image=img5, bg='lightgray', relief=RIDGE,
                     font=('Ivy 8 bold'))
b_img5.place(x=5, y=213)

img6 = Image.open('animal6.png')
img6 = img6.resize((60, 50))
img6 = ImageTk.PhotoImage(img6)
b_img6 = Label(frame_direita, image=img6, bg='lightgray', relief=RIDGE,
                     font=('Ivy 8 bold'))
b_img6.place(x=5, y=2)

img7 = Image.open('animal7.png')
img7 = img7.resize((60, 50))
img7 = ImageTk.PhotoImage(img7)
b_img7 = Label(frame_direita, image=img7, bg='lightgray', relief=RIDGE,
                     font=('Ivy 8 bold'))
b_img7.place(x=5, y=55)

img8 = Image.open('animal8.png')
img8 = img8.resize((60, 50))
img8 = ImageTk.PhotoImage(img8)
b_img8 = Label(frame_direita, image=img8, bg='lightgray', relief=RIDGE,
                     font=('Ivy 8 bold'),)
b_img8.place(x=5, y=108)
#
img9 = Image.open('animal9.png')
img9 = img9.resize((60, 50))
img9 = ImageTk.PhotoImage(img9)
b_img9 = Label(frame_direita, image=img9, bg='lightgray', relief=RIDGE,
                     font=('Ivy 8 bold'))
b_img9.place(x=5, y=160)
#
img10 = Image.open('animal10.png')
img10 = img10.resize((60, 50))
img10 = ImageTk.PhotoImage(img10)
b_img10 = Label(frame_direita, image=img10, bg='lightgray', relief=RIDGE,
                      font=('Ivy 8 bold'))
b_img10.place(x=5, y=212)


janela.mainloop()