class Auto():
    def __init__(self, placa, color, vel_max, llantas, asientos):
        self.placa = placa
        self.color = color
        self.vel_max = vel_max
        self.llantas = llantas
        self.asientos = asientos

    def acelerar(self):
        pass
    def getPlaca(self):
        return self.placa
    def setAsientos(self, asientos):
        self.asientos = asientos