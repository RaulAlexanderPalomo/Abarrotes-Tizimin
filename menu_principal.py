# menu_principal.py
import tkinter as tk
from controlador.controlador_cliente import ControladorCliente
from controlador.controlador_articulo import ControladorArticulo
from controlador.controlador_compra import ControladorCompra
from vista.vista_cliente import VistaCliente
from vista.vista_articulo import VistaArticulo
from vista.vista_compra import VistaCompra

class MenuPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Abarrotes Tiziyork")
        self.root.configure(bg='lightgray')
        self.controlador_cliente = ControladorCliente()
        self.controlador_articulo = ControladorArticulo()
        self.controlador_compra = ControladorCompra()

        self.frame = tk.Frame(self.root, bg='lightgray')
        self.frame.pack(fill=tk.BOTH, expand=True)

        button_bg = 'MistyRose4'  # Color de fondo de los botones (verde)
        button_fg = 'white'    # Color del texto de los botones (blanco)

        self.registrar_cliente_button = tk.Button(self.frame, text="Registrar Cliente",
                                                  command=self.registrar_cliente,
                                                  bg=button_bg, fg=button_fg)
        self.registrar_cliente_button.place(relx=0.5, rely=0.2, anchor=tk.CENTER, relwidth=0.3, relheight=0.1)

        self.registrar_articulo_button = tk.Button(self.frame, text="Registrar Artículo",
                                                   command=self.registrar_articulo,
                                                   bg=button_bg, fg=button_fg)
        self.registrar_articulo_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER, relwidth=0.3, relheight=0.1)

        self.realizar_compra_button = tk.Button(self.frame, text="Realizar Compra",
                                                command=self.realizar_compra,
                                                bg=button_bg, fg=button_fg)
        self.realizar_compra_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER, relwidth=0.3, relheight=0.1)

        self.salir_button = tk.Button(self.frame, text="Salir",
                                      command=self.root.quit,
                                      bg=button_bg, fg=button_fg)
        self.salir_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER, relwidth=0.3, relheight=0.1)

    def registrar_cliente(self):
        new_window = tk.Toplevel(self.root)
        VistaCliente(new_window, self.controlador_cliente)

    def registrar_articulo(self):
        new_window = tk.Toplevel(self.root)
        VistaArticulo(new_window, self.controlador_articulo)

    def realizar_compra(self):
        new_window = tk.Toplevel(self.root)
        VistaCompra(new_window, self.controlador_compra, self.controlador_cliente, self.controlador_articulo)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")  # Tamaño inicial de la ventana
    app = MenuPrincipal(root)
    root.mainloop()
