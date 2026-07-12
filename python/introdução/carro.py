class Carro:
    def __init__(self, modelo, ano, cor, a_venda):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.a_venda = a_venda

    def dirigir(self):
        print(f"Você dirige o {self.modelo} {self.cor}")

    def parar(self):
        print(f"Você para o {self.modelo} {self.cor}")

    def descrever(self):
        print(f"{self.modelo} {self.cor} {self.ano}")