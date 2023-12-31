import tkinter as tk
import csv
from tkinter import messagebox
from interfaz_menu import *
from interfaz_personalizada import *
import pandas as pd

# Función para que el usuario pueda elegir entre una pizza del menú o una personalizada
def interfaz2():

    options_window = tk.Tk()
    options_window.title("Opciones")
    
    tk.Label(options_window, text="Elige una opción:").pack(pady=10)
    
    # Función para obtener la recomendación de pizza del usuario
    def hacer_recomendacion():
        df = pd.read_csv('ejercicio2/datos/pedidos.csv')

        nombre_usuario = entry_usuario.get()

        df_filtrado = df[df["usuario"] == nombre_usuario]

        dato_mas_repetido = df_filtrado["tipo"].mode().iloc[0]
        
        if str(dato_mas_repetido) != "personalizada":

            print(dato_mas_repetido)
            
            recomendacion = str(dato_mas_repetido)

            resultado.config(text=recomendacion)
        else:
            masa_repetida = df_filtrado["masa"].mode().iloc[0]
            salsa_repetida = df_filtrado["salsa"].mode().iloc[0]
            coccion_repetida = df_filtrado["coccion"].mode().iloc[0]
            presentacion_repetida = df_filtrado["presentacion"].mode().iloc[0]
            maridaje_repetido = df_filtrado["maridaje"].mode().iloc[0]

            resultado.config(text=(masa_repetida, salsa_repetida, coccion_repetida, presentacion_repetida, maridaje_repetido))


    # Función para mostrar la interfaz del menú
    def menu_option():
        messagebox.showinfo("Opción Seleccionada", "Has seleccionado: Menú")
        options_window.destroy()  # Cerrar la ventana de opciones
        
        root = tk.Tk()
        app = Menu(root)
        app.iniciar_interfaz()


    # Función para mostrar la interfaz de la pizza personalizada
    def custom_option():
        messagebox.showinfo("Opción Seleccionada", "Has seleccionado: Personalizada")
        options_window.destroy()  # Cerrar la ventana de opciones

        interfaz_personalizada()
    
    # Crear y colocar widgets para la recomendación de pizza
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

    # Mostrar la ventana de opciones
    options_window.mainloop()