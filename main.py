#import tkinter
from tkinter import *
from tkinter import ttk

#cores

cor1 = "#1e1e1e" #preto
cor2 = "#ffffff" #branco
cor3 = "#ECEFF1" #cinza
cor4 = "#c78b46" #laranja
cor5 = "#ad5058" #vermelho
cor6 = "#565c63" #azul

window = Tk()
window.title("Calculadora")
window.geometry("350x500")
window.config(bg= cor6)

frame_tela = Frame(window, width= 350, height= 100)
frame_tela.grid(row = 0, column= 0)

window.mainloop()