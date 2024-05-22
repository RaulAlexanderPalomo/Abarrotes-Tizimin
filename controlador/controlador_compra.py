# controlador/controlador_compra.py
from singleton import DataStore
from factory import Factory
from datetime import datetime

class ControladorCompra:
    def __init__(self):
        self.data_store = DataStore()

    def realizar_compra(self, cliente, articulo, cantidad):
        if articulo.cantidad >= cantidad:
            articulo.cantidad -= cantidad
            compra = Factory.crear_compra(cliente, articulo, cantidad)
            self.data_store.compras.append(compra)
            self.data_store.guardar_datos()
            return compra
        return None

    def obtener_compras(self):
        return self.data_store.compras
