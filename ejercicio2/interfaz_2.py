import tkinter as tk
import csv
from tkinter import messagebox
from interfaz_menu import *
from interfaz_personalizada import *
import pandas as pd

def interfaz2():

    options_window = tk.Tk()
    options_window.title("Opciones")
    
    tk.Label(options_window, text="Elige una opción:").pack(pady=10)
    

    def hacer_recomendacion():
        df = pd.read_csv('ejercicio2/datos/pedidos.csv')

        nombre_usuario = entry_usuario.get()

        df_filtrado = df[df["usuario"] == nombre_usuario]

        dato_mas_repetido = df_filtrado["tipo"].mode().iloc[0]

        recomendacion = str(dato_mas_repetido)

        resultado.config(text=recomendacion)

    def menu_option():
        messagebox.showinfo("Opción Seleccionada", "Has seleccionado: Menú")
        options_window.destroy()  # Cerrar la ventana de opciones
        
        root = tk.Tk()
        app = Menu(root)
        app.iniciar_interfaz()



    def custom_option():
        messagebox.showinfo("Opción Seleccionada", "Has seleccionado: Personalizada")
        options_window.destroy()  # Cerrar la ventana de opciones

        interfaz_personalizada()
    
    label_usuario = tk.Label(options_window, text="Usuario:")
    label_usuario.pack(pady=10)
    entry_usuario = tk.Entry(options_window, width=30)
    entry_usuario.pack(pady=10)

    recomendar_button = tk.Button(options_window, text="Obtener Recomendación", command=hacer_recomendacion)
    recomendar_button.pack(pady=10)

    resultado = tk.Label(options_window, text="")
    resultado.pack(pady=10)

    menu_button = tk.Button(options_window, text="Menú", command=menu_option)
    menu_button.pack(pady=10)
    
    custom_button = tk.Button(options_window, text="Personalizada", command=custom_option)
    custom_button.pack(pady=10)

    options_window.mainloop()