# modelo/compra.py
from datetime import datetime
from modelo.interfaces import ICompra

class Compra(ICompra):
    def __init__(self, cliente, articulo, cantidad, fecha=None):
        self.cliente = cliente
        self.articulo = articulo
        self.cantidad = cantidad
        self.fecha = fecha if fecha else datetime.now()

    @property
    def total(self):
        return self.articulo.precio_publico * self.cantidad

    def to_dict(self):
        return {
            "cliente_id": self.cliente.id_cliente,
            "articulo_id": self.articulo.id_articulo,
            "cantidad": self.cantidad,
            "fecha": self.fecha.isoformat()
        }
