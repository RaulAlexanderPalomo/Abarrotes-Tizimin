import tkinter as tk
from tkinter import messagebox

class VistaCliente:
    def __init__(self, root, controlador_cliente):
        self.controlador_cliente = controlador_cliente
        self.root = root
        self.root.title("Registrar Cliente")
        self.root.configure(bg='lightgray')

        self.frame = tk.Frame(self.root, bg='lightgray')
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.id_label = tk.Label(self.frame, text="ID Cliente:", bg='lightgray')
        self.id_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.id_entry = tk.Entry(self.frame)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.nombre_label = tk.Label(self.frame, text="Nombre:", bg='lightgray')
        self.nombre_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.nombre_entry = tk.Entry(self.frame)
        self.nombre_entry.grid(row=1, column=1, padx=5, pady=5)

        self.apellido_label = tk.Label(self.frame, text="Apellido Paterno:", bg='lightgray')
        self.apellido_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.apellido_entry = tk.Entry(self.frame)
        self.apellido_entry.grid(row=2, column=1, padx=5, pady=5)

        self.direccion_label = tk.Label(self.frame, text="Dirección:", bg='lightgray')
        self.direccion_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.direccion_entry = tk.Entry(self.frame)
        self.direccion_entry.grid(row=3, column=1, padx=5, pady=5)

        button_bg = 'MistyRose4'
        button_fg = 'white'

        self.registrar_button = tk.Button(self.frame, text="Registrar", command=self.registrar_cliente,
                                          bg=button_bg, fg=button_fg)
        self.registrar_button.grid(row=4, columnspan=2, pady=10)

    def registrar_cliente(self):
        id_cliente = self.id_entry.get()
        nombre = self.nombre_entry.get()
        apellido_paterno = self.apellido_entry.get()
        direccion = self.direccion_entry.get()
        self.controlador_cliente.registrar_cliente(id_cliente, nombre, apellido_paterno, direccion)
        messagebox.showinfo("Registro", "Cliente registrado exitosamente")
        self.root.destroy()
