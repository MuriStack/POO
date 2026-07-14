# super() = Função utilizada em uma classe filha para chamar métodos de uma classe pai (superclasse).
#           Permite estender a funcionalidade dos métodos herdados.

class Formato:

    def __init__(self, cor, preenchido):
        self.cor = cor
        self.preenchido = preenchido

    def descrever(self):
        print(f"Isso é {self.cor} e {'preenchido' if self.preenchido else 'não preenchido'}")

class Circulo(Formato):

    def __init__(self, cor, preenchido, raio):
        super().__init__(cor, preenchido)
        self.raio = raio

    def descrever(self):
        super().descrever()        
        print(f"É um círculo com área de {3.14 * (self.raio)**2}cm²")

class Quadrado(Formato):

    def __init__(self, cor, preenchido, lado):
        super().__init__(cor, preenchido)
        self.lado = lado

    def descrever(self):
        super().descrever()        
        print(f"É um quadrado com área de {self.lado**2}cm²")

class Triangulo(Formato):

    def __init__(self, cor, preenchido, base, altura):
        super().__init__(cor, preenchido)
        self.base = base
        self.altura = altura
    
    def descrever(self):
        super().descrever()        
        print(f"É um triângulo com área de {self.base * self.altura/2}cm²")

circulo = Circulo(cor="Vermelho", preenchido=True, raio=5)
quadrado = Quadrado(cor="Azul", preenchido=False, lado=6)
triangulo = Triangulo(cor="Amarelo", preenchido=True, base=7, altura=8)

print(circulo.cor)
print(circulo.preenchido)
print(f"{circulo.raio}cm")

print("")

print(quadrado.cor)
print(quadrado.preenchido)
print(f"{quadrado.lado}cm")

print("")

print(triangulo.cor)
print(triangulo.preenchido)
print(f"{triangulo.base}cm")
print(f"{triangulo.altura}cm")

print("")

circulo.descrever()
quadrado.descrever()
triangulo.descrever()