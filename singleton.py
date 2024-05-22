# singleton.py
import json
from datetime import datetime
from factory import Factory

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

        try:
            with open('compras.json', 'r') as f:
                compras_dict = json.load(f)
                self.compras = [Factory.crear_compra(self.clientes, self.articulos, **compra) for compra in compras_dict]
        except FileNotFoundError:
            self.compras = []

    def guardar_datos(self):
        with open('clientes.json', 'w') as f:
            json.dump([cliente.to_dict() for cliente in self.clientes], f, indent=4)
        with open('articulos.json', 'w') as f:
            json.dump([articulo.to_dict() for articulo in self.articulos], f, indent=4)
        with open('compras.json', 'w') as f:
            json.dump([compra.to_dict() for compra in self.compras], f, indent=4)
