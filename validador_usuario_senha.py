def validar_usuario():
    usuario = input("Digite o nome de usuário: ")

    if len(usuario) < 5:
        print("O nome de usuário deve ter pelo menos 5 caracteres.")
        return False
    if usuario.isspace() or ' ' in usuario:
        print("O nome de usuário não deve conter espaços em branco.")
        return False
    

def validar_senha():
    senha = input("Digite a senha: ")
    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        return False

    if senha.isspace() or ' ' in senha:
        print("A senha não deve conter espaços em branco.")
        return False

    for char in senha:
        if char.isdigit():
            break
    else:
        print("A senha deve conter pelo menos um número.")
        return False

    for char in senha:
        if char.isupper():
            break
    else:
        print("A senha deve conter pelo menos uma letra maiúscula.")
        return False

    for char in senha:
        if char in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '_', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '/', '?', '|', '~', '`']:
            break
    else:
        print("A senha deve conter pelo menos um caractere especial")
        return False

    print("Nome de usuário e senha válidos!")
    return True

def main():
    if validar_usuario() is not False:
        while validar_senha() is False:
            validar_senha()
    else: 
        main()

if __name__ == "__main__":
    main()


