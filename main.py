# Arquivo responsável por autenticação:
# - criar conta
# - login
# - validação de usuário

from bank.services import Services
from bank.data import Data

class MenuLogin:
    def __init__(self):
        self.services = Services()
        self.data = Data()


    def starting_database(self):
        self.data.starting_database()
    
    def menu_login(self):
        while True:
            print("""
        Bem vindo ao nosso banco! Oque o senhor deseja fazer?
        \n1 - Criar conta""")
            print("2 - Login")
            print("3 - Sair")

            opcao = input("Escolha: ")

            if opcao == "1":
                self.services.main_method_connect(opcao)

            elif opcao == "2":
                self.services.main_method_connect(opcao)

            elif opcao == "3":
                print("Saindo...")
                break

            else:
                print("Opção inválida.")

class MenuActions:
    def __init__(self):
        pass

    def menu_actions(self):
        pass

menu_to_login = MenuLogin()
menu_to_login.starting_database()
menu_to_login.menu_login()