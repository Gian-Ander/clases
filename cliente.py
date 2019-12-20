class Cliente():
    def __init__(self, nombre, direccion, empresa, telefono, importe):
        self.nombre = nombre
        self.direccion = direccion
        self.empresa = empresa
        self.telefono = telefono
        self.importe = importe

    def adquirir(self):
        return "El señor " + self.nombre + " es cliente de la empresa " + self.empresa

    def setTelefono(self, telefono):
        self.telefono = telefono

    def getImporte(self):
        return self.importe