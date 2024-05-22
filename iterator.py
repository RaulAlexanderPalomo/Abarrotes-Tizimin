# iterator.py
class ClienteIterator:
    def __init__(self, clientes):
        self._clientes = clientes
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._clientes):
            cliente = self._clientes[self._index]
            self._index += 1
            return cliente
        raise StopIteration

class ArticuloIterator:
    def __init__(self, articulos):
        self._articulos = articulos
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._articulos):
            articulo = self._articulos[self._index]
            self._index += 1
            return articulo
        raise StopIteration

class CompraIterator:
    def __init__(self, compras):
        self._compras = compras
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._compras):
            compra = self._compras[self._index]
            self._index += 1
            return compra
        raise StopIteration
