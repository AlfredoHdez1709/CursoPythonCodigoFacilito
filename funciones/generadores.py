def tabla_multiplicar(numero, maximo):
    for posicion in range(1, maximo+1):
        yield numero * posicion, numero, posicion

print("Tabla  de multiplicar: ")
variable = int(input())

print("Numero de items: ")
maximo = int(input())

for resultado, numero, posicion in tabla_multiplicar(variable, maximo):
    print(numero, "*",posicion, "=", resultado)