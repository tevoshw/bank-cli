usuarios = {}

while True:
    print("\n1 - Criar conta")
    print("2 - Login")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        user = input("Usuário: ")
        if user in usuarios:
            print("Usuário já existe.")
        else:
            senha = input("Senha: ")
            usuarios[user] = senha
            print("Conta criada.")

    elif opcao == "2":
        user = input("Usuário: ")
        senha = input("Senha: ")
        if user in usuarios and usuarios[user] == senha:
            print("Login realizado.")
        else:
            print("Usuário ou senha incorretos.")

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")