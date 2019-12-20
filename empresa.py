class Empresa():
    def __init__(self, propietario, direccion, telefono, ruc, atencion_cliente):
        self.propietario = propietario
        self.direccion = direccion
        self.telefono = telefono
        self.ruc = ruc
        self.atencion_cliente = atencion_cliente

    def lucrar(self):
        pass
    def getDireccion(self):
        return self.direccion
    def setAtencion_cliente(self, atencion_cliente):
        self.atencion_cliente = atencion_cliente