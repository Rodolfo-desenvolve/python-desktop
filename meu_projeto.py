# 0° passo : importar as bibliotecas
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from dbb import *

# 1° passo : criar minha janela
janela = Tk()


# 2° passo opcional : criar classe
class Agenda_Tarefas:
    # 3° passo : criar um construtor para a classe
    def __init__(self):
        self.janela = janela
        self.cores()
        self.config_tela()
        self.config_frames()
        self.config_widghts()
        self.mostrar()
        self.janela.mainloop()

    # 4° passo : configurar a janela
    def config_tela(self):
        self.janela.title('')
        self.janela.geometry('500x250')
        self.janela.configure(bg=self.cor3)
        self.janela.resizable(False, False)

    # 5° passo : dividir os frames de tela
    def config_frames(self):
        self.frame_titulo = Frame(self.janela, width=210, height=50, bg=self.cor2, highlightbackground=self.cor11,
                                  highlightthickness=2)
        self.frame_titulo.grid(row=0, column=0)

        self.frame_botoes = Frame(self.janela, width=210, height=50, bg=self.cor6, highlightbackground=self.cor11,
                                  highlightthickness=2)
        self.frame_botoes.grid(row=0, column=1)

        self.frame_esquerda = Frame(self.janela, width=210, height=200, bg=self.cor14, highlightbackground=self.cor2,
                                    highlightthickness=2)
        self.frame_esquerda.grid(row=1, column=0)

        self.frame_direita = Frame(self.janela, width=210, height=200, bg=self.cor3, highlightthickness=2,
                                   highlightbackground=self.cor2)
        self.frame_direita.grid(row=1, column=1)

        self.frame_img = Frame(self.janela, width=80, height=250, bg=self.cor2, highlightbackground=self.cor11,
                               highlightthickness=2)
        self.frame_img.place(x=420, y=0)

    # 6° passo : criar widghts
    def config_widghts(self):

        self.l_titulo = Label(self.frame_titulo, text='TAREFAS', bg=self.cor2, fg=self.cor11, relief=FLAT,
                              font=('Verdana 18 bold'))
        self.l_titulo.place(x=10, y=10, width=130, height=30)

        self.icon = Image.open('lista.png')
        self.icon = self.icon.resize((40, 40))
        self.icon = ImageTk.PhotoImage(self.icon)
        self.l_icon = Label(self.frame_titulo, image=self.icon, bg=self.cor2, fg=self.cor11, relief=FLAT)
        self.l_icon.place(x=160, y=2)

        self.img1 = Image.open('acordar.png')
        self.img1 = self.img1.resize((50, 45))
        self.img1 = ImageTk.PhotoImage(self.img1)
        self.l_img1 = Label(self.frame_img, image=self.img1, bg=self.cor2, relief=FLAT)
        self.l_img1.place(x=10, y=0)

        self.img2 = Image.open('bola.png')
        self.img2 = self.img2.resize((50, 45))
        self.img2 = ImageTk.PhotoImage(self.img2)
        self.l_img2 = Label(self.frame_img, image=self.img2, bg=self.cor2, relief=FLAT)
        self.l_img2.place(x=10, y=48)
        self.img3 = Image.open('celular.png')
        self.img3 = self.img3.resize((50, 45))
        self.img3 = ImageTk.PhotoImage(self.img3)
        self.l_img3 = Label(self.frame_img, image=self.img3, bg=self.cor2, relief=FLAT)
        self.l_img3.place(x=10, y=97)

        self.img4 = Image.open('estudar.png')
        self.img4 = self.img4.resize((50, 45))
        self.img4 = ImageTk.PhotoImage(self.img4)
        self.l_img4 = Label(self.frame_img, image=self.img4, bg=self.cor2, relief=FLAT)
        self.l_img4.place(x=10, y=147)

        self.img5 = Image.open('limpar.png')
        self.img5 = self.img5.resize((50, 45))
        self.img5 = ImageTk.PhotoImage(self.img5)
        self.l_img5 = Label(self.frame_img, image=self.img5, bg=self.cor2, relief=FLAT)
        self.l_img5.place(x=10, y=195)

        self.b_salvar = Button(self.frame_botoes, text='SALVAR', bg=self.cor13, fg=self.cor8, relief=RAISED,
                               overrelief=RIDGE, font=('Ivy 10 bold'), command=lambda: self.main('NOVO'))
        self.b_salvar.place(x=1, y=1, width=65, height=45)

        self.b_delete = Button(self.frame_botoes, text='DELETE', bg=self.cor12, fg=self.cor8, relief=RAISED, overrelief=RIDGE,
                               font=('Ivy 10 bold'), command=self.remover)
        self.b_delete.place(x=66, y=1, width=65, height=45)

        self.b_atualizar = Button(self.frame_botoes, text='ATUALIZAR', bg=self.cor9, fg=self.cor8, relief=RAISED,
                                  overrelief=RIDGE, font=('Ivy 10 bold'), command=lambda: self.main('ATUALIZAR'))
        self.b_atualizar.place(x=131, y=1, width=76, height=45)

        self.lb_lista = Listbox(self.frame_direita, font=('Verdana 7 bold'), highlightbackground=self.cor2,
                                highlightthickness=2)
        self.lb_lista.place(x=0, y=0, width=205, height=195)

    # 7° passo : funções
    def main(self, botao):
        if botao == 'NOVO':

            for width in self.frame_esquerda.winfo_children():
                width.destroy()

            def adicionar():
                self.tarefa = self.e_entrada.get()
                inserir([self.tarefa])
                self.mostrar()
                self.e_entrada.delete(0, END)

            self.l_tarefa = Label(self.frame_esquerda, text='ADICIONE TAREFA', bg=self.cor14, fg=self.cor6,
                                  relief=FLAT, anchor=CENTER, font=('Arial 10 bold'))
            self.l_tarefa.place(x=20, y=60, width=170, height=20)

            self.e_entrada = Entry(self.frame_esquerda, bg=self.cor14, fg=self.cor6, relief=SOLID,
                                   font=('Verdana 10 bold'))
            self.e_entrada.place(x=0, y=120, width=205, height=30)

            self.b_adicionar = Button(self.frame_esquerda, text='ADICIONAR', bg=self.cor14, fg=self.cor5,
                                      relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'),command=adicionar)
            self.b_adicionar.place(x=0, y=155, width=205, height=40)

        if botao == 'ATUALIZAR':
            for width in self.frame_esquerda.winfo_children():
                width.destroy()

            def on():
                self.l_tarefa = Label(self.frame_esquerda, text='ATUALIZAR TAREFA', bg=self.cor14, fg=self.cor6, relief=FLAT,
                                      anchor=CENTER, font=('Arial 10 bold'))
                self.l_tarefa.place(x=20, y=60, width=170, height=20)

                self.e_entrada = Entry(self.frame_esquerda, bg=self.cor14, fg=self.cor6, relief=SOLID, font=('Verdana 10 bold'))
                self.e_entrada.place(x=0, y=120, width=205, height=30)

                v_seleciona = self.lb_lista.curselection()[0]
                palavra = self.lb_lista.get(v_seleciona)
                self.e_entrada.insert(0, palavra)

                self.tarefas = selecionar()

                def alterar():
                    for e in self.tarefa:
                        if palavra == e[1]:
                            nova = [self.e_entrada.get(), e[0]]
                            atualizar(nova)
                            self.e_entrada.delete(0, END)
                    self.mostrar()

                self.b_atualizar = Button(self.frame_esquerda, text='ATUALIZAR', bg=self.cor14, fg=self.cor8, relief=RAISED,
                                          overrelief=RIDGE, font=('Arial 10 bold'), command=alterar)
                self.b_atualizar.place(x=0, y=155, width=205, height=40)
            on()

    def remover(self):
        v_seleciona = self.lb_lista.curselection()[0]
        palavra = self.lb_lista.get(v_seleciona)

        self.tarefas = selecionar()

        for e in self.tarefas:
            if palavra == e[1]:
                deletar([e[0]])

        self.mostrar()


    def mostrar(self):
        self.lb_lista.delete(0, END)
        self.tarefa = selecionar()
        for e in self.tarefa:
            self.lb_lista.insert(END, e[1])

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
        self.cor11 = '#00cc99' # verde tela
        self.cor12 = "#f04141"  # vermelho
        self.cor13 = "#59b356"  # verde
        self.cor14 = "#cdd1cd"  # cizenta

Agenda_Tarefas()

























