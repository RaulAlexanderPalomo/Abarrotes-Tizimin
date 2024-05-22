from modelo.interfaces import ICliente

class Cliente(ICliente):
    def __init__(self, id_cliente, nombre, apellido_paterno, direccion):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.direccion = direccion

    def to_dict(self):
        return {
            "id_cliente": self.id_cliente,
            "nombre": self.nombre,
            "apellido_paterno": self.apellido_paterno,
            "direccion": self.direccion
        }