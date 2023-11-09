import tkinter as tk
import csv
from builder.Director import *
from Cliente import Cliente  # Asegúrate de importar la clase Cliente desde el archivo correspondiente

# Clase para la interfaz del menú
class Menu:
    def __init__(self, root):
        

        self.label_usuario = tk.Label(root, text="Usuario:")
        self.label_usuario.pack()
        self.entry_usuario = tk.Entry(root)
        self.entry_usuario.pack()

        self.label_pedido = tk.Label(root, text="Realiza tu pedido (Barbacoa, Hawaiana, Cuatro Quesos, Margherita)")
        self.label_pedido.pack()
        self.entry_pedido = tk.Entry(root)
        self.entry_pedido.pack()

        self.pedido_button = tk.Button(root, text="Realizar Pedido", command=self.realizar_pedido)
        self.pedido_button.pack()

        self.resultado_label = tk.Label(root, text="")
        self.resultado_label.pack()

        self.ingredientes = []  # Lista para almacenar los ingredientes ingresados por el usuario


        # Cargar datos de clientes desde el archivo CSV
        self.clientes = self.cargar_clientes("ejercicio2/datos/clientes.csv")

        # Configurar el director y el constructor adecuado
        self.director = Director()
        self.builder = None
        print("Menu creado")

    # Función para iniciar la interfaz
    def iniciar_interfaz(self):
        root = tk.Tk()
        self.__init__(root)
        root.mainloop()

    # Función para cargar los datos de los clientes desde el archivo CSV
    def cargar_clientes(self, archivo):
        clientes = []
        with open(archivo, "r") as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                cliente = Cliente(row['usuario'],  row['contrasenia'], row['nombre'], row['direccion'], row['telefono'],
                                  row['email'],)
                clientes.append(cliente)
        return clientes
    
    # Función para realizar el pedido
    def realizar_pedido(self):
        print("Realizando pedido")
        usuario = self.entry_usuario.get()
        tipo_pedido = self.entry_pedido.get()

        # Seleccionar el constructor de pizza adecuado según el tipo de pedido
        if tipo_pedido.lower() == "barbacoa":
            self.builder = ConstructorPizzaBarbacoa()
            pizza = self.builder.nombre()
        elif tipo_pedido.lower() == "hawaiana":
            self.builder = ConstructorPizzaHawaiana()
            pizza = self.builder.nombre()
        elif tipo_pedido.lower() == "cuatro quesos":
            self.builder = ConstructorPizzaCuatroQuesos()
            pizza = self.builder.nombre()
        elif tipo_pedido.lower() == "margherita":
            self.builder = ConstructorPizzaMargherita()
            pizza = self.builder.nombre()
        

            # Solicitar y agregar masa, salsa base, maridaje y cocción a la pizza personalizada

        

        if self.builder:
            print("Builder creado")
            self.director.builder = self.builder
            self.director.build()

            # Guardar el pedido en un archivo CSV con columnas separadas para cada atributo
            with open("ejercicio2/datos/pedidos.csv", "a", newline="") as file:
                writer = csv.writer(file, delimiter=',')
                
                writer.writerow([usuario, tipo_pedido, pizza.masa, pizza.salsa_base, pizza.ingredientes, pizza.maridaje, pizza.coccion])
                
            self.resultado_label.config(text=f"Pedido de {usuario}: {tipo_pedido} realizado con éxito!")
        else:
            self.resultado_label.config(text=f"Tipo de pizza no válido.")




