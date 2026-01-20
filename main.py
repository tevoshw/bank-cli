# Arquivo responsável por autenticação:
# - criar conta
# - login
# - validação de usuário

usuarios = {}

while True:
    print("""
Bem vindo ao nosso banco! Oque o senhor deseja fazer?
\n1 - Criar conta""")
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
            # Pegue o valor que está guardado dentro de usuarios usando a chave user
            # Guarde a senha dentro do dicionário usando o nome do usuário como chave
            print("Conta criada.")

    elif opcao == "2":
        user = input("Usuário: ")
        senha = input("Senha: ")
        if user in usuarios and usuarios[user] == senha:
            #Se o usuário existe E a senha está correta
            print("Login realizado.")
        else:
            print("Usuário ou senha incorretos.")

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")