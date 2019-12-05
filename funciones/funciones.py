def saluda():
    print("Hola mundo")

def crear_mensaje(nombre):
    mensaje = "Hola {}, al curso".format(nombre)
    return mensaje

def obtener_curso():
    return "Curso de Python ", "Basico",3.6


def suma (val1, val2, val3):
    return val1 + val2 + val3

print(crear_mensaje("Alfredo"))
print(print(suma(2,3,70)))

curso, nivel, version = obtener_curso()
print(curso, nivel, version)