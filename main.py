from bank.validation import Validation
from bank.services import Services

while True:
    print("""
1 - Criar conta
2 - Login
3 - Sair
""")

    op = input("Escolha: ")

    if op == "1":
        user = input("Usuário: ")
        password = input("Senha: ")

        v = Validation(user, password)
        v.create_account()

    elif op == "2":
        user = input("Usuário: ")
        password = input("Senha: ")

        v = Validation(user, password)
        index = v.login()

        if index is not None:
            s = Services(index)

            while True:
                print("""
1 - Depositar
2 - Sacar
3 - Ver saldo
4 - Ver histórico
5 - Sair
""")

                choice = input("Escolha: ")

                if choice == "1":
                    s.deposit(float(input("Valor: ")))
                elif choice == "2":
                    s.withdraw(float(input("Valor: ")))
                elif choice == "3":
                    s.balance()
                elif choice == "4":
                    s.history()
                elif choice == "5":
                    break
                else:
                    print("Opção inválida.")

    elif op == "3":
        break