class Cuenta():
    def __init__(self, tipo_cuenta, banco, titular, saldo, nro_cuenta):
        self.tipo_cuenta = tipo_cuenta
        self.banco = banco
        self.titular = titular
        self.saldo = saldo
        self.nro_cuenta = nro_cuenta

    def ahorrar(self):
        return "El señor " + self.titular + " tiene una cuenta de ahorros en el banco " + self.banco

    def setSaldo(self, saldo):
        self.saldo = saldo

    def getNro_cuenta(self):
        return self.nro_cuenta