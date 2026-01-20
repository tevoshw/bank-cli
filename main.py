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
        pass

    elif opcao == "2":
        pass

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")