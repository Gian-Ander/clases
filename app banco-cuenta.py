import banco
import cuenta
import os
tit = os.sys.argv[1]
ban = os.sys.argv[2]
b = banco.Banco(ban, "Av. Las Rosas", "41 %", 2451, "Si")
c = cuenta.Cuenta("Ahorros", "Interbank", tit, 2092, 478563214587452)
print(c.ahorrar())