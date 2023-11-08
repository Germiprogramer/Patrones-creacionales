import tkinter as tk
import csv
from builder.Director import *
from Cliente import Cliente  # Asegúrate de importar la clase Cliente desde el archivo correspondiente

class PizzeriaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizzería")

        self.label_usuario = tk.Label(root, text="Usuario:")
        self.label_usuario.pack()
        self.entry_usuario = tk.Entry(root)
        self.entry_usuario.pack()

        self.label_pedido = tk.Label(root, text="Realiza tu pedido (Barbacoa, Hawaiana, Cuatro Quesos, Margherita, Personalizada):")
        self.label_pedido.pack()
        self.entry_pedido = tk.Entry(root)
        self.entry_pedido.pack()

        self.pedido_button = tk.Button(root, text="Realizar Pedido", command=self.realizar_pedido)
        self.pedido_button.pack()

        self.resultado_label = tk.Label(root, text="")
        self.resultado_label.pack()

        self.ingredientes = []  # Lista para almacenar los ingredientes ingresados por el usuario

        self.ingredientes_label = tk.Label(root, text="Ingredientes (escribe 'fin' para terminar):")
        self.ingredientes_label.pack()
        self.entry_ingredientes = tk.Entry(root)
        self.entry_ingredientes.pack()

        self.masas_label = tk.Label(root, text="Tipo de masa:")
        self.masas_label.pack()
        self.entry_masa = tk.Entry(root)
        self.entry_masa.pack()

        self.salsa_label = tk.Label(root, text="Tipo de salsa base:")
        self.salsa_label.pack()
        self.entry_salsa = tk.Entry(root)
        self.entry_salsa.pack()

        self.maridaje_label = tk.Label(root, text="Tipo de maridaje:")
        self.maridaje_label.pack()
        self.entry_maridaje = tk.Entry(root)
        self.entry_maridaje.pack()

        self.coccion_label = tk.Label(root, text="Tipo de cocción:")
        self.coccion_label.pack()
        self.entry_coccion = tk.Entry(root)
        self.entry_coccion.pack()

        # Cargar datos de clientes desde el archivo CSV
        self.clientes = self.cargar_clientes("ejercicio2/datos/clientes.csv")

        # Configurar el director y el constructor adecuado
        self.director = Director()
        self.builder = None

    def cargar_clientes(self, archivo):
        clientes = []
        with open(archivo, "r") as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                cliente = Cliente(row['usuario'], row['nombre'], row['apellido'], row['direccion'], row['telefono'],
                                  row['email'], row['contrasenia'], row['n_pedidos'], row['dinero'])
                clientes.append(cliente)
        return clientes

    def realizar_pedido(self):
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
        elif tipo_pedido.lower() == "personalizada":
            self.builder = ConstructorPizzaPersonalizada()
            pizza = self.builder.nombre()

            # Solicitar y agregar masa, salsa base, maridaje y cocción a la pizza personalizada
            masa = self.entry_masa.get()
            salsa_base = self.entry_salsa.get()
            maridaje = self.entry_maridaje.get()
            coccion = self.entry_coccion.get()

            self.builder.product.masa(masa)
            self.builder.product.salsa_base(salsa_base)
            self.builder.product.maridaje(maridaje)
            self.builder.product.coccion(coccion)

            # Agregar ingredientes a la pizza personalizada
            for ingrediente in self.ingredientes:
                self.builder.product.ingredientes(ingrediente)

            # Construir un objeto Pizza con los atributos de la pizza personalizada
            pizza = self.builder.nombre()

        

        if self.builder:
            self.director.builder = self.builder
            self.director.build()

            # Guardar el pedido en un archivo CSV con columnas separadas para cada atributo
            with open("ejercicio2/datos/pedidos.csv", "a", newline="") as file:
                writer = csv.writer(file, delimiter=';')
                if tipo_pedido.lower() != "personalizada":
                    writer.writerow([usuario, tipo_pedido, pizza.masa, pizza.salsa_base, ', '.join(pizza.ingredientes), pizza.maridaje, pizza.coccion])
                else:
                    writer.writerow([usuario, tipo_pedido, ', '.join(pizza.masa), ', '.join(pizza.salsa_base), ', '.join(pizza.ingredientes), pizza.maridaje, pizza.coccion])
            self.resultado_label.config(text=f"Pedido de {usuario}: {tipo_pedido} realizado con éxito!")
        else:
            self.resultado_label.config(text=f"Tipo de pizza no válido.")

    def agregar_ingrediente(self):
        ingrediente = self.entry_ingredientes.get()
        if ingrediente.lower() == 'fin':
            # Cuando el usuario escribe 'fin', finaliza la entrada de ingredientes y realiza el pedido
            self.realizar_pedido()
        else:
            self.ingredientes.append(ingrediente)
            self.entry_ingredientes.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = PizzeriaApp(root)
    root.mainloop()
