#Questão 2 da prova corrigida:

# 2. Modele a classe Curso com os atributos nome do curso, valor do curso e os alunos.
# Usando o conceito de associação de classes, o atributo alunos da classe Curso deve ser os objetos da classe Aluno.
# Lembrando que um curso pode ter vários alunos.
# Implemente a classe Curso com o construtor, os métodos gets e sets necessários e estes métodos funcionais dentro da classe Curso:
# - insere_aluno, ele inclui um aluno no curso;
# - mostra_dados_curso, ele mostra todos os dados do curso;
# - consulta_nome_alunos, ele mostra a relação com o nome de todos os alunos do curso.
# E a classe Aluno tem os atributos ra do aluno e nome do aluno. Implemente a classe Aluno com o construtor, e pelo menos um método gets e um método set.
# No método main, crie dois objetos da classe aluno e pelo menos um objetos da classe Curso. Em cada curso cadastre alguns alunos.
# E teste todos os métodos desenvolvidos.
# Prof. Barbosa.

class Aluno:
    def __init__(self,ra,nome):
        self.ra = ra
        self.nome = nome

    #Métodos gets e sets.
    def get_ra(self):
        return self.ra
    def set_ra(self):
        self.ra = ra
    def get_nome(self):
        return self.nome
    def set_nome(self):
        self.nome = nome

class Curso:
    def __init__(self,nome,valor):
        self.nome = nome
        self.valor = valor
        self.alunos = []

    # Métodos gets e sets.
    def get_nome(self):
        return self.nome
    def set_nome(self):
        self.nome = nome
    def get_valor(self):
        return self.valor
    def set_valor(self):
        self.valor = valor

    # Método para inserir os alunos nos cursos.
    def insere_aluno(self,aluno):
        self.alunos.append(aluno)

    # Método para mostrar os dados do curso.
    def mostra_dados_curso(self):
        print("\nNome do curso:", self.nome, "\nValor:", self.valor)

    # Método para consultar o nome dos alunos no curso.
    def consulta_nome_alunos(self):
        if not self.alunos:
            print("Sem alunos")
        else:
            for o_aluno in self.alunos:
                print("\nCurso:", self.nome,"\nAluno:",o_aluno.get_nome())

if __name__ == '__main__':
    #Cadastro dos alunos.
    aluno1 = Aluno("66666666", "Pedro")
    aluno2 = Aluno("22222222", "Maria")
    aluno3 = Aluno("33333333", "João")

    #Cadastro dos cursos.
    curso1 = Curso("Matemática", 100)
    curso2 = Curso("Física", 200)

    #Método para inserir os alunos nos cursos.
    curso1.insere_aluno(aluno1)
    curso1.insere_aluno(aluno2)
    curso2.insere_aluno(aluno3)

    #Teste do método para mostrar dados do curso.
    Curso.mostra_dados_curso(curso1)
    Curso.mostra_dados_curso(curso2)

    #Teste do método para consultar o nome dos alunos.
    curso1.consulta_nome_alunos()
    curso2.consulta_nome_alunos()