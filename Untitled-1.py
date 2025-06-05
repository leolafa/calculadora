import tkinter
from tkinter import *
from tkinter import ttk

#cria a janela principal
janela= Tk()
janela.title("calculadora magica 🪄 🎩")
janela.geometry('400x310')
janela.configure(bg="light blue")
#estilo do tema
style= ttk.Style()
style.theme_use("clam")
ttk.Separator(janela, orient=HORIZONTAL ).grid(row=0, columnspan=1, ipadx=1)

#titulo da aplicação
frame_cima=Frame(janela, width=400, height=60, bg="light blue", pady=0, padx=0)
frame_cima.grid(row=1, column=0)

frame_baixo=Frame(janela, width=400, height=300, bg="light blue", pady=12, padx=20)
frame_baixo.grid(row=2, column=0, sticky=NW)

#titulo principal
nome_principal= Label(frame_cima, text="Calculadora magica 🪄 🎩", relief=FLAT,anchor='center', font=('Arial 14'), bg="white", fg="black")
nome_principal.place(x=10, y=15)

#funçao conversao
def converter():
    #converte decimal para binario
    def numero_para_decimal(numero, base):

        decimal= int(numero,base)
        binario= bin(decimal)

        n_decimal['text']=str(decimal)
        n_binario['text']= str(binario[2:])
        
    numero= valor_conver.get()
    base= combo.get()


#converte o texto para numero
    if base== 'Binario':
        base= 2
    elif base =='Decimal':
        base= 10
#chama a funçao conversao
    numero_para_decimal(numero, base)


#opçoes do combobox
bases=['Binario', 'Decimal']

#escolher a entrada
combo= ttk.Combobox(frame_baixo, width=12, justify=CENTER, font=('Arial 12'))
combo ['values'] = (bases)
combo.place(x=35, y=10 )

#entrada do numero
valor_conver= Entry(frame_baixo, width=9, justify='center', font='Arial 13', highlightthickness=
                    1, relief='solid')
valor_conver.place(x=160, y=10)
#botao conversao
botao_converter= Button(frame_baixo, command=converter, text="CONVERTER", relief=RAISED,overrelief=RIDGE, font=('Arial 8 bold'), bg="white", fg="black")
botao_converter.place(x=247, y=10)
#binario
n_binario= Label(frame_baixo, text="BINÁRIO", width=12, relief=FLAT,anchor='nw', font=('Arial 12'), bg="orange", fg="black")
n_binario.place(x=30, y=40)

#mostra o valor binario
n_binario= Label(frame_baixo, text="", width=13, relief=FLAT,anchor='center', font=('Arial 12'), bg="white", fg="black")
n_binario.place(x=170, y=40)

#,,,,,

#decimal
n_decimal= Label(frame_baixo, text="DECIMAL", width=12, relief=FLAT,anchor='nw', font=('Arial 12'), bg="orange", fg="black")
n_decimal.place(x=30, y=80)

#mostra o valor em decimal
n_decimal= Label(frame_baixo, text="", width=13, relief=FLAT,anchor='center', font=('Arial 12'), bg="white", fg="black")
n_decimal.place(x=170, y=80)



#inicia a janela
janela.mainloop()