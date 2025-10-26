def validar_valores(valor):
    if valor <= 0:
        return False
    return True

def validar_porcentagem(porcentagem):
    if porcentagem <= 0 or porcentagem > 100:
        return False
    return True

def validar_emprestimo(valor_parcela, renda_mensal, porcentagem_maxima):
    if validar_valores(renda_mensal) is False or validar_valores(renda_mensal) is False:
        return 'Renda mensal e valor da parcela devem ser maiores do que zero'
    if validar_porcentagem(porcentagem_maxima) is False:
        return 'Porcentagem máxima deve estar entre 0 e 100'
    if valor_parcela > (renda_mensal * (porcentagem_maxima / 100)):
        return 'Empréstimo não aprovado: parcela excede a porcentagem máxima da renda mensal'
    return 'Empréstimo aprovado!'

def calcular_emprestimo_maximo(renda_mensal, porcentagem_maxima):
    if validar_valores(renda_mensal) is False:
        return 'Renda mensal deve ser maior do que zero'
    if validar_porcentagem(porcentagem_maxima) is False:
        return 'Porcentagem máxima deve estar entre 0 e 100'
    valor_maximo = renda_mensal * (porcentagem_maxima / 100)
    return f'Valor máximo do empréstimo aprovado: R$ {valor_maximo:.2f}'

def exibir_menu():
    print('Validador de Empréstimos')
    print('1. Validar Empréstimo')
    print('2. Calcular Empréstimo Máximo')
    print('3. Sair')

def main():
    while True:
        exibir_menu()
        input_opcao = input('Escolha uma opção: ')
        if input_opcao == '1':
            try:
                valor_parcela = float(input('Digite o valor da parcela do empréstimo: '))
                renda_mensal = float(input('Digite a sua renda mensal: '))
                porcentagem_maxima = float(input('Digite a porcentagem máxima da renda mensal dedicada ao empréstimo: '))
            except ValueError:
                print('Entrada inválida. Por favor, insira somente números.')
                return
            resultado = validar_emprestimo(valor_parcela, renda_mensal, porcentagem_maxima)
            print(resultado)
        elif input_opcao == '2':
            try:
                renda_mensal = float(input('Digite a sua renda mensal: '))
                porcentagem_maxima = float(input('Digite a porcentagem máxima da renda mensal dedicada ao empréstimo: '))
            except ValueError:
                print('Entrada inválida. Por favor, insira somente números.')
                return
            resultado = calcular_emprestimo_maximo(renda_mensal, porcentagem_maxima)
            print(resultado)
        elif input_opcao == '3':
            print('Saindo do validador de empréstimos.')
            return
        else:
            print('Opção inválida. Insira um número de 1-3.')

if __name__ == '__main__':
    main()