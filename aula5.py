'''
Usando o conceito de associação de classes em POO, faça a análise das classes
necessárias para desenvolva um sistema de carrinho de compras com as informações
do pedido, do cliente e dos produtos colocados no carrinho.

Implemente:
1- Crie a classe Cliente com os atributos (características) cpf e nome
- Crie os métodos gets, teste.
- Crie a classe CarrinhoCompra com os atributos número do pedido, o cliente e os produtos.
- Crie os métodos gets, teste
5- Crie a classe Produto com os atributos: identificador, nome, preço e quantidade.
- Crie os métodos gets, teste
- Crie o método __str__ pra retornar todos os dados de um produto formatados (concatenados)
8- Crie o método mostra carrinho, teste
- Insira um produto no carrinho de compras do cliente1. Crie o método insere_produto,
ele recebe um objeto da classe Produto e insere no carrinho.
10- Insira mais um produto no carrinho de compras do cliente1, teste
- Crie o método mostra_carrinho2, com todos os dados do produto e a quantidade de itens
no carrinho. Se o carrinho estiver vazio, mostre a mensagem "Carrinho vazio". Teste

- Crie o método retorna_total, ele calcula e retorna o valor total da compra,
ou seja, dos produtos no carrinho de compras, teste  (valor total 57,00)

13- Crie o método remova_produto, ele remove um produto do carrinho de compras, teste
- Crie o método remova_produto2, ele remove um produto do carrinho de compras
  com críticas e mensagens, teste
15- Insira mais um produto no carrinho de compras do cliente1, teste
- Crie o método fecha_compra. Ele finalize a compra e mostra os produtos e o
  valor total, teste
17- Crie o método remova_produto3, ele não recebe nada, mostre todos os produtos no carrinho,
  o cliente escolhe o produto para remover e remove o produto do carrinho de compras, teste
- Finalize a compra e feche o carrinho 2. Além de mostrar os produtos e o valor total
  Mostrar também o número de pedido, o nome do cliente, a data e hora, teste
  '''

class Cliente():
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def get_cpf(self):
        return self.cpf
    def get_nome(self):
        return self.nome

class CarrinhoCompra():
    def __init__(self, npedido, cliente):
        self.npedido = npedido
        self.cliente = cliente
        self.produtos = list()

    def get_npedido(self):
        return self.npedido
    def get_cliente_nome(self):
        return self.cliente.get_nome()
    def get_produtos(self):
        return self.produtos

    def insere_produto(self, produto_novo):
        self.produtos.append(produto_novo)

    def mostra_carrinho(self):
        qtd = len(self.produtos)
        if not self.produtos:
            print("Carrinho vazio")
        else:
            print("Carrinho:")
            for produto_novo in self.produtos:
                print("Descrição:", produto_novo.nomeproduto)

class Produto(object):
    def __init__(self, identificador, nomeproduto, preco, qtd=1):
        self.identificador = identificador
        self.nomeproduto = nomeproduto
        self.preco = preco
        self.qtd = qtd

    def __str__(self):
        return f'{self.identificador}{self.nomeproduto}{self.preco}{self.qtd}'


if __name__ == '__main__':

    print("-------------------CLIENTE 1-------------------")
    cliente1 = Cliente (12299645147,"João")
    print("\nNome:", cliente1.nome, "\nCPF: ", cliente1.cpf)

    carrinho1 = CarrinhoCompra (1,cliente1)
    print("\nCarrinho1: \nNúmero do Pedido:", carrinho1.get_npedido())
    print("Cliente:", carrinho1.get_cliente_nome())

    p1_arroz = Produto (1, 'Arroz', 30.00)
    print(p1_arroz)

    carrinho1.mostra_carrinho()
    carrinho1.insere_produto(p1_arroz)
    carrinho1.mostra_carrinho()

    print("\n-------------------CLIENTE 2-------------------")
    cliente2 = Cliente(22222222222, "Maria")
    print("\nNome:", cliente2.nome, "\nCPF: ", cliente2.cpf)

    carrinho2 = CarrinhoCompra(2, cliente2)
    print("\nNúmero do Pedido:", carrinho2.get_npedido())
    print("Cliente:", carrinho2.get_cliente_nome())

    p2_feijao = Produto(2, 'Feijão', 20.00)
    print(p2_feijao)

    carrinho2.mostra_carrinho()
    carrinho2.insere_produto(p2_feijao)
    carrinho2.insere_produto(p1_arroz)
    carrinho2.mostra_carrinho()













