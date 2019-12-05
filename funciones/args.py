def suma (parametro_requerido,*args):
    total = 0
    print(parametro_requerido)
    for valor in args:
        total += valor
    return total

def usuarios_autenticados(**kwargs):
    print(kwargs)

resultado = suma("Este es un argumento requerido",10, 20, 30, 30, 300)
print(resultado)

print(usuarios_autenticados(codi = True, facilito=False))
