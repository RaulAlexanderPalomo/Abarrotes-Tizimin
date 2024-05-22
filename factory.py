# factory.py
from modelo.cliente import Cliente
from modelo.articulo import Articulo
from modelo.compra import Compra
from modelo.interfaces import ICliente, IArticulo, ICompra

class Factory:
    @staticmethod
    def crear_cliente(id_cliente, nombre, apellido_paterno, direccion) -> ICliente:
        return Cliente(id_cliente, nombre, apellido_paterno, direccion)

    @staticmethod
    def crear_articulo(id_articulo, nombre, precio_publico, precio_proveedor, cantidad) -> IArticulo:
        return Articulo(id_articulo, nombre, precio_publico, precio_proveedor, cantidad)

    @staticmethod
    def crear_compra(cliente, articulo, cantidad) -> ICompra:
        return Compra(cliente, articulo, cantidad)