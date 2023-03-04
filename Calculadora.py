from tkinter import*
from math import*
from bokeh.plotting import figure, show
from bokeh.io import output_notebook, push_notebook
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import seaborn as sns
import pandas as pd

ventana=Tk()
ventana.geometry("1250x550")
ventana.title("Calculadora")

GMatplot=Tk()
GMatplot.title("Gráfico Matplotlib")


al=3
an=11

# Bokeh

def GBokeh():
    # Recoger los valores del input del usuario
    x_input = x_entry.get()
    y_input = y_entry.get()

    # Procesar los datos
    x = [int(i) for i in x_input.split(',')]
    y = [int(i) for i in y_input.split(',')]

    # Crear la figura de Bokeh
    source = ColumnDataSource(data=dict(x=x, y=y))
    fig = figure(title='Gráfico libreria Bokeh', x_axis_label='X', y_axis_label='Y')
    fig.line('x', 'y', source=source)

    # Mostrar la figura en una ventana de Bokeh
    show(fig)

#Calculadora

def bclick(num):
    global operador
    operador=operador+str(num)
    a.set(operador)
    
def clear():
    global operador
    operador=" "
    a.set(operador)
    
def operacion():
    global operador
    try:
        opera=eval(operador)
    except:
        clear()
        opera=("ERROR")
    a.set(opera)
    
# Matplotlib
    
def graficar(valores):
    x = [1, 2, 3, 4]
    y = valores
    fig = Figure(figsize=(5, 4), dpi=100)
    fig.add_subplot(111).fill_between(x, y)
    canvas = FigureCanvasTkAgg(fig, master=GMatplot)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Función para obtener los valores ingresados por el usuario y llamar a la función de graficar
def obtener_valores():
    valores = []
    valores.append(float(entry1.get()))
    valores.append(float(entry2.get()))
    valores.append(float(entry3.get()))
    valores.append(float(entry4.get()))
    graficar(valores)
    
#seaborn
# Función que se ejecuta al hacer clic en el botón "Mostrar gráfico"
def mostrar_grafico():
    # Obteniendo los valores ingresados por el usuario
    Miembros_hogar = float(total_bill_entry.get())
    Trabajando = float(tip_entry.get())

    # Creando un DataFrame con los datos ingresados
    data = {'Miembros_hogar': [Miembros_hogar], 'Trabajando': [Trabajando]}
    tips = pd.DataFrame(data)

    # Creando el gráfico de dispersión
    sns.scatterplot(x="Miembros_hogar", y="Trabajando", data=tips)

    # Mostrando el gráfico
    plt.show()

    
    
a=StringVar()
operador=""

btnRaiz=Button(ventana,text="√",width=an, height=al, command=lambda:bclick("sqrt("))
btnRaiz.place(x=1, y=85)
btnExpo=Button(ventana,text="EXP",width=an, height=al, command=lambda:bclick("**"))
btnExpo.place(x=90, y=85)
btnLog=Button(ventana,text="log",width=an, height=al, command=lambda:bclick("log10("))
btnLog.place(x=179, y=85)
btnLn=Button(ventana,text="ln",width=an, height=al, command=lambda:bclick("log"))
btnLn.place(x=268, y=85)
btnSin=Button(ventana,text="sin",width=an, height=al, command=lambda:bclick("sin("))
btnSin.place(x=357, y=85)

btnCos=Button(ventana,text="cos",width=an, height=al, command=lambda:bclick("cos("))
btnCos.place(x=1, y=143)
btnTan=Button(ventana,text="tan",width=an, height=al, command=lambda:bclick("tan("))
btnTan.place(x=90, y=143)
btnArcSin=Button(ventana,text="arcsin",width=an, height=al, command=lambda:bclick("asin("))
btnArcSin.place(x=179, y=143)
btnArcCos=Button(ventana,text="arccos",width=an, height=al, command=lambda:bclick("acos"))
btnArcCos.place(x=268, y=143)
btnArcTan=Button(ventana,text="arctan",width=an, height=al, command=lambda:bclick("atan("))
btnArcTan.place(x=357, y=143)

btnSec=Button(ventana,text="sec",width=an, height=al, command=lambda:bclick("1/cos("))
btnSec.place(x=1, y=201)
btnCsc=Button(ventana,text="csc",width=an, height=al, command=lambda:bclick("1/sin("))
btnCsc.place(x=90, y=201)
btnCot=Button(ventana,text="cot",width=an, height=al, command=lambda:bclick("1/tan("))
btnCot.place(x=179, y=201)
btnParenA=Button(ventana,text="(",width=an, height=al, command=lambda:bclick("("))
btnParenA.place(x=268, y=201)
btnParenC=Button(ventana,text=")",width=an, height=al, command=lambda:bclick(")"))
btnParenC.place(x=357, y=201)

btn7=Button(ventana,text="7",width=an, height=al, command=lambda:bclick("7"))
btn7.place(x=1, y=259)
btn8=Button(ventana,text="8",width=an, height=al, command=lambda:bclick("8"))
btn8.place(x=90, y=259)
btn9=Button(ventana,text="9",width=an, height=al, command=lambda:bclick("9"))
btn9.place(x=179, y=259)
btnAC=Button(ventana,text="AC",width=an, height=al, command=clear)
btnAC.place(x=268, y=259)
btnDEL=Button(ventana,text="DEL",width=an, height=al, command=lambda:bclick("remove"))
btnDEL.place(x=357, y=259)

btn4=Button(ventana,text="4",width=an, height=al, command=lambda:bclick("4"))
btn4.place(x=1, y=317)
btn5=Button(ventana,text="5",width=an, height=al, command=lambda:bclick("5"))
btn5.place(x=90, y=317)
btn6=Button(ventana,text="6",width=an, height=al, command=lambda:bclick("6"))
btn6.place(x=179, y=317)
btnMultip=Button(ventana,text="x",width=an, height=al, command=lambda:bclick("*"))
btnMultip.place(x=268, y=317)
btnDivid=Button(ventana,text="/",width=an, height=al, command=lambda:bclick("/"))
btnDivid.place(x=357, y=317)

btn1=Button(ventana,text="1",width=an, height=al, command=lambda:bclick("1"))
btn1.place(x=1, y=375)
btn2=Button(ventana,text="2",width=an, height=al, command=lambda:bclick("2"))
btn2.place(x=90, y=375)
btn3=Button(ventana,text="3",width=an, height=al, command=lambda:bclick("3"))
btn3.place(x=179, y=375)
btnSuma=Button(ventana,text="+",width=an, height=al, command=lambda:bclick("+"))
btnSuma.place(x=268, y=375)
btnResta=Button(ventana,text="-",width=an, height=al, command=lambda:bclick("-"))
btnResta.place(x=357, y=375)

btn0=Button(ventana,text="0",width=an, height=al, command=lambda:bclick("0"))
btn0.place(x=1, y=433)
btnComa=Button(ventana,text=",",width=an, height=al, command=lambda:bclick(","))
btnComa.place(x=90, y=433)
btnPi=Button(ventana,text="π",width=an, height=al, command=lambda:bclick("pi"))
btnPi.place(x=179, y=433)
btnPorcen=Button(ventana,text="%",width=an, height=al, command=lambda:bclick("%"))
btnPorcen.place(x=268, y=433)
btnResultado=Button(ventana,text="=",width=an, height=al, command=operacion)
btnResultado.place(x=357, y=433)
btnSalir=Button(ventana,text="Salir",width=an, height=al, command=quit)
btnSalir.place(x=357, y=490)
consola=Entry(ventana, font=("Arial",20,"bold"),textvariable=a,width=22,bd=20,insertwidth=5,justify="right")
consola.pack()
consola.place (x=30, y=5)

labelTBokeh = Label(ventana, text="Libreria Bokeh")
labelTBokeh.place (x=595,y=55)
x_label = Label(ventana, text='Valores de X:')
x_label.place (x=535, y=85)
x_entry = Entry(ventana)
x_entry.place (x=624, y=85 )
y_label = Label(ventana, text='Valores de Y:')
y_label.place (x=535, y=115)
y_entry = Entry(ventana)
y_entry.place (x=624,y=115)
plot_button = Button(ventana, text='Graficar', command=GBokeh)
plot_button.place (x=635,y=145)

#inicio interfaz Matplotlib

# Crear widgets de entrada de texto y etiquetas
labelTML = Label(ventana, text= "Libreria Matlotlib")
labelTML.place (x=920,y=30)
label1 = Label(ventana, text="Valor 1:")
label1.place (x=950, y=50)
entry1 = Entry(ventana)
entry1.place (x=910, y=75)
label2 = Label(ventana, text="Valor 2:")
label2.place (x=950, y=100)
entry2 = Entry(ventana)
entry2.place (x=910, y=125)
label3 = Label(ventana, text="Valor 3:")
label3.place (x=950,y=150)
entry3 = Entry(ventana)
entry3.place (x=910,y=175)
label4 = Label(ventana, text="Valor 4:")
label4.place (x=950,y=200)
entry4 = Entry(ventana)
entry4.place (x=910,y=225)

# Crear botón de graficar y llamar a la función de obtener_valores
boton_graficar = Button(ventana, text="Graficar", command=obtener_valores)
boton_graficar.place (x=950,y=250)

#Fin Matplotlib

#seabron

labelTSeabron = Label(ventana,text= "Libreria Seabron")
labelTSeabron.place (x=625,y=245)
total_bill_label = Label(ventana, text="Miembros de hogar:")
total_bill_label.place (x=535,y=275)
total_bill_entry = Entry(ventana)
total_bill_entry.place (x=660,y=275)

tip_label = Label(ventana, text="Trabajan actualmente:")
tip_label.place (x=535,y=300)
tip_entry = Entry(ventana)
tip_entry.place (x=660,y=300)

# Creando el botón para mostrar el gráfico
mostrar_grafico_button = Button(ventana, text="Mostrar gráfico", command=mostrar_grafico)
mostrar_grafico_button.place (x=590,y=350)


ventana.mainloop()