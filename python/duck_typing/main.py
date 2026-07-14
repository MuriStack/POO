# "Duck typing" = Outra maneira de alcançar o polimorfismo, além da herança.
#                 O objeto deve possuir os atributos/métodos mínimos necessários.
#                 "Se parece um pato e grasna como um pato, deve ser um pato."

class Animal:

    vivo = True

class Cachorro(Animal):

    def falar(self):
        print("WOOF!")

class Gato(Animal):

    def falar(self):
        print("MIAU!")

class Carro:

    vivo = True

    def falar(self):
        print("HONK")

animais = [
    Cachorro(),
    Gato(),
    Carro()
]

for animal in animais:
    animal.falar()
    print(animal.vivo)