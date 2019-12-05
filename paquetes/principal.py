#forma 1

'''import calculadora

resultado = calculadora.suma(10,20)
print(resultado)'''

#from calculadora import * # * hace referencia a todas las funciones de la clase, si necesito solo una funion solo llamo a la funcion necesaria.

import calculadora
from animales.aves import Pinguino
from animales import *

pinguino = Pinguino()
pinguino.nadar()

print(__name__)

#forma para importar ls funciones individualmente
'''from calculadora import suma
from calculadora import resta
from calculadora import multiplicacion
from calculadora import division'''

#importar todas las funciones en una linea de codigo
#from calculadora import (suma, resta, division, multiplicacion)

#Se puede renombrar la funcion usando as despues de invocar a la funion
#from calculadora import suma as nueva_suma
#resultado = nueva_suma(10,20)

#print(resultado)


