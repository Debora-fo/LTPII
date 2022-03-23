'''Teoria:
- Uma classe abstrata deve herdar de ABC (Abstract Base Classes)
- A superclasse abstrata FormaGeometrica com os métodos abstratos area e perímetro.
- As subclasses Circulo e Quadrado herdam da superclasse abstrata FormaGeometrica e tem
que implementar todos os métodos abstratos da superclasse.

- Analise o problema da figura geométrica e o cálculo da área e do perímetro.

Implemente:
1- Crie a superclasse abstrata FormaGeometrica que herda de ABC (Abstract Base Classes)
2- Crie os dois métodos abstratos area e perímetro
3- Crie um objeto da superclasse abstrata FormaGeometrica, teste
4- Crie a subclasse Quadrado que herda da superclasse abatrata FormaGeometrica
5- Crie o construtor com o atributo lado
6- Crie os métodos get_lado e set_lado
7- Sobreescreva o método abstrato area da superclasse abstrata FormaGeometrica
8- Crie um objeto da subclasse Quadrado, teste
9- Sobreescreva também o método perímetro da superclasse abstrata
10- Crie um objeto da subclasse Quadrado, teste
11- Crie a subclasse Circulo que herda da superclasse abstrata FormaGeometrica
12- Crie o construtor com o atributo lado
- Os métodos get_lado e set_lado
- Sobreescreva o método area
15- Crie um objeto da subclasse Circulo, teste
16- Sobreescreva também o método perímetro
17- Crie um objeto de Circulo, teste
18- Crie um método concreto na superclasse para mostrar uma mensagem, teste
19- Crie mais um método concreto para mostrar uma mensagem na superclasse
    e identifique o objeto da subclasse que chamou o método, teste
20- Refaça o anterrior sem mostrar o endereço hexadecimal, mostre só o nome da classe
21- Refaça a subclasse Circulo usando a constante pi do Python
'''

from abc import ABC, abstractmethod #importar modulo abstract
import math

class FormaGeometrica(ABC): #Classe abstrata, herda da classe ABC
    @abstractmethod #Decorator
    def area(self): #
        ...
    @abstractmethod
    def perimetro(self):
        pass

    def mensagem(self):
        print("Método concreto da superclasse abstrata FormaGeometrica que herda de ABC")

    def mensagem2(self):
        print("Método concreto da superclasse abstrata FormaGeometrica que herda de ABC")
        print("Dados do objeto:", self)

    def mensagem3(self):
        print("Método concreto da superclasse abstrata FormaGeometrica que herda de ABC")
        print("Nome da Classe:", self.__class__.__name__)

class Quadrado(FormaGeometrica): #class NomeSubclasse(NomeSuperclasse): (sintaxe)

    def __init__(self,lado):
        self.lado = lado
    def get_lado(self):
        return self.lado
    def set_lado(self,valor):
        self.lado = valor

    #Método obrigatório, sobrscreve o método abstrato da superclasse abstrata

    def area(self):
        vl_area = self.lado ** 2
        return vl_area
    def perimetro(self):
        vl_perimetro = self.lado * 4
        return vl_perimetro

class Circulo(FormaGeometrica):

    def __init__(self, raio):
        self.raio = raio
    def get_raio(self):
        return self.raio
    def set_raio(self, valor):
        self.raio = valor

    def area(self):
        vl_area = (self.raio * math.pi) **2
        return vl_area
    def perimetro(self):
        vl_perimetro = 2 * 3.14 * self.raio
        return vl_perimetro

if __name__ == '__main__':

    obj_quad = Quadrado(2)
    print("Lado:", obj_quad.get_lado())
    print("Área:", obj_quad.area())
    print("Perímetro:", obj_quad.perimetro())

    obj_quad.set_lado(4)
    print("\nLado:", obj_quad.get_lado())
    print("Área:", obj_quad.area())
    print("Perímetro:", obj_quad.perimetro())

    obj_quad.mensagem()
    obj_quad.mensagem2()
    obj_quad.mensagem3()

    obj_circ = Circulo(2)
    print("\nRaio:", obj_circ.get_raio())
    print(f"Área: {obj_circ.area():.2f}") #(f"texto {resutado :.2f}") ---> para limitar os caracteres
    print(f"Perímetro: {obj_circ.perimetro():.2f}")

    obj_circ.mensagem()
    obj_circ.mensagem2()
    obj_circ.mensagem3()
