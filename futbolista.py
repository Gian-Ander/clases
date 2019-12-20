class Futbolista():
    def __init__(self, nombre, equipo, estadio, posicion, liga):
        self.nombre = nombre
        self.equipo = equipo
        self.estadio = estadio
        self.posicion = posicion
        self.liga = liga

    def jugar(self):
        return self.nombre + " juega en el equipo " + self.equipo + "y su estadio es " + self.estadio

    def setEdad(self, edad):
        self.edad = edad

    def getLiga(self):
        return self.liga