class Livro(object):

    def __init__(self, titulo, autores, paginas, preco):
        self.titulo = titulo
        self.autores = autores
        self.paginas = paginas
        self.preco = preco

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_autores(self):
        return self.autores

    def set_autores(self, n_autores):
        if isinstance(n_autores, list) and len(n_autores) > 0:
            self.autores = n_autores

    def mostra_autores(self):
        print("Autores:")
        for i, autor in enumerate(self.autores):
            print(f'{i+1} - {autor}')

    def acrescenta_autor(self,autor):
        self.autores.append(autor)

    def remove_autor(self,autor):
        if autor in self.autores:
            self.autores.remove(autor)
            print('Remoção realizada com sucesso')
        else:
            print(f'- Erro(remove): autor {autor} não est[a cadastrado.')

    def pesquisa_autor(self, autor):

        if autor in self.autores:
            print('Autor encontrado')
        else:
            print('Autor não encontrado')

    def get_paginas(self):
        return self.paginas

    def set_paginas(self, paginas):
        self.paginas = paginas

    def get_preco(self):
        return self.preco

    def set_preco(self, preco):
        self.preco = preco


def valorPagina(paginas, preco):
    return preco / paginas


def desconto(preco, v2):
    return preco - preco * v2 / 100

def __str__(self):
    return f'{self.titulo}{self.autores}{self.paginas}{self.preco}'


if __name__ == '__main__':

# LIVRO 1

    livro1 = Livro("Senhora", ["José de Alencar", "bla"], 200, 15)
    print("Título:", livro1.get_titulo())
    livro1.mostra_autores()
    print("Páginas:", livro1.paginas, "\nPreço:", livro1.preco)

    #Mudar autores
    livro1.set_autores(["João", "Maria"])
    livro1.mostra_autores()
    print("\nPáginas:", livro1.paginas, "\nPreço:", livro1.preco)

    # Mudar valores das páginas e colocar desconto
    print("Valor por página:", valorPagina(livro1.paginas, livro1.preco))
    print("Valor com desconto de 20%:", desconto(livro1.preco, 20))

    # Acrescentar autores
    livro1.acrescenta_autor("Roberto")
    livro1.mostra_autores()

    # Remover autores
    livro1.remove_autor(4)
    livro1.remove_autor("Roberto")
    livro1.mostra_autores()

    # Pesquisar autores
    livro1.pesquisa_autor("Maria")
    livro1.pesquisa_autor(5)

# LIVRO 2

    livro2 = Livro("As crônicas de Nárnia", ["C.S. Lewis"], 2000, 200)
    print("\nTítulo:", livro2.titulo)
    livro2.mostra_autores()
    print("Páginas:", livro2.paginas, "\nPreço:",livro2.preco)

    # Mudar valores das páginas e colocar desconto
    print("Valor por página:", valorPagina(livro2.paginas, livro2.preco))
    print("Valor com desconto de 20%:", desconto(livro2.preco, 20))