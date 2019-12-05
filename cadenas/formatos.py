texto = "      Curso de python 3, PYTHON BASIC     "

#Retorna un string con mayus initial
resultado = texto.capitalize()

#retorna un string donde las mayusculas las pasa a minisculas y min a mayus
resultado2 = texto.swapcase()

#retorna un string con texto en mayusculas
resultado3  = texto.upper()

#retorna todo en minusculas
resultado4  = texto.lower()

#Remplaza texto
resultado5 = texto.replace("python", "JAVA", 1)

#Elimina espacios en string
resultado6 = texto.strip()


#----------------------------------------

curso = "Python"
version = "3"

#Insertar variables en string -- con respecto a la posicion 
resultadonew = "Curso de %s %s" %(curso, version)

#Insertar variable en string con format  -- podemos nombrar a la variables a usar
resultadonew2 = "Curso de {a} {b}".format(a = curso, b=version)
print(resultadonew2)