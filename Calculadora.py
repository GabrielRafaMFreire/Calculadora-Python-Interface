from tkinter import *
from tkinter import ttk 

#cores

cor1 = "#0a0a0a" #preto
cor2 = "#121417" #azul meio diferenciado
cor3 = "#d4cfcf" #cor cinzenta 
cor4 = "#f5940c" #cor laranja
cor5= "#ffffff" #cor branca


window = Tk()
window.title("Calculadora")
window.geometry("235x318")
window.config(bg=cor1)


#utilizando frames para dividir o display e os botões
frame_tela = Frame(window, width=235, height=50, bg=cor2)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(window, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#criando botões 

b_1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor3)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, text="%", width=5, height=2, bg=cor3)
b_2.place(x=89, y=0)

b_3 = Button(frame_corpo, text="/", width=5, height=2, bg=cor4, fg=cor5)
b_3.place(x=177, y=0)


window.mainloop()