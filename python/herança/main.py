# Herança = Permite que uma classe herde atributos e métodos de outra classe.
#           Auxilia na reutilização e na extensibilidade do código.
#           classe Filho(Pai).

class Animal:
    def __init__(self, nome):
        self.nome = nome
        self.vivo = True

    def comer(self):
        print(f"{self.nome} está comendo")

    def dormir(self):
        print(f"{self.nome} está dormindo")

class Cachorro(Animal):
    def latir(self):
        print("WOOF")

class Gato(Animal):
    def miar(self):
        print("MIAU")

class Rato(Animal):
    def chiar(self):
        print("CHIII")

canino = Cachorro("Scooby")
felino = Gato("Garfield")
roedor = Rato("Jerry")

# print("")

# print(canino.nome)
# print(canino.vivo)
# canino.comer()
# canino.dormir()

print("")

canino.latir()

print("")

felino.miar()

print("")

roedor.chiar()

print("")