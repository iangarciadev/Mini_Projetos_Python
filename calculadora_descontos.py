def calcular_desconto():
    try:
        porcentagem = int(input("Digite a porcentagem do desconto:"))
    except ValueError: 
        print("Digite um valor numérico entre 1 e 100")
        return
    
    if porcentagem < 0 or porcentagem > 100:
        print("Porcentagem deve estar entre 0 e 100")
        return
    
    try:
        valor_produto = int(input("Digite o valor original do produto:"))
    except ValueError:
        print("Digite um valor numérico")
        return
    
    valor_final = valor_produto - valor_produto * (porcentagem / 100)

    print(f'O valor final do produto é R$ {valor_final:.2f}.')


if __name__ == "__main__":
    while True:
        print("Calculadora de descontos")
        calcular_desconto()