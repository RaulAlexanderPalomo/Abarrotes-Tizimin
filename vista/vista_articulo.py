import tkinter as tk
from tkinter import messagebox

class VistaArticulo:
    def __init__(self, root, controlador_articulo):
        self.controlador_articulo = controlador_articulo
        self.root = root
        self.root.title("Registrar Artículo")
        self.root.configure(bg='lightgray')

        self.frame = tk.Frame(self.root, bg='lightgray')
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.id_label = tk.Label(self.frame, text="ID Artículo:", bg='lightgray')
        self.id_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.id_entry = tk.Entry(self.frame)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.nombre_label = tk.Label(self.frame, text="Nombre:", bg='lightgray')
        self.nombre_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.nombre_entry = tk.Entry(self.frame)
        self.nombre_entry.grid(row=1, column=1, padx=5, pady=5)

        self.precio_publico_label = tk.Label(self.frame, text="Precio Público:", bg='lightgray')
        self.precio_publico_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.precio_publico_entry = tk.Entry(self.frame)
        self.precio_publico_entry.grid(row=2, column=1, padx=5, pady=5)

        self.precio_proveedor_label = tk.Label(self.frame, text="Precio Proveedor:", bg='lightgray')
        self.precio_proveedor_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.precio_proveedor_entry = tk.Entry(self.frame)
        self.precio_proveedor_entry.grid(row=3, column=1, padx=5, pady=5)

        self.cantidad_label = tk.Label(self.frame, text="Cantidad:", bg='lightgray')
        self.cantidad_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.cantidad_entry = tk.Entry(self.frame)
        self.cantidad_entry.grid(row=4, column=1, padx=5, pady=5)

        button_bg = 'MistyRose4'
        button_fg = 'white'

        self.registrar_button = tk.Button(self.frame, text="Registrar", command=self.registrar_articulo,
                                          bg=button_bg, fg=button_fg)
        self.registrar_button.grid(row=5, columnspan=2, pady=10)

    def registrar_articulo(self):
        id_articulo = self.id_entry.get()
        nombre = self.nombre_entry.get()
        precio_publico = float(self.precio_publico_entry.get())
        precio_proveedor = float(self.precio_proveedor_entry.get())
        cantidad = int(self.cantidad_entry.get())
        self.controlador_articulo.registrar_articulo(id_articulo, nombre, precio_publico, precio_proveedor, cantidad)
        messagebox.showinfo("Registro", "Artículo registrado exitosamente")
        self.root.destroy()
