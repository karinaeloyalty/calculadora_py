from ctypes import pointer
from tkinter import *
from tkinter import font

ventana = Tk()
ventana.title("Calculadora de Karys")

e_texto = Entry(ventana, font=("arial 25"))
e_texto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

i = 0

#funciones
def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def borrar():
    e_texto.delete(0, END)
    i = 0

def resultado():
    ecuacion = e_texto.get()
    result = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, result)
    i = 0


font = ("arial 16 bold")
bg = "#009999"
color = "#ffffff"
cursor = "tcross"
#Botones
btn1 =  Button(ventana, text="1", width=5, height=2, command=lambda: click_boton(1), font=font, bg=bg, fg=color, cursor=cursor)
btn2 =  Button(ventana, text="2", width=5, height=2, command=lambda: click_boton(2), font=font, bg=bg, fg=color, cursor=cursor)
btn3 =  Button(ventana, text="3", width=5, height=2, command=lambda: click_boton(3), font=font, bg=bg, fg=color, cursor=cursor)
btn4 =  Button(ventana, text="4", width=5, height=2, command=lambda: click_boton(4), font=font, bg=bg, fg=color, cursor=cursor)
btn5 =  Button(ventana, text="5", width=5, height=2, command=lambda: click_boton(5), font=font, bg=bg, fg=color, cursor=cursor)
btn6 =  Button(ventana, text="6", width=5, height=2, command=lambda: click_boton(6), font=font, bg=bg, fg=color, cursor=cursor)
btn7 =  Button(ventana, text="7", width=5, height=2, command=lambda: click_boton(7), font=font, bg=bg, fg=color, cursor=cursor)
btn8 =  Button(ventana, text="8", width=5, height=2, command=lambda: click_boton(8), font=font, bg=bg, fg=color, cursor=cursor)
btn9 =  Button(ventana, text="9", width=5, height=2, command=lambda: click_boton(9), font=font, bg=bg, fg=color, cursor=cursor)
btn0 =  Button(ventana, text="0", width=5, height=2, command=lambda: click_boton(0), font=font, bg=bg, fg=color, cursor=cursor)

btn_borrar =  Button(ventana, text="Borrar", width=5, height=2, command=lambda: borrar(), font=font, bg=bg, fg=color, cursor=cursor)
btn_para1 =  Button(ventana, text="(", width=5, height=2, command=lambda: click_boton("("), font=font, bg=bg, fg=color, cursor=cursor)
btn_para2 =  Button(ventana, text=")", width=5, height=2, command=lambda: click_boton(")"), font=font, bg=bg, fg=color, cursor=cursor)
btn_punto =  Button(ventana, text=".", width=5, height=2, command=lambda: click_boton("."), font=font, bg=bg, fg=color, cursor=cursor)

btn_div =  Button(ventana, text="/", width=5, height=2, command=lambda: click_boton("/"), font=font, bg=bg, fg=color, cursor=cursor)
btn_por =  Button(ventana, text="*", width=5, height=2, command=lambda: click_boton("*"), font=font, bg=bg, fg=color, cursor=cursor)
btn_sum =  Button(ventana, text="+", width=5, height=2, command=lambda: click_boton("+"), font=font, bg=bg, fg=color, cursor=cursor)
btn_res =  Button(ventana, text="-", width=5, height=2, command=lambda: click_boton("-"), font=font, bg=bg, fg=color, cursor=cursor)

btn_fin =  Button(ventana, text="=", width=5, height=2, command=lambda:resultado(), font=font, bg=bg, fg=color, cursor=cursor)

#btn en pantalla
btn_borrar.grid(row=1, column=0, padx=5, pady=5)
btn_para1.grid(row=1, column=1, padx=5, pady=5)
btn_para2.grid(row=1, column=2, padx=5, pady=5)
btn_div.grid(row=1, column=3, padx=5, pady=5)


btn7.grid(row=2, column=0, padx=5, pady=5)
btn8.grid(row=2, column=1, padx=5, pady=5)
btn9.grid(row=2, column=2, padx=5, pady=5)
btn_por.grid(row=2, column=3, padx=5, pady=5)

btn4.grid(row=3, column=0, padx=5, pady=5)
btn5.grid(row=3, column=1, padx=5, pady=5)
btn6.grid(row=3, column=2, padx=5, pady=5)
btn_sum.grid(row=3, column=3, padx=5, pady=5)

btn1.grid(row=4, column=0, padx=5, pady=5)
btn2.grid(row=4, column=1, padx=5, pady=5)
btn3.grid(row=4, column=2, padx=5, pady=5)
btn_res.grid(row=4, column=3, padx=5, pady=5)

btn0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
btn_punto.grid(row=5, column=2, padx=5, pady=5)
btn_fin.grid(row=5, column=3, padx=5, pady=5)


ventana.resizable(False, False)
ventana.config(bg="#D3D3D3")
ventana.mainloop()