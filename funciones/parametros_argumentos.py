def crear_usuario(nombre, apellido, edad=0):
    return{
        'nombre':nombre,
        'apellido':apellido,
        'nombre_completo': "{} {}".format(nombre, apellido),
        'edad':edad
    }

codi = crear_usuario("Codi","Facilito",6)

print(codi["nombre"])
print(codi["apellido"])
print(codi["edad"])