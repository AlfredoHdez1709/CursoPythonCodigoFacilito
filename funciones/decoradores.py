#a, b, c
#a(b) -> c

def decorador(funcion):
    def nueva_funcion():
        print("Podemos agregar codigo antes")
        funcion()
        print("Podemos agregar codigo despues")
    return nueva_funcion 

@decorador
def function_a_decorar():
    print("Este es una funcion a decorar")
function_a_decorar()