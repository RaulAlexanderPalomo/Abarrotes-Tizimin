import json
from datetime import datetime
from factory import Factory
import os

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class DataStore(metaclass=SingletonMeta):
    def __init__(self):
        self.clientes = []
        self.articulos = []
        self.compras = []
        self.cargar_datos()

    def cargar_datos(self):
        # Crear el directorio "archivos" si no existe
        os.makedirs("archivos", exist_ok=True)

        try:
            with open('clientes.json', 'r') as f:
                clientes_dict = json.load(f)
                self.clientes = [Factory.crear_cliente(**cliente) for cliente in clientes_dict]
        except FileNotFoundError:
            self.clientes = []

        try:
            with open('articulos.json', 'r') as f:
                articulos_dict = json.load(f)
                self.articulos = [Factory.crear_articulo(**articulo) for articulo in articulos_dict]
        except FileNotFoundError:
            self.articulos = []

        # Ignorar cualquier error al leer el archivo de compras
        try:
            with open('archivos/compras.json', 'r') as f:
                compras_dict = json.load(f)
                self.compras = [Factory.crear_compra(self.clientes, self.articulos, **compra) for compra in
                                compras_dict]
        except:
            self.compras = []

    def guardar_datos(self):
        with open('clientes.json', 'w') as f:
            json.dump([cliente.to_dict() for cliente in self.clientes], f, indent=4)
        with open('articulos.json', 'w') as f:
            json.dump([articulo.to_dict() for articulo in self.articulos], f, indent=4)

        # Leer las compras existentes del archivo
        try:
            with open('archivos/compras.json', 'r') as f:
                compras_existentes = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            compras_existentes = []

        # Agregar las nuevas compras a la lista
        compras_actualizadas = compras_existentes + [compra.to_dict() for compra in self.compras]

        # Guardar todas las compras en el archivo
        with open('archivos/compras.json', 'w') as f:
            json.dump(compras_actualizadas, f, indent=4)