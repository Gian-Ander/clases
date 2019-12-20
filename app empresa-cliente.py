import empresa
import cliente
import os
nom = os.sys.argv[1]
prop = os.sys.argv[2]
e = empresa.Empresa(prop, "Av. Grau", 45876321, 1254782451, "Si")
c = cliente.Cliente(nom, "Calle Los Incas", "Gloria", 84752092, 120)
print(c.adquirir())