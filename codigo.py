import tkinter as tk
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Función que se ejecuta al hacer clic en el botón "Mostrar gráfico"
def mostrar_grafico():
    # Obteniendo los valores ingresados por el usuario
    total_bill = float(total_bill_entry.get())
    tip = float(tip_entry.get())

    # Creando un DataFrame con los datos ingresados
    data = {'total_bill': [total_bill], 'tip': [tip]}
    tips = pd.DataFrame(data)

    # Creando el gráfico de dispersión
    sns.scatterplot(x="total_bill", y="tip", data=tips)

    # Mostrando el gráfico
    plt.show()

# Creando la ventana principal
root = tk.Tk()
root.title("Gráfico de dispersión")

# Creando los widgets para la entrada de datos
total_bill_label = tk.Label(root, text="Total de la factura:")
total_bill_entry = tk.Entry(root)

tip_label = tk.Label(root, text="Monto de la propina:")
tip_entry = tk.Entry(root)

# Creando el botón para mostrar el gráfico
mostrar_grafico_button = tk.Button(root, text="Mostrar gráfico", command=mostrar_grafico)

# Ubicando los widgets en la ventana
total_bill_label.grid(row=0, column=0)
total_bill_entry.grid(row=0, column=1)

tip_label.grid(row=1, column=0)
tip_entry.grid(row=1, column=1)

mostrar_grafico_button.grid(row=2, columnspan=2)

# Ejecutando la ventana principal
root.mainloop()







