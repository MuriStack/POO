# Composição = O objeto composto possui diretamente seus componentes, que não podem existir de forma independente 
#              (relação 'tem um')

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Roda:
    def __init__(self, tamanho):
        self.tamanho = tamanho

class Carro:
    def __init__(self, marca, modelo, potencia, roda_tamanho):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(potencia)
        self.rodas = [ Roda(roda_tamanho) for roda in range(4)]

    def descrever(self):
        return f"{self.marca} {self.modelo} {self.motor.potencia}hp {self.rodas[0].tamanho}in"

carro1 = Carro(marca="Ford", modelo="Mustang", potencia=500, roda_tamanho=18)
carro2 = Carro(marca="Chevrolet", modelo="Corvette", potencia=670, roda_tamanho=19)

print(carro1.descrever())
print(carro2.descrever())