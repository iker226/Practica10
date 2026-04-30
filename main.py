from time import time
from fuerza_bruta import buscador

to = time()
con = 'H014'
buscador(con)
t1 = time()
t2 = round(t1-t0, 6)
print("El tiempo de ejecucion fue {}".format(t2))
