class Animal:
    def comer(self):
        print("Comiendo")

    def dormir(self):
        print("Durmiendo")

    def comun(self):
        print("Este es un metodo de animal")

class Mascota:
    def fecha_adopcion(self, fecha):
        self.fecha_adopcion = fecha
    def comun(self):
        print("Este es un metodo de mascota")

class Perro(Animal, Mascota):
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print("Ladrando")

    def comun(self):
        print("Este es un metodo de perro")

    def dormir(self):
        print(self.nombre, " esta durmiendo")
        Animal.dormir(self)
        print("No molestar")
        
firulais = Perro("Firulais")
firulais.dormir()

"""firulais.fecha_adopcion("Hoy")
print(firulais.fecha_adopcion)
firulais.ladrar()
firulais.comer()
firulais.dormir()
firulais.comun()"""