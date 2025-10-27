class Livro:
    livros = []

    def __init__(self, titulo, estoque):
        self.titulo = titulo
        self.estoque = estoque
        Livro.livros.append(self)

    @classmethod
    def adicionar_livro(cls):
        novo_livro = input("Digite o título do livro que deseja adicionar: ")
        try:
            quantidade_estoque = int(input("Digite a quantidade em estoque: "))
        except ValueError:
            print("Quantidade inválida. Por favor, insira um número inteiro maior ou igual a zero.")
            return
        livro = Livro(novo_livro, quantidade_estoque)
        print(f'Livro "{livro.titulo}" adicionado com {livro.estoque} unidades em estoque.')

    @classmethod
    def listar_livros(cls):
        if not cls.livros:
            print("Nenhum livro cadastrado.")
            return
        for livro in cls.livros:
            print(f'{livro.titulo} possui {livro.estoque} unidades em estoque.')
    
    @classmethod
    def atualizar_estoque(cls):
        livro_atualizar = input("Digite o título do livro que deseja atualizar o estoque: ")
        try:
            nova_quantidade = int(input("Digite a nova quantidade em estoque: "))
        except ValueError:
            print("Quantidade inválida. Por favor, insira um número inteiro maior ou igual a zero.")
            return
        for livro in cls.livros:
            if livro.titulo == livro_atualizar:
                livro.estoque = nova_quantidade
                print(f'Estoque do livro "{livro.titulo}" atualizado para {livro.estoque}.')
                return
        print(f'Livro "{livro_atualizar}" não encontrado.')
    
    @classmethod
    def emprestar_livro(cls):
        livro_emprestar = input("Digite o título do livro que deseja emprestar: ")
        for livro in cls.livros:
            if livro.titulo == livro_emprestar:
                break
        if livro.estoque > 0:
            livro.estoque -= 1
            print(f'Empréstimo realizado com sucesso. Estoque restante do livro "{livro.titulo}": {livro.estoque}.')
        else:
            print(f'Não há estoque disponível para o livro "{livro_emprestar}".')
    
    @classmethod
    def devolver_livro(cls):
        livro_devolver = input("Digite o título do livro que deseja devolver: ")
        try:
            for livro in cls.livros:
                if livro.titulo == livro_devolver:
                    break
            livro.estoque += 1
            print(f'Devevolução realizada com sucesso. Estoque atualizado do livro "{livro.titulo}": {livro.estoque}.')
        except ValueError:
            print(f'Livro "{livro_devolver}" não encontrado.')

def exibir_menu():
    print("\nGerenciador de Biblioteca")
    print("1. Adicionar Livro")
    print("2. Listar Livros")
    print("3. Atualizar Estoque")
    print("4. Emprestar Livro")
    print("5. Devolver Livro")
    print("6. Sair")

def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            Livro.adicionar_livro()
        elif escolha == '2':
            Livro.listar_livros()
        elif escolha == '3':
            Livro.atualizar_estoque()
        elif escolha == '4':
            Livro.emprestar_livro()
        elif escolha == '5':
            Livro.devolver_livro()
        elif escolha == '6':
            print("Saindo do gerenciador de biblioteca.")
            break
        else:
            print("Opção inválida. Tente novamente.")
    
    
if __name__ == "__main__":
    main()