class Produto:
    produtos = []

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        Produto.produtos.append(self)
    
    @property
    def valor_total(self):
        return f' O valor total vendido do produto {self.nome} é: R$ {self.preco * self.quantidade:.2f}'
    
    @classmethod
    def comparar_vendas(cls):
        valores_produtos = []
        for produto in cls.produtos:
            valores_produtos.append((produto.nome, produto.preco * produto.quantidade))
        valores_produtos.sort(key=lambda x: x[1], reverse=True)
        for nome, valor in valores_produtos:
            print(f'Produto: {nome}, Valor Total Vendido: R$ {valor:.2f}')

def main():
    while True:
        escolha = exibir_menu()
        if escolha == '1':
            produto_nome = input("Digite o nome do produto que deseja cadastrar:")
            try:
                preco = float(input("Digite o preço do produto:"))
            except ValueError:
                print("Preço inválido. Digite um número.")
                continue
            try:
                quantidade = int(input("Digite a quantidade vendida do produto:"))
            except ValueError:
                print("Quantidade inválida. Digite um número inteiro.")
                continue
            novo_produto = Produto(produto_nome, preco, quantidade)
            print("Produto cadastrado com sucesso!")
        elif escolha == '2':
            produto_nome = input("Digite o nome do produto que deseja consultar:")
            try:
                print(novo_produto.valor_total)
            except NameError:
                print("Nenhum produto cadastrado. Por favor, cadastre um produto primeiro.")
        elif escolha == '3':
                Produto.comparar_vendas()
        elif escolha == '4':
            print("Saindo do gerenciador de vendas.")
            return
        elif escolha:
            print("Opção inválida. Tente novamente.")
    

def exibir_menu():
    print("Gerenciador de Vendas")
    print("1. Cadastrar Produto")
    print("2. Consultar Valor Total Vendido de um Produto")
    print("3. Comparar Vendas entre Produtos")
    print("4. Sair")
    escolha = input("Escolha uma opção: ")
    return escolha


if __name__ == "__main__":
    main()