class Banco():
    def __init__(self, nombre, direccion, tasa_interes, nro_clientes, banca_por_internet):
        self.nombre = nombre
        self.direccion = direccion
        self.tasa_interes = tasa_interes
        self.nro_clientes = nro_clientes
        self.banca_por_internet = banca_por_internet

    def invertir(self):
        pass
    def getDireccion(self):
        return self.direccion
    def setTasa_interes(self, tasa_interes):
        self.tasa_interes = tasa_interes