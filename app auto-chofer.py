import auto
import chofer
import os
pla = os.sys.argv[1]
vel = os.sys.argv[2]
a = auto.Auto(pla, "rojo", 180, 4, 6)
c = chofer.Chofer("Luis", 38, a, 92, vel)
print(c.conducir())