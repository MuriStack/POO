# Variáveis de classe = Compartilhado entre todas as instâncias de uma classe.
#                       Definido fora do __init__.
#                       Permite compartilhar dados entre todos os objetos criados a partir dessa classe.

class Estudante:

    ano_de_formatura = 2026
    num_estudantes = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Estudante.num_estudantes += 1

estudante1 = Estudante("Bob Esponja", 39)
estudante2 = Estudante("Patrick Estrela", 39)
estudante3 = Estudante("Lula Molusco", 39)
estudante4 = Estudante("Sandy", 39)

# print("")

# print(estudante1.nome)
# print(estudante1.idade)
# print(Estudante.ano_de_formatura)

# print("")

# print(Estudante.num_estudantes)

print("")

print(f"Minha turma de {Estudante.ano_de_formatura} tem {Estudante.num_estudantes} alunos:")

print("")

print(estudante1.nome)
print(estudante2.nome)
print(estudante3.nome)
print(estudante4.nome)


print("")