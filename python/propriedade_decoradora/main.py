# @property = Decorador usado para definir um método como uma propriedade (ele pode ser acessado como um atributo).
#             Benefício: Adicionar lógica adicional ao ler, gravar ou excluir atributos.
#             Fornece métodos getter, setter e deleter.

class Retangulo:

    def __init__(self, largura, altura):
        self._largura = largura
        self._altura = altura

    @property
    def largura(self):
        return f"{self._largura:.1f}cm "

    @property
    def altura(self):
        return f"{self._altura:.1f}cm "

    @largura.setter
    def largura(self, nova_largura):
        if nova_largura > 0:
            self._largura = nova_largura
        else:
            print("Largura tem que ser maior que zero")

    @altura.setter
    def altura(self, nova_altura):
        if nova_altura > 0:
            self._altura = nova_altura
        else:
            print("Altura tem que ser maior que zero")

    @largura.deleter
    def largura(self):
        del self._largura
        print("Largura foi deletada")

    @altura.deleter
    def altura(self):
        del self._altura
        print("Altura foi deletada")

retangulo = Retangulo(3, 4)

print(retangulo.largura)
print(retangulo.altura)

print("")

print(retangulo._largura)
print(retangulo._altura)

print("")

retangulo.largura = 5
retangulo.altura = 6

print("")

del retangulo.largura
del retangulo.altura