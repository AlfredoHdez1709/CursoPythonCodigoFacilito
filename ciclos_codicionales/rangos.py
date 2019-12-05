lista = [1,2,3,4,5,6]
#for valor in range(len(lista)):
#    print("indice: " , valor, "valor: ", lista[valor])


for indice, valor in enumerate(lista, 10):
    print("indice: " , indice,  "Valor: ", valor)