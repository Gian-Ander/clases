class Mascota():
    def __init__(self, nombre, tipo, raza, sexo, peso):
        self.nombre = nombre
        self.tipo = tipo
        self.raza = raza
        self.sexo = sexo
        self.peso = peso

    def jugar(self):
        pass
    def getRaza(self):
        return self.raza
    def setSexo(self, sexo):
        self.sexo = sexo