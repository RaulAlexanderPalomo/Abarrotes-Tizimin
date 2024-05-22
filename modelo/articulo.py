# modelo/articulo.py
from modelo.interfaces import IArticulo

class Articulo(IArticulo):
    def __init__(self, id_articulo, nombre, precio_publico, precio_proveedor, cantidad):
        self.id_articulo = id_articulo
        self.nombre = nombre
        self.precio_publico = precio_publico
        self.precio_proveedor = precio_proveedor
        self.cantidad = cantidad

    def to_dict(self):
        return {
            "id_articulo": self.id_articulo,
            "nombre": self.nombre,
            "precio_publico": self.precio_publico,
            "precio_proveedor": self.precio_proveedor,
            "cantidad": self.cantidad
        }