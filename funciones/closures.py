#clousure- cuando una funcion genere una nueva funcion y pueda acceder a las variables locales de la primer funcion

def monstrar_mensaje(mensaje):
    mensaje = mensaje.title()
    def mostrar():
        print(mensaje)
    return mostrar
nueva_funcion = monstrar_mensaje("Codigo Facilito")
nueva_funcion()