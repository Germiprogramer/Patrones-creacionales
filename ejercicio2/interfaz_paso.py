import tkinter as tk


def interfaz2():
    root = tk.Tk()
    root.title("Selección de Interfaz")

    # Botones para elegir la interfaz
    button1 = tk.Button(root, text="Interfaz 1", command=show_interface1)
    button1.pack(pady=20)
    button2 = tk.Button(root, text="Interfaz 2", command=show_interface2)
    button2.pack(pady=20)

    # Iniciar el bucle principal
    root.mainloop()