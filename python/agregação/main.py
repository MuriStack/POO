# Agregação = Representa um relacionamento em que um objeto (o todo)
#             contém referências a um ou mais objetos INDEPENDENTES (as partes)

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        return [f"{livro.titulo} por {livro.autor}"for livro in self.livros]

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

biblioteca = Biblioteca("Biblioteca pública de Nova York")

livro1 = Livro("Harry Potter...", "J.K. Rowling")
livro2 = Livro("A Metamorfose", "Franz Kafka")
livro3 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

print(biblioteca.nome)

for livro in biblioteca.listar_livros():
    print(livro)