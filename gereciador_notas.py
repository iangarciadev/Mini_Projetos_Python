class Aluno:

    alunos = []

    def __init__(self, nome):
        self.nome = nome
        self.notas = []
        Aluno.alunos.append(self)

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            raise ValueError("A nota deve estar entre 0 e 10.")

    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 6:
            return f'Aluno {self.nome} aprovado com média {media:.2f}'
        elif media >= 3:
            return f'Aluno {self.nome} em recuperação com média {media:.2f}'
        else:
            return f'Aluno {self.nome} reprovado com média {media:.2f}'
    
    @classmethod
    def listar_alunos(cls):
        if not cls.alunos:
            print("Nenhum aluno cadastrado.")
            return
        for aluno in Aluno.alunos:
            print(f'Aluno: {aluno.nome}, Notas: {aluno.notas}, Média: {aluno.calcular_media():.2f}, Status: {aluno.verificar_aprovacao()}')  
    
    @classmethod
    def listar_aprovados(cls):
        alunos_aprovados = []
        for aluno in Aluno.alunos:
            if aluno.calcular_media() >= 6:
                alunos_aprovados.append((aluno.nome, aluno.calcular_media()))
        if not alunos_aprovados:
            print("Nenhum aluno aprovado.")
            return
        for nome, media in alunos_aprovados:
            print(f'Aluno: {nome}, Média: {media:.2f}')
    
    @classmethod
    def listar_recuperacao(cls):
        alunos_recuperacao = []
        for aluno in Aluno.alunos:
            if 3 <= aluno.calcular_media() < 6:
                alunos_recuperacao.append((aluno.nome, aluno.calcular_media()))
        if not alunos_recuperacao:
            print("Nenhum aluno em recuperação.")
            return
        for nome, media in alunos_recuperacao:
            print(f'Aluno: {nome}, Média: {media:.2f}')
                
    
    @classmethod
    def listar_reprovados(cls):
        alunos_reprovados = []
        for aluno in Aluno.alunos:
            if aluno.calcular_media() < 3:
                alunos_reprovados.append((aluno.nome, aluno.calcular_media()))
        if not alunos_reprovados:
            print("Nenhum aluno reprovado.")
            return
        for nome, media in alunos_reprovados:
            print(f'Aluno: {nome}, Média: {media:.2f}')

def listar_menu():
    print("Gerenciador de Notas")
    print("1. Cadastrar Aluno")
    print("2. Adicionar Nota a um Aluno")
    print("3. Calcular Média e Verificar Aprovação de um Aluno")
    print("4. Listar Todos os Alunos")
    print("5. Listar Alunos Aprovados")
    print("6. Listar Alunos em Recuperação")
    print("7. Listar Alunos Reprovados")
    print("8. Sair")

def main():
    while True:
        listar_menu()
        escolha = input("Escolha uma opção:")
        if escolha == '1':
            nome_aluno = input("Digite o nome do aluno que deseja cadastrar:")
            novo_aluno = Aluno(nome_aluno)
            print("Aluno cadastrado com sucesso!")
        elif escolha == '2':
            nome_aluno = input("Digite o nome do aluno para adicionar uma nota:")
            aluno_procurado = next((aluno for aluno in Aluno.alunos if aluno.nome == nome_aluno), None)
            if aluno_procurado == None:
                print("Aluno não encontrado. Por favor, cadastre o aluno primeiro.")
                main()
            if aluno_procurado != None:
                try:
                    nota = float(input("Digite a nota a ser adicionada:"))
                    aluno_procurado.adicionar_nota(nota)
                    print("Nota adicionada com sucesso!")
                except ValueError:
                    print("Nota inválida. Digite um número entre 0 e 10.")
        elif escolha == '3':
            nome_aluno = input("Digite o nome do aluno para calcular a média e verificar aprovação:")
            aluno_procurado = next((aluno for aluno in Aluno.alunos if aluno.nome == nome_aluno), None)
            if aluno_procurado == None:
                print("Aluno não encontrado. Por favor, cadastre o aluno primeiro.")
                main()
            if aluno_procurado != None:
                print(aluno_procurado.verificar_aprovacao())
        elif escolha == '4':
            Aluno.listar_alunos()
        elif escolha == '5':
            Aluno.listar_aprovados()
        elif escolha == '6':
            Aluno.listar_recuperacao()
        elif escolha == '7':
            Aluno.listar_reprovados()
        elif escolha == '8':
            print("Saindo do gerenciador de notas.")
            return
        

if __name__ == "__main__":
    main()
