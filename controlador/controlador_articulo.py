from singleton import DataStore
from factory import Factory
from iterator import ArticuloIterator

class ControladorArticulo:
    def __init__(self):
        self.data_store = DataStore()

    def registrar_articulo(self, id_articulo, nombre, precio_publico, precio_proveedor, cantidad):
        articulo = Factory.crear_articulo(id_articulo, nombre, precio_publico, precio_proveedor, cantidad)
        self.data_store.articulos.append(articulo)
        self.data_store.guardar_datos()
        return articulo

    def obtener_articulos(self):
        return ArticuloIterator(self.data_store.articulos)