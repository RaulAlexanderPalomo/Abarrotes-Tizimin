import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class VistaCompra:
    def __init__(self, root, controlador_compra, controlador_cliente, controlador_articulo):
        self.controlador_compra = controlador_compra
        self.controlador_cliente = controlador_cliente
        self.controlador_articulo = controlador_articulo
        self.root = root
        self.root.title("Realizar Compra")
        self.root.configure(bg='lightgray')

        self.frame = tk.Frame(self.root, bg='lightgray')
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.cliente_label = tk.Label(self.frame, text="ID Cliente:", bg='lightgray')
        self.cliente_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.cliente_entry = tk.Entry(self.frame)
        self.cliente_entry.grid(row=0, column=1, padx=5, pady=5)

        self.articulo_label = tk.Label(self.frame, text="ID Artículo:", bg='lightgray')
        self.articulo_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.articulo_entry = tk.Entry(self.frame)
        self.articulo_entry.grid(row=1, column=1, padx=5, pady=5)

        self.cantidad_label = tk.Label(self.frame, text="Cantidad:", bg='lightgray')
        self.cantidad_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.cantidad_entry = tk.Entry(self.frame)
        self.cantidad_entry.grid(row=2, column=1, padx=5, pady=5)

        button_bg = 'MistyRose4'
        button_fg = 'white'

        self.comprar_button = tk.Button(self.frame, text="Comprar", command=self.realizar_compra,
                                        bg=button_bg, fg=button_fg)
        self.comprar_button.grid(row=3, columnspan=2, pady=10)

    def realizar_compra(self):
        id_cliente = self.cliente_entry.get()
        id_articulo = self.articulo_entry.get()
        cantidad = int(self.cantidad_entry.get())

        cliente = next((c for c in self.controlador_cliente.obtener_clientes() if c.id_cliente == id_cliente), None)
        articulo = next((a for a in self.controlador_articulo.obtener_articulos() if a.id_articulo == id_articulo), None)

        if cliente and articulo:
            compra = self.controlador_compra.realizar_compra(cliente, articulo, cantidad)
            if compra:
                ticket = f"""
                Compra realizada exitosamente
                Cliente: {cliente.nombre} {cliente.apellido_paterno}
                Dirección: {cliente.direccion}
                Artículo: {articulo.nombre}
                Cantidad: {cantidad}
                Total: {compra.total}
                Fecha: {compra.fecha.strftime('%Y-%m-%d %H:%M:%S')}
                """
                messagebox.showinfo("Compra", ticket)
            else:
                messagebox.showwarning("Error", "Cantidad insuficiente en stock")
        else:
            messagebox.showwarning("Error", "Cliente o Artículo no encontrado")

        self.root.destroy()
