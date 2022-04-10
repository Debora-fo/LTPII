'''
Usando o conceito de associação de classes em POO, faça a análise das classes
necessárias para desenvolva um sistema de carrinho de compras com as informações
do pedido, do cliente e dos produtos colocados no carrinho.
Implemente:
1- Crie a classe Cliente com os atributos (características) cpf e nome
2- Crie os métodos gets, teste.
3- Crie a classe CarrinhoCompra com os atributos número do pedido, o cliente e os produtos.
4- Crie os métodos gets, teste
5- Crie a classe Produto com os atributos: identificador, nome, preço e quantidade.
5- Crie os métodos gets, teste
6- Crie o método __str__ pra retornar todos os dados de um produto formatados (concatenados)
8- Crie o método mostra carrinho, teste
9- Insira um produto no carrinho de compras do cliente1. Crie o método insere_produto,
ele recebe um objeto da classe Produto e insere no carrinho.
10- Insira mais um produto no carrinho de compras do cliente1, teste
11- Crie o método mostra_carrinho2, com todos os dados do produto e a quantidade de itens
no carrinho. Se o carrinho estiver vazio, mostre a mensagem "Carrinho vazio". Teste
12- Crie o método retorna_total, ele calcula e retorna o valor total da compra,
ou seja, dos produtos no carrinho de compras, teste  (valor total 57,00)
13- Crie o método remova_produto, ele remove um produto do carrinho de compras, teste
14- Crie o método remova_produto2, ele remove um produto do carrinho de compras
  com críticas e mensagens, teste
15- Insira mais um produto no carrinho de compras do cliente1, teste
16- Crie o método fecha_compra. Ele finalize a compra e mostra os produtos e o valor total, teste
17- Crie o método remova_produto3, ele não recebe nada, mostre todos os produtos no carrinho,
  o cliente escolhe o produto para remover e remove o produto do carrinho de compras, teste

18- Finalize a compra e feche o carrinho 2. Além de mostrar os produtos e o valor total
  Mostrar também o número de pedido, o nome do cliente, a data e hora, teste
  '''


#1- Crie a classe Cliente com os atributos (características) cpf e nome

from datetime import datetime

class Cliente():
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

# 2- Crie os métodos gets, teste.

    def get_cpf(self):
        return self.cpf
    def get_nome(self):
        return self.nome

#5- Crie a classe Produto com os atributos: identificador, nome, preço e quantidade.

class Produto():

    def __init__(self, identificador, nomeproduto, preco: int, qtd=1):
        self.identificador = identificador
        self.nomeproduto = nomeproduto
        self.preco = preco
        self.qtd = qtd

#5- Crie os métodos gets, teste
#6- Crie o método __str__ pra retornar todos os dados de um produto formatados (concatenados)
    def __str__(self):
        return f'{self.identificador}{self.nomeproduto}{self.preco}{self.qtd}'

#3- Crie a classe CarrinhoCompra com os atributos número do pedido, o cliente e os produtos.
class CarrinhoCompra():

    def __init__(self, npedido, cliente):
        self.npedido = npedido
        self.cliente = cliente
        self.produtos = list()

# 4- Crie os métodos gets, teste

    def get_npedido(self):
        return self.npedido
    def get_cliente_nome(self):
        return self.cliente.get_nome()
    def get_produtos(self):
        return self.produtos

#9- Crie o método insere_produto, ele recebe um objeto da classe Produto e insere no carrinho.

    def insere_produto(self, produto_novo):
        self.produtos.append(produto_novo)

#8- Crie o método mostra carrinho, teste
#11- Crie o método mostra_carrinho2, com todos os dados do produto e a quantidade de itens no carrinho.
# Se o carrinho estiver vazio, mostre a mensagem "Carrinho vazio". Teste

    def mostra_carrinho(self):
        if not self.produtos:
            print("Carrinho vazio")
        else:
            print("Quantidade de produtos no carrinho:", len(self.produtos))
            print("Produtos dentro do carrinho:")
            for produto_novo in self.produtos:
                print("-", produto_novo.nomeproduto)


#12- Crie o método retorna_total, ele calcula e retorna o valor total da compra,ou seja, dos produtos no carrinho de compras, teste  (valor total 57,00)

    def retorna_total(self):
        valor = 0
        for produto in self.produtos:
            valor = valor + (produto.preco * produto.qtd)
        print("\nValor total da compra:", valor)
        print("\n")

        return valor

#13- Crie o método remova_produto, ele remove um produto do carrinho de compras, teste
#14- Crie o método remova_produto2, ele remove um produto do carrinho de compras com críticas e mensagens, teste
#17- Crie o método remova_produto3, ele não recebe nada, mostre todos os produtos no carrinho,
# o cliente escolhe o produto para remover e remove o produto do carrinho de compras, teste

    def remova_produto(self):
        cont = 0
        if not self.produtos:
            print("Carrinho vazio")
        else:
            print("Produtos no carrinho:")
            for produto_novo in self.produtos:
                print(cont,"-", produto_novo.nomeproduto)
                cont = cont + 1
        retirar = input('\nDigite o número do produto que deseja remover:\n')
        if len(self.produtos) > int(retirar) >= 0:
            self.produtos.pop(int(retirar))
            self.mostra_carrinho()
        else:
            print("Produto não encontrado")

#16- Crie o método fecha_compra. Ele finalize a compra e mostra os produtos e o valor total, teste
#18- Finalize a compra e feche o carrinho 2. Além de mostrar os produtos e o valor total
#Mostrar também o número de pedido, o nome do cliente, a data e hora, teste

    def fecha_compra(self):
        print("\nCompra finalizada.")
        print("Cliente:", self.cliente)
        data = datetime.now()
        print("Data:",data.day,"/",data.month,"/",data.year)
        print("Horário:",data.hour,":",data.minute)
        self.mostra_carrinho()
        self.retorna_total()


if __name__ == '__main__':

    print("-------------------CLIENTE 1-------------------")

    cliente1 = Cliente (12299645147,"João")
    print("Nome:", cliente1.nome, "\nCPF: ", cliente1.cpf)

    print("------------------CARRINHO 1------------------")

    carrinho1 = CarrinhoCompra (1,cliente1)
    print("Número do Pedido:", carrinho1.get_npedido())
    print("Cliente:", carrinho1.get_cliente_nome())
    print("\n")

#9- Insira um produto no carrinho de compras do cliente1.

    p1 = Produto(1, 'Arroz', 30, 2)

#10- Insira mais um produto no carrinho de compras do cliente1, teste

    p2 = Produto(2,"Macarrão", 14, 2)

#15- Insira mais um produto no carrinho de compras do cliente1, teste

    p3 = Produto(3,"Ovo de Páscoa", 70, 5)

    carrinho1.insere_produto(p1)
    carrinho1.insere_produto(p2)
    carrinho1.insere_produto(p3)
    carrinho1.mostra_carrinho()
    carrinho1.retorna_total()
    carrinho1.remova_produto()
    carrinho1.fecha_compra()

    print("\n------------------CLIENTE 2-------------------")
    cliente2 = Cliente(22222222222, "Maria")
    print("Nome:", cliente2.nome, "\nCPF: ", cliente2.cpf)

    print("------------------CARRINHO 2------------------")
    carrinho2 = CarrinhoCompra(2, cliente2)
    print("Número do Pedido:", carrinho2.get_npedido())
    print("Cliente:", carrinho2.get_cliente_nome())

    p3 = Produto(3, 'Feijão', 20,5)

    carrinho2.insere_produto(p3)
    carrinho2.insere_produto(p1)
    carrinho2.insere_produto(p3)
    carrinho2.mostra_carrinho()
    carrinho2.retorna_total()
    carrinho1.fecha_compra()
