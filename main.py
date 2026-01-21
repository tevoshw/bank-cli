# Arquivo responsável por autenticação:
# - criar conta
# - login
# - validação de usuário

import os
from bank.services import Services
from bank.data import Data

class MenuLogin:
    def __init__(self):
        self.services = Services()
        self.data = Data()


    def starting_database(self):
        self.data.starting_database()
    
    def menu_login(self):
            print("""
        Bem vindo ao nosso banco! Oque o senhor deseja fazer?
        \n1 - Criar conta""")
            print("2 - Login")
            print("3 - Sair")

            opcao = input("Escolha: ")
            os.system('cls' if os.name == 'nt' else 'clear')


            if opcao == "1":
                self.services.main_method_connect(opcao)

            elif opcao == "2":
                self.services.main_method_connect(opcao)
                

            elif opcao == "3":
                print("Saindo...")

            else:
                print("Opção inválida.")

class MenuActions:
    def __init__(self):
        self.services = Services()


    def menu_actions(self):
        print("""
        Bem vindo ! Oque o senhor deseja fazer?
        \n1 - Deposito""")
        print("2 - Saque")
        print("3 - Ver saldo")
        print("4 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            self.services.deposit()
                
        elif opcao == "2":
            self.services.withdrawaw
                
        elif opcao == "3":
            self.services.view_balance

        elif opcao == "4":
            print("Saindo...")
            

        else:
            print("Opção inválida.")

menu_to_login = MenuLogin()
menu_to_login.starting_database()
menu_to_login.menu_login()