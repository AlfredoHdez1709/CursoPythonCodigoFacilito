mensaje = "Este es un texto un poco grande en cuanto a longitud de caracteres se refiere"

#Funciones para busqueda de palabras
#resultato = mensaje.count("z")
#resultato = "texto" in mensaje

#Metodo find

#Retorna la pocision de la primer letra del string
#resultato = mensaje.find("texto")

resultato = mensaje[resultato: resultato + len("texto") ]

print(resultato)