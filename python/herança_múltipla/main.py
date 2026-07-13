# Herança múltipla = Herdar de mais de uma classe pai.
#                    C(A, B)

# Herança multinível = Herda de uma classe pai que herda de outra classe pai.
#                      A -> B(A) -> C(B)

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"Este {self.nome} está comendo")

    def dormir(self):
        print(f"Este {self.nome} está dormindo")

class Presa(Animal):
   def fugir(self):
       print(f"Este {self.nome} está fugindo")

class Predador(Animal):
    def caçar(self):
        print(f"Este {self.nome} está caçando")

class Coelho(Presa):
    pass

class Falcão(Predador):
    pass

class Peixe(Presa, Predador):
    pass

coelho = Coelho("Perna longa")
falcao = Falcão("Falcão")
peixe = Peixe("Nemo")

# print("")

# coelho.fugir()

# print("")

# falcao.caçar()

# print("")

# peixe.caçar()
# peixe.fugir()

# print("")

# coelho.comer()

# print("")

# peixe.dormir()

# print("")