from tkinter import *
import random
def verificar_palpite():
    palpite = int(caixatexto.get())
    if palpite == numero_secreto:
        resultado ["text"] = "Parabéns! Você acertou"
    else :
        resultado ["text"] = "Errou! Tente novamente."
numero_secreto = random.randint(0,10)

janela = Tk()
janela.title("Jogo")
janela.geometry("280x380")
janela.resizable(False,False)

instrucoes = Label(janela,text = "Digite um número de 1 a 10")
instrucoes.pack(pady = 20)

caixatexto = Entry(janela)
caixatexto.pack(padx=10,pady=10)

botao = Button(janela,text="ENVIAR",pady=14,padx=14,bd=4,command=verificar_palpite)
botao.place(x=180,y=170)

resultado = Label (janela,text="")
resultado.place(x=70,y=220)

janela.mainloop()