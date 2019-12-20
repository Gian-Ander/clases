import estadio
import futbolista
import os
nom = os.sys.argv[1]
eq = os.sys.argv[2]
es = os.sys.argv[3]
e = estadio.Estadio(nom, "Barcelona", 96000, "España", "Futbol")
f = futbolista.Futbolista("L. Suarez", eq, es, "Delantero", "Santander")
print(f.jugar())