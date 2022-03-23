'''
1 - Crie um projeto usando o conceito de POO com herança (inheritance) contendo a superclasse
(classe pai) Pessoa e duas subclasses (classes filhas) Professor e Funcionário.
2 - A superclasse Pessoa tem o atributo de instância nome
3 - O construtor da superclasse recebe o parâmetro nome e armazena no atributo nome.
4 - Os métodos get e set referente ao atributo nome. Faça crítica no set
5 - A primeira subclasse Professor tem os atributos de instância nome e qtd_turma
6 - O construtor da subclasse Professor recebe os dois parâmetros e chama o construtor
da superclasse enviado o nome e depois armazena o valor inteiro no atributo qtd_turma.
7 - Use valor default (padrão) no construtor
8 - Cadastre um professor no sistema
9 - Use os métodos get e set de nome e qtd de turma
10 - No método set referente ao atributo qtd_turma, faça pelo menos uma crítica.
11 - Crie o método rendimentos, ele recebe o valor em reais que o professor ganha por turma
que ministra e retorna o valor dos seus rendimentos, o objetivo é calcular o rendimento
do professor que depende da quantidade de turmas e do valor que ele ganha por turma.
12 - No método main, crie pelo menos um objeto da subclasse Professor e use os métodos do sistema
para o objeto instanciado.
13 - E a segunda subclasse Funcionário tem os atributos de instância nome e salario
14 - O construtor da subclasse Funcionário recebe dois parâmetros e chama o construtor
da superclasse enviando o nome e depois armazena o valor float no atributo salário.
15 - Use valor default (padrão) no construtor
16 - No método set referente ao atributo salario, faça uma crítica.
17 - No método main, crie pelo menos um objeto da subclasse Funcionario e use os métodos do sistema
para o objeto instanciado.
18 - O sistema precisa saber quantas pessoas tem cadastro no sistema.
Crie o atributo de classe e método de classe necessários para atender essa necessidade.
19 - Crie uma lista e adicione todos os objetos instanciados.
20 - Crie um método de classe para mostrar os dados de todas as pessoas.

'''

class Pessoa(object):
    qtd = 0

    def __init__(self,nome):
        self.nome = nome
        Pessoa.qtd += 1  #atributo de classe (contar as pessoas que são acrescentadas)

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self.nome = novo_nome
        else:
            print("Erro(set_nome): tipo inválido")

    @classmethod
    def get_qtd(cls):
        return Pessoa.qtd

class Professor(Pessoa):
    def __init__(self, nome, qtd_turmas=1):
        super().__init__(nome)
        self.qtd_turmas = qtd_turmas

    def get_qtd_turmas(self):
        return self.qtd_turmas

    def set_qtd_turmas(self, nova_qtd_turmas):
        if isinstance(nova_qtd_turmas, int):
            self.qtd_turmas = nova_qtd_turmas
        else:
            print("Erro(set_qtd_turmas): tipo inválido")

    def rendimentos(self):
        valor = float(input("\nValor por turma: "))
        rendimentos = valor * self.qtd_turmas
        print("Rendimentos:", rendimentos)

    def mostra_dados(self):
            print("\nProfessor(a)", "\nNome:", self.nome, "\nTurmas:", self.qtd_turmas)

class Funcionario(Pessoa):
    def __init__(self, nome, salario=2000.00):
        super().__init__(nome)
        self.salario = salario

    def get_salario(self):
        return self.salario

    def set_salario(self, novo_salario):
        if isinstance(novo_salario, float):
            self.salario = novo_salario
        else:
            print("Erro(set_salario): tipo inválido")

    def mostra_dados(self):
            print("\nFuncionário(a)", "\nNome:", self.nome, "\nSalario:", self.salario)

if __name__ == '__main__':

    p1 = Professor("João",3)
    print(p1)
    print("Nome:", p1.get_nome(), "\nTurmas:", p1.get_qtd_turmas())
    p1.set_nome("Alice")
    print(f"Nome: {p1.get_nome()}","\nTurmas:", p1.get_qtd_turmas())
    p1.rendimentos()
    print("\nPessoas cadastradas:", Pessoa.qtd)

    p2 = Funcionario("José")
    print("\nNome:", p2.get_nome(), "\nSalário:", p2.get_salario())
    p2.set_salario(3000.00)
    print("Nome:", p2.get_nome(), "\nSalário:", p2.get_salario())
    print("\nPessoas cadastradas:", Pessoa.qtd)

    lista_p1= [p1.get_nome(), p1.get_qtd_turmas()]
    lista_p2= [p2.get_nome(), p2.get_salario()]

    print("Pessoa 1 :", lista_p1, "\nPessoa 2 :", lista_p2)

    p1.mostra_dados()
    p2.mostra_dados()

