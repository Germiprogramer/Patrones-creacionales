import tkinter as tk
import csv
from tkinter import messagebox


def interfaz2():

    options_window = tk.Tk()
    options_window.title("Opciones")
    
    tk.Label(options_window, text="Elige una opción:").pack(pady=10)
    
    def menu_option():
        messagebox.showinfo("Opción Seleccionada", "Has seleccionado: Menú")
        options_window.destroy()  # Cerrar la ventana de opciones


        
    def custom_option():
        messagebox.showinfo("Opción Seleccionada", "Has seleccionado: Personalizada")
        options_window.destroy()  # Cerrar la ventana de opciones
    
    menu_button = tk.Button(options_window, text="Menú", command=menu_option)
    menu_button.pack(pady=10)
    
    custom_button = tk.Button(options_window, text="Personalizada", command=custom_option)
    custom_button.pack(pady=10)

    options_window.mainloop()