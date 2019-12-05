diccionario = {"a":1, "b":2, "c":3, "a":4}

#busqueda de llaves
resultado = "a" in diccionario

#busqueda con get
resultado1 = diccionario.get("z","La llave no existe")

#setdefault - en caso de que la llave no exista se agrega otro valor 

resultado2 = diccionario.setdefault("z",{})
print(resultado2, diccionario)