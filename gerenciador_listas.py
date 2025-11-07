class Lista:

    listas = []

    def __init__(self, nome, produtos=None):
        self.nome = nome
        self.produtos = produtos if produtos is not None else []
        Lista.listas.append(self)
    
    def adicionar_item(self, produto):
        self.produtos.append(produto)
    
    def remover_item(self, produto):
        try:
            self.produtos.remove(produto)
            print(f'Produto removido com sucesso!')
        except Exception:
            print(f'Produto não encontrado na {self.nome}')
    
    def ver_lista(self):
        print(f'{self.nome} : {self.produtos}')
    
    def procurar_item(self):
        item = input("digite o produto que deseja buscar")
        if item in self.produtos:
            print(f'Produto {item} encontrado na lista {self.nome}')
        else:
            print(f'{item} não encontrado na lista {self.nome}')
    
    @classmethod
    def exibir_listas_cadastradas(cls):
        for lista in Lista.listas:
            print(lista.nome)
    
    @classmethod
    def consultar_lista(cls):
        lista_consulta = input("Digite o nome da lista que deseja consultar")
        lista_encontrada = next((lista for lista in Lista.listas if lista.nome == lista_consulta), None)
        if lista_encontrada:
            lista_encontrada.ver_lista()
        else:
            print("Lista não cadastrada")

    @classmethod
    def encontrar_lista(cls, lista_procurada):
        lista_procurada = next((lista for lista in Lista.listas if lista.nome == lista_procurada), None)
        if lista_procurada:
            return lista_procurada
        


def main ():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            nova_lista = input("Digite o nome da nova lista: ")
            Lista(nova_lista)
            print(f"Lista {nova_lista} cadastrada com sucesso! \n")
        elif escolha == "2":
            Lista.exibir_listas_cadastradas()
        elif escolha == "3":
            Lista.consultar_lista()
        elif escolha == "4":
            lista_escolhida = input("Digite o nome da lista: ")
            lista_encontrada = Lista.encontrar_lista(lista_escolhida)
            if lista_encontrada:
                produto_adicionar = input("Digite o nome do produto que deseja adicionar: ")
                Lista.adicionar_item(lista_encontrada, produto_adicionar)
                print(f"{produto_adicionar} adicionado com sucesso!")
            else:
                print("Lista não cadastrada")
        elif escolha == "5":
            lista_escolhida = input("Digite o nome da lista: ")
            lista_encontrada = Lista.encontrar_lista(lista_escolhida)
            if lista_encontrada:
                produto_remover = input("Digite o nome do produto que deseja remover: ")
                Lista.remover_item(lista_encontrada, produto_remover)
            else:
                print("Lista não cadastrada")
        elif escolha == "6":
            lista_escolhida = input("Digite o nome da lista na qual o prodto se encontra: ")
            lista_encontrada = Lista.encontrar_lista(lista_escolhida)
            if lista_encontrada:
                produto_buscado = input("Digite o nome do produto que deseja buscar: ")
                if produto_buscado in lista_encontrada.produtos:
                    print("Produto encontrado na lista ")
                else: 
                    print("Produto não encontrado na lista ")
            else: 
                print("Lista não cadastrada ")
        elif escolha == "7":
            print("Saindo do programa...")
            break



def exibir_menu():
    print("\n Gerenciador de Listas \n")
    print("1. Cadastrar lista")
    print("2. Consultar listas existentes")
    print("3. Visualizar uma lista")
    print("4. Adicionar produto a uma lista")
    print("5. Remover produto de uma lista")
    print("6. Buscar produto em uma lista")
    print("7. Sair")


if __name__ == "__main__":
    lista1 = Lista("Lista de Compras", ["Arroz", "Feijão", "Carne"])
    lista2 = Lista("Material Escolar", ["Caderno", "Lápis", "Borracha"])
    lista3 = Lista("Tarefas", ["Limpar a casa", "Estudar", "Academia"])
    lista4 = Lista("Filmes para assistir", ["Inception", "Matrix", "Interestelar"])
    lista5 = Lista("Livros para ler", ["1984", "Dom Casmurro", "O Hobbit"])
    main()