class Estadio():
    def __init__(self, nombre, equipo, capacidad, ubicacion, deporte):
        self.nombre = nombre
        self.equipo = equipo
        self.capacidad = capacidad
        self.ubicacion = ubicacion
        self.deporte = deporte

    def jugar(self):
        pass
    def getCapacidad(self):
        return self.capacidad
    def setDeporte(self, deporte):
        self.deporte = deporte