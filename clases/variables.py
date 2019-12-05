#variables d einstancia y de clase

class Circulo:
    pi = 3.14159265 # es una variable de clase - Solo le pertenece a la clase y puede ser usada por instncias
    def __init__(self, radio):
        self.radio = radio #Radio es una variable de instancia - cada variable es independiente de cada una de ellas

circulo_a = Circulo(10)
circulo_b = Circulo(20)

circulo_b.radio = 100
print(circulo_a.pi)
print(circulo_b.radio)
        