import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")

indice = 0
#INPUT

input_text = tk.Entry(ventana, font=("Calibri 20"));  #entrada de texto
input_text.grid(row = 0,column = 0,columnspan = 4, padx = 10, pady = 5)  #dandole formato a la cuadricula de la entrada
#el padx y pady es como el margin en css

#FUNCIONES
def click_button(value_b):
    global indice
    input_text.insert(indice,value_b)
    indice+=1

def delete_text():
    global indice
    input_text.delete(0,tk.END)
    indice=0
def make_operation():
    global indice
    ecuation = input_text.get()
    result = eval(ecuation)
    input_text.delete(0,tk.END)
    input_text.insert(0,result)
    indice=0
    


#BOTONES

button1 = tk.Button(ventana,text = "1", width = 5,height = 2, command = lambda: click_button(1))
button2 = tk.Button(ventana,text = "2", width = 5,height = 2, command = lambda: click_button(2))
button3 = tk.Button(ventana,text = "3", width = 5,height = 2, command = lambda: click_button(3))
button4 = tk.Button(ventana,text = "4", width = 5,height = 2, command = lambda: click_button(4))
button5 = tk.Button(ventana,text = "5", width = 5,height = 2, command = lambda: click_button(5))
button6 = tk.Button(ventana,text = "6", width = 5,height = 2, command = lambda: click_button(6))
button7 = tk.Button(ventana,text = "7", width = 5,height = 2, command = lambda: click_button(7))
button8 = tk.Button(ventana,text = "8", width = 5,height = 2, command = lambda: click_button(8))
button9 = tk.Button(ventana,text = "9", width = 5,height = 2, command = lambda: click_button(9))
button0 = tk.Button(ventana,text = "0", width = 14,height = 2, command = lambda: click_button(0))


button_delete = tk.Button(ventana,text = "AC", width = 5,height = 2, command = lambda: delete_text())
button_parentheses_opening = tk.Button(ventana,text = "(", width = 5,height = 2, command = lambda: click_button("("))
button_parentheses_closing = tk.Button(ventana,text = ")", width = 5,height = 2, command = lambda: click_button(")"))
button_dot = tk.Button(ventana,text = ".", width = 5,height = 2, command = lambda: click_button("."))

button_plus = tk.Button(ventana,text = "+", width = 5,height = 2, command = lambda: click_button("+"))
button_minus = tk.Button(ventana,text = "-", width = 5,height = 2, command = lambda: click_button("-"))
button_times = tk.Button(ventana,text = "x", width = 5,height = 2, command = lambda: click_button("*"))
button_divided = tk.Button(ventana,text = "/", width = 5,height = 2, command = lambda: click_button("/"))
button_equals = tk.Button(ventana,text = "=", width = 5,height = 2, command = lambda: make_operation())

#INTERFAZ

button_delete.grid(row = 1, column = 0, padx = 5, pady = 5)
button_parentheses_opening.grid(row = 1, column = 1, padx = 5, pady = 5)
button_parentheses_closing.grid(row = 1, column = 2, padx = 5, pady = 5)
button_divided.grid(row = 1, column = 3, padx = 5, pady = 5)

button7.grid(row = 2, column = 0, padx = 5, pady = 5)
button8.grid(row = 2, column = 1, padx = 5, pady = 5)
button9.grid(row = 2, column = 2, padx = 5, pady = 5)
button_times.grid(row = 2, column = 3, padx = 5, pady = 5)

button4.grid(row = 3, column = 0, padx = 5, pady = 5)
button5.grid(row = 3, column = 1, padx = 5, pady = 5)
button6.grid(row = 3, column = 2, padx = 5, pady = 5)
button_plus.grid(row = 3, column = 3, padx = 5, pady = 5)

button1.grid(row = 4, column = 0, padx = 5, pady = 5)
button2.grid(row = 4, column = 1, padx = 5, pady = 5)
button3.grid(row = 4, column = 2, padx = 5, pady = 5)
button_minus.grid(row = 4, column = 3, padx = 5, pady = 5)

button0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
button_dot.grid(row = 5, column = 2, padx = 5, pady = 5)
button_equals.grid(row = 5, column = 3, padx = 5, pady = 5)






ventana.mainloop()