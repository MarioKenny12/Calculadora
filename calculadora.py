from tkinter import *
from tkinter import font


root = Tk()
#Titulo de la aplicación
root.title("Calculadora")
#root.geometry("1200x1200")
#Tamaño de letra de la pantalla
display = Entry(root,font=("Times New Roman",40))
display.grid(row=1,columnspan=10,sticky=W+E)
#Funciones 
i=0
#Funcion para imprimir en pantalla
def escribir(n):
    global i
    display.insert(i,n)
    i+=1
#Funcion para operadores matematicos
def oper(operator):
    global i
    display.insert(i,operator)
    i+=1
#Funcion para borar numero por numero
def borrar():
    display.delete(0, END)
    i=0
#Funcion para borrar toda la pantalla
def clc():
    display_state=display.get()
    if len(display_state):
        display_new_state=display_state[:-1]
        borrar()
        display.insert(0,display_new_state)
    else:
        borrar()
#Funcion para calcular        
def calcula():
    ecuacion=display.get()
    resultado = eval(ecuacion)
    display.delete(0, END)
    display.insert(0,resultado)
    i=0

#BOTONES
#Agregamos botones con el comando (Button)
Button(root,text="1",command=lambda:escribir(1),font=("Times New Roman",40)).grid(row=3,column=1,sticky=W+E)
Button(root,text="2",command=lambda:escribir(2),font=("Times New Roman",40)).grid(row=3,column=2,sticky=W+E)
Button(root,text="3",command=lambda:escribir(3),font=("Times New Roman",40)).grid(row=3,column=3,sticky=W+E)

Button(root,text="4",command=lambda:escribir(4),font=("Times New Roman",40)).grid(row=4,column=1,sticky=W+E)
Button(root,text="5",command=lambda:escribir(5),font=("Times New Roman",40)).grid(row=4,column=2,sticky=W+E)
Button(root,text="6",command=lambda:escribir(6),font=("Times New Roman",40)).grid(row=4,column=3,sticky=W+E)

Button(root,text="7",command=lambda:escribir(7),font=("Times New Roman",40)).grid(row=5,column=1,sticky=W+E)
Button(root,text="8",command=lambda:escribir(8),font=("Times New Roman",40)).grid(row=5,column=2,sticky=W+E)
Button(root,text="9",command=lambda:escribir(9),font=("Times New Roman",40)).grid(row=5,column=3,sticky=W+E)
Button(root,text="0",command=lambda:escribir(0),font=("Times New Roman",40)).grid(row=6,column=2,sticky=W+E)

#Botones de igual
Button(root,text="=",command=lambda:calcula(),font=("Times New Roman",40)).grid(row=6,column=4,sticky=W+E,rowspan=2)
#Botones de borrar
Button(root,text="c",command=lambda:borrar(),font=("Times New Roman",40)).grid(row=2,column=1,sticky=W+E)
#Botones aritmeticos
Button(root,text="+",command=lambda:oper("+"),font=("Times New Roman",40)).grid(row=4,column=4,sticky=W+E)
Button(root,text="-",command=lambda:oper("-"),font=("Times New Roman",40)).grid(row=3,column=4,sticky=W+E)
Button(root,text="*",command=lambda:oper("*"),font=("Times New Roman",40)).grid(row=2,column=3,sticky=W+E)
Button(root,text="÷",command=lambda:oper("÷"),font=("Times New Roman",40)).grid(row=2,column=2,sticky=W+E)
#Botones extras
Button(root,text=",",command=lambda:oper(","),font=("Times New Roman",40)).grid(row=6,column=3,sticky=W+E)
Button(root,text="%",command=lambda:oper("%"),font=("Times New Roman",40)).grid(row=6,column=1,sticky=W+E)
Button(root,text="⌫",command=lambda:clc(),font=("Times New Roman",40)).grid(row=2,column=4,sticky=W+E)

root.mainloop()

