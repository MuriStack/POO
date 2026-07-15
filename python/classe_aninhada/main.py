# Classe aninhada = Uma classe definida dentro de outra classe
#                   class externa:
#                       class interna:

# Benefícios: Permite agrupar logicamente classes que estão intimamente relacionadas.
#             Encapsula detalhes privados que não são relevantes fora da classe externa.
#             Mantém o namespace limpo; reduz a possibilidade de conflitos de nomes.

class Empresa:
    
    class Funcionario:

        def __init__(self, nome, cargo):
            self.nome = nome
            self.cargo = cargo

        def obter_detalhes(self):
            return f"{self.nome} {self.cargo}"

    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, nome, cargo):
        novo_funcionario = self.Funcionario(nome, cargo)
        self.funcionarios.append(novo_funcionario)

    def listar_funcionarios(self):
        return [funcionario.obter_detalhes() for funcionario in self.funcionarios]

empresa1 = Empresa("Siri Cascudo")
empresa2 = Empresa("Balde de Lixo")

empresa1.adicionar_funcionario("Sr. Sirigueijo", "Dono")
empresa1.adicionar_funcionario("Bob Esponja", "Cozinheiro")
empresa1.adicionar_funcionario("Lula Molusco", "Caixa")

empresa2.adicionar_funcionario("Plankton", "Dono")
empresa2.adicionar_funcionario("Karen", "Assistente")

for funcionario in empresa1.listar_funcionarios():
    print(funcionario)

print("")

for funcionario in empresa2.listar_funcionarios():
    print(funcionario)