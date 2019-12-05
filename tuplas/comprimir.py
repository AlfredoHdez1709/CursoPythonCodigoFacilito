tupla = (1,2,3,4,5,6)
lista = [10, 20, 30, 40]


"""
uno, dos, tres, *cuatro = tupla 
# tupla[0], tupla[1], tupla[2], tupla[3]

print(uno)
print(dos)
print(tres)
print(cuatro)


lista = [10, 20, 30, 40]
"""

#return objeto de tipo zip
resultado = zip(tupla, lista)
resultado = tuple(resultado)

print(resultado)
