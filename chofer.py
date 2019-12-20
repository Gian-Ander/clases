class Chofer():
    def __init__(self, nombre, edad, auto, peso, sexo):
        self.nombre = nombre
        self.edad = edad
        self.auto = auto
        self.peso = peso
        self.sexo = sexo
    def conducir(self):
        return "El chofer " + self.nombre + " conduce el auto de color " + self.auto.color
    def setNombre(self, nombre):
        self.nombre = nombre
    def getPeso(self):
        return self.peso