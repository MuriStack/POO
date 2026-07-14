# Polimorfismo = Palavra grega que significa "ter muitas formas ou faces"
#                Poli = Muitos/Muitas
#                morfo = Formas

#                DUAS MANEIRAS DE ALCANÇAR O POLIMORFISMO
#                1. Herança = Um objeto pode ser tratado como sendo do mesmo tipo que uma classe pai.
#                2. "Duck typing" = O objeto deve possuir os atributos/métodos necessários.

from abc import ABC, abstractmethod

class Formato:

    @abstractmethod
    def area(self):
        pass

class Circulo(Formato):

    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio ** 2

class Quadrado(Formato):

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Triangulo(Formato):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5
    
class Pizza(Circulo):

    def __init__(self, sabor, raio):
        super().__init__(raio)
        self.sabor = sabor

formatos = [
    Circulo(4),
    Quadrado(5),
    Triangulo(6, 7),
    Pizza("Calabresa", 15)
]

for shape in formatos:
    print(f"{shape.area()}cm²")