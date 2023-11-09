import tkinter as tk
import csv
from tkinter import messagebox
from builder.Director import *

def interfaz_personalizada():

    # Initialize Director for pizza construction
    director = Director()
    builder = ConstructorPizzaPersonalizada()
    director.builder = builder

    # Function to handle pizza order
    def place_order():
        # Get user input for pizza attributes
        masa = masa_var.get()
        salsa_base = salsa_var.get()
        ingredientes = ingredientes_var.get()
        coccion = coccion_var.get()
        presentacion = presentacion_var.get()
        maridaje = maridaje_var.get()
        extras = extras_var.get()

        # Construct pizza using builder pattern
        director.build()
        pizza = builder.product

        # Save pizza order to pedidos.csv file
        with open('ejercicio2/datos/pedidos.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username_entr.get(), masa, salsa_base, ingredientes, coccion, presentacion, maridaje, extras])

        messagebox.showinfo("Pedido Realizado", "Pedido registrado con éxito")

    # Create main window
    root = tk.Tk()
    root.title("Pizzería")

    # Create and place registration form widgets
    tk.Label(root, text="Registro de Usuario").grid(row=0, column=0, columnspan=2, pady=10)
    tk.Label(root, text="Usuario").grid(row=1, column=0, padx=10)
    username_entr = tk.Entry(root)
    username_entr.grid(row=2, column=0, padx=10)

    # Create and place pizza order form widgets
    tk.Label(root, text="Realizar Pedido").grid()

    # Pizza attributes options
    options = ["Delgada", "Normal", "Gruesa"]
    masa_var = tk.StringVar(root)
    masa_var.set(options[0])
    tk.Label(root, text="Masa").grid()
    masa_menu = tk.OptionMenu(root, masa_var, *options)
    masa_menu.grid()

    options = ["Tomate", "Blanca"]
    salsa_var = tk.StringVar(root)
    salsa_var.set(options[0])
    tk.Label(root, text="Salsa Base").grid()
    salsa_menu = tk.OptionMenu(root, salsa_var, *options)
    salsa_menu.grid()

    ingredientes_var = tk.StringVar(root)
    ingredientes_entry = tk.Entry(root, textvariable=ingredientes_var)
    tk.Label(root, text="Ingredientes").grid()
    ingredientes_entry.grid()

    options = ["Suave", "Crujiente", "Crocante"]
    coccion_var = tk.StringVar(root)
    coccion_var.set(options[0])
    tk.Label(root, text="Cocción").grid()
    coccion_menu = tk.OptionMenu(root, coccion_var, *options)
    coccion_menu.grid()

    options = ["Normal", "Premium"]
    presentacion_var = tk.StringVar(root)
    presentacion_var.set(options[0])
    tk.Label(root, text="Presentación").grid()
    presentacion_menu = tk.OptionMenu(root, presentacion_var, *options)
    presentacion_menu.grid()

    options = ["Vino tinto", "Cerveza", "Refresco"]
    maridaje_var = tk.StringVar(root)
    maridaje_var.set(options[0])
    tk.Label(root, text="Maridaje").grid()
    maridaje_menu = tk.OptionMenu(root, maridaje_var, *options)
    maridaje_menu.grid()

    extras_var = tk.StringVar(root)
    extras_entry = tk.Entry(root, textvariable=extras_var)
    tk.Label(root, text="Extras").grid()
    extras_entry.grid()

    order_button = tk.Button(root, text="Realizar Pedido", command=place_order)
    order_button.grid()

    # Start the main loop
    root.mainloop()
