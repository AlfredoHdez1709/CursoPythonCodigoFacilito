lenguajes = "Python; Java; Rube; PHP; Swift; JavaScript; C#; C; C++"

#split - Retorna una nueva lista a partir de texto 
result = lenguajes.split(";")
#print(result)

#join - retorna un string a partir de una lista

nuevo_string = "_".join(result)
#print(nuevo_string)


texto = """Ete es un texto 
con 
falto
de 
linea"""

resultado = texto.splitlines()
print(resultado)

