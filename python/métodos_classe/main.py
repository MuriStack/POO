# Métodos de classe = Permitir operações relacionadas à própria classe.
#                     Receba (cls) como o primeiro parâmetro, o qual representa a própria classe.

class Estudante:

    count = 0
    total_gpa = 0

    def __init__(self, nome, gpa):
        self.nome = nome
        self.gpa = gpa
        Estudante.count += 1
        Estudante.total_gpa += gpa

    # MÉTODO DE INSTÂNCIA
    def obter_info(self):
        return f"{self.nome} = {self.gpa}"

    @classmethod
    def obter_contagem(cls):
        return f"Total de estudantes: {cls.count}"
    
    @classmethod
    def media_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{(cls.total_gpa / cls.count):.2f}"
    
estudante1 = Estudante("Bob Esponja", 3.2)
estudante2 = Estudante("Patrick", 2.0)
estudante3 = Estudante("Sandy", 4.0)

print(Estudante.obter_contagem())
print(Estudante.media_gpa())