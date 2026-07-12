# objeto = Um conjunto de atributos relacionados (variáveis) e métodos (funções)
#           Ex: celular, xícara, livro...
#           Você precisa de uma "classe" para criar muitos objetos

# class = (modelo) usado para projetar a estrutura e o layout de um objeto

from carro import Carro

carro1 = Carro("Porsche 911 GT3 RS", 2026, "Prata", False)
carro2 = Carro("Nissan Skyline GT-R R34", 2000, "Branco", False)
carro3 = Carro("Aston Martin DB5", 1964, "Azul-Marinho", True)

print("")

# print(carro1.modelo)
# print(carro1.ano)
# print(carro1.cor)
# print(carro1.a_venda)

# print("")

# print(carro2.modelo)
# print(carro2.ano)
# print(carro2.cor)
# print(carro2.a_venda)

# print("")

# print(carro3.modelo)
# print(carro3.ano)
# print(carro3.cor)
# print(carro3.a_venda)

# print("")

# carro1.dirigir()
# carro1.parar()

# print("")

# carro2.dirigir()
# carro2.parar()

# print("")

# carro3.dirigir()
# carro3.parar()

# print("")

print("")

carro1.descrever()

print("")

carro2.descrever()

print("")

carro3.descrever()

print("")