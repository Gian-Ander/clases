import mascota
import perro
import os
nom = os.sys.argv[1]
raz = os.sys.argv[2]
m = mascota.Mascota("Pancho", "gato", "normal", "Macho", "4 kg")
p = perro.Perro(nom, raz, "Macho", 7, "Negro")
print(p.jugar())