# Métodos mágicos = Métodos dunder (underline) __init__, __str__, __eq__
#                   Eles são chamados automaticamente por muitas das operações nativas do Python.
#                   Eles permitem que os desenvolvedores definam ou personalizem o comportamento de objetos.

class Livro:

    def __init__(self, titulo, autor, num_pags):
        self.titulo = titulo
        self.autor = autor
        self.num_pags = num_pags

    def __str__(self):
        return f"{self.titulo} por {self.autor}"
    
    def __eq__(self, outro):
        return self.titulo == outro.titulo and self.autor == outro.autor
    
    def __gt__(self, outro):
        return self.num_pags > outro.num_pags
    
    def __add__(self, outro):
        return f"{self.num_pags + outro.num_pags} páginas"
    
    def __contains__(self, palavra_chave):
        return palavra_chave in self.titulo or palavra_chave in self.autor
    
    def __getitem__(self, chave):
        
        if chave == "titulo":
            return self.titulo
        elif chave == "autor":
            return self.autor
        elif chave == "num_pags":
            return self.num_pags
        else:
            return "Chave inválida"

livro1 = Livro("Hobbit", "J. R. R. Tolkien", 310)
livro2 = Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling", 223)
livro3 = Livro("O Leão, a Feiticeira e o Guarda-Roupa", "C.S. Lewis", 172)

print(livro1['titulo'])