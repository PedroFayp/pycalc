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
window.geometry("360x450")
window.config(bg = cor6)

#frames

frame_tela = Frame(window, width = 360, height = 100, bg = cor2)
frame_tela.grid(row = 0, column = 0)


frame_num = Frame(window, width = 360, height = 400)
frame_num.grid(row = 1, column = 0)

#botoes

b1 = Button(frame_num, text = "C", width = 17, height = 3, bg = cor3, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b1.place(x = 0, y = 0)

b2 = Button(frame_num, text = "%", width = 8, height = 3, bg = cor3, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b2.place(x = 180, y = 0)

b3 = Button(frame_num, text = "/", width = 8, height = 3, bg = cor4, fg = cor2, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b3.place(x = 270, y = 0)

b4 = Button(frame_num, text = "7", width = 8, height = 3, bg = cor3, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b4.place(x = 0, y = 70)

b5 = Button(frame_num, text = "8", width = 8, height = 3, bg = cor3, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b5.place(x = 90, y = 70)

b6 = Button(frame_num, text = "9", width = 8, height = 3, bg = cor3, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b6.place(x = 180, y = 70)

b7 = Button(frame_num, text = "*", width = 8, height = 3, bg = cor4, fg = cor2, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b7.place(x = 270, y = 70)

b8 = Button(frame_num, text = "4", width = 8, height = 3, bg = cor3, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b8.place(x = 0, y = 140)

b9 = Button(frame_num, text = "5", width = 8, height = 3, bg = cor3, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b9.place(x = 90, y = 140)

b10 = Button(frame_num, text = "6", width = 8, height = 3, bg = cor3, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b10.place(x = 180, y = 140)

b11 = Button(frame_num, text = "-", width = 8, height = 3, bg = cor4, fg = cor2, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b11.place(x = 270, y = 140)

b12 = Button(frame_num, text = "1", width = 8, height = 3, bg = cor3, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b12.place(x = 0, y = 210)

b13 = Button(frame_num, text = "2", width = 8, height = 3, bg = cor3, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b13.place(x = 90, y = 210)

b14 = Button(frame_num, text = "3", width = 8, height = 3, bg = cor3, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b14.place(x = 180, y = 210)

b15 = Button(frame_num, text = "+", width = 8, height = 3, bg = cor4, fg = cor2, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b15.place(x = 270, y = 210)

b16 = Button(frame_num, text = "0", width = 17, height = 3, bg = cor3, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b16.place(x = 0, y = 280)

b17 = Button(frame_num, text = ".", width = 8, height = 3, bg = cor3, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b17.place(x = 180, y = 280)

b18 = Button(frame_num, text = "=", width = 8, height = 3, bg = cor4, fg = cor2, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b18.place(x = 270, y = 280)


window.mainloop()