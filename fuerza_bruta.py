from string import ascii_letters, digits
from itertools import product

caracteres = ascii_letters+digits

def buscador(con):
  archivo = open("combinaciones.txt","w")

 if 3 <= len(con) <= 4:
  for i in range(3,5):
    for comb in product(caracteres, repeat= i):
      prueba = "".join(comb)

      archivo.write(prueba+"\n")
      if prueba == con:
        print("Tu contraseña es: {}".format(prueba))
        archivo.close()
        break
else
 print("Introduce una contraseña de longitud entre 3 y 4 caracteres")
