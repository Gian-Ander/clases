class Perro():
    def __init__(self, nombre, raza, sexo, peso, color_pelo):
        self.nombre = nombre
        self.raza = raza
        self.sexo = sexo
        self.peso = peso
        self.color_pelo = color_pelo

    def jugar(self):
        return self.nombre + " es un perro de raza " + self.raza + " y juega feliz en el patio"

    def setPeso(self, peso):
        self.peso = peso

    def getRaza(self):
        return self.raza