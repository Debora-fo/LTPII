from abc import ABC,abstractmethod

class Carro(ABC):
    def __init__(self, modelo, preco):
        self.modelo = modelo
        self.preco = preco

    def get_modelo(self):
        return self.modelo
    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_preco(self):
        return self.preco
    def set_preco(self):
        self.preco = preco

    @abstractmethod
    def preco_diaria(self):
        ...

class Economico(Carro):

    def get_modelo(self):
        return self.modelo
    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_preco(self):
        return self.preco
    def set_preco(self):
        self.preco = preco

    def preco_diaria(self):
        self.diaria = self.preco + (self.preco * 0.05)
        return self.diaria


if __name__ == '__main__':

    carro1 = Economico("Megane",300.000)
    print("Modelo:",carro1.modelo)
    print("Preço:", carro1.preco)
    print("Diária", carro1.preco_diaria() )

    carro2 = Economico("Gol", 89.000 )
    print("Modelo:",carro2.modelo)
    print("Preço:", carro2.preco)
    print("Diária", carro2.preco_diaria())





