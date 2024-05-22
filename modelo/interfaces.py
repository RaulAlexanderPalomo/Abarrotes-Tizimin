# modelo/interfaces.py
from abc import ABC, abstractmethod

class ICliente(ABC):
    @abstractmethod
    def __init__(self, id_cliente, nombre, apellido_paterno, direccion):
        pass

class IArticulo(ABC):
    @abstractmethod
    def __init__(self, id_articulo, nombre, precio_publico, precio_proveedor, cantidad):
        pass

class ICompra(ABC):
    @abstractmethod
    def __init__(self, cliente, articulo, cantidad):
        pass
