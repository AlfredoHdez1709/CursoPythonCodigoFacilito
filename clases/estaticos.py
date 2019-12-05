#Metodos que se usan sin necesidad de usar instancias

class Triangulo:
    #No podemos usar variables de instancias pero si variables de clase
    numero = 2
    @staticmethod
    def area(base, altura):
        return(base * altura) / Triangulo.numero
resultado = Triangulo.area(10, 20)
print(resultado)