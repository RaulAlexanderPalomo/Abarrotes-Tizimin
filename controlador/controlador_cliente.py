# controlador/controlador_cliente.py
from singleton import DataStore
from factory import Factory
from iterator import ClienteIterator

class ControladorCliente:
    def __init__(self):
        self.data_store = DataStore()

    def registrar_cliente(self, id_cliente, nombre, apellido_paterno, direccion):
        cliente = Factory.crear_cliente(id_cliente, nombre, apellido_paterno, direccion)
        self.data_store.clientes.append(cliente)
        self.data_store.guardar_datos()
        return cliente

    def obtener_clientes(self):
        return ClienteIterator(self.data_store.clientes)