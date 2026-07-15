# Métodos estáticos = Um método que pertence a uma classe, em vez de a qualquer objeto dessa classe (instância).
#                     Geralmente usado para funções utilitárias gerais.

# Métodos de instância = Mais adequados para operações em instâncias da classe (objetos).
# Métodos estáticos = Ideais para funções utilitárias que não precisam de acesso aos dados da classe.

class Funcionario:

    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

    def obter_info(self):
        return f"{self.nome} = {self.cargo}"
    
    @staticmethod
    def cargo_valido(cargo):
        cargos_validos = ["Gerente", "Caixa", "Cozinheiro", "Zelador"]
        return cargo in cargos_validos
    
funcionario1 = Funcionario("Sr. Sirigueijo", "Dono")
funcionario2 = Funcionario("Lula Molusco", "Caixa")
funcionario3 = Funcionario("Bob Esponja", "Cozinheiro")

print(funcionario1.obter_info())
print(funcionario2.obter_info())
print(funcionario3.obter_info())