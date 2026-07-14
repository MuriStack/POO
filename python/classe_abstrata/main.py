# Classe abstrata: Uma classe que não pode ser instanciada por si só; Destinada a ser estendida (ter subclasses).
#                  Elas podem conter métodos abstratos, que são declarados, mas não possuem implementação.
#                  Benefícios das classes abstratas:
#                  1. Impede a instanciação da própria classe.
#                  2. Exige que as subclasses implementem métodos abstratos herdados.

from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def ir(self):
        pass

    @abstractmethod
    def parar(self):
        pass

class Carro(Veiculo):

    def ir(self):
        print("Você DIRIGE o carro")

    def parar(self):
        print("Você PARA o carro")

class Moto(Veiculo):

    def ir(self):
        print("Você DIRIGE a moto")

    def parar(self):
        print("Você PARA a moto")

class Barco(Veiculo):

    def ir(self):
        print("Você NAVEGA o barco")

    # def parar(self):
    #     print("Você ANCORA o barco")