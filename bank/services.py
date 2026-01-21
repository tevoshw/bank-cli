from bank.validation import Validation
import sqlite3

class Services:
    def __init__(self):
        self.validation = Validation()
        self.conn = sqlite3.connect("bank/database.db")
        self.cursor = self.conn.cursor()


# ------------------------------------------------------- ! ------------------------------------------
# ---------------------------- ANALISAR ESCOLHA DO USUARIO --------------------------------------
    def main_method_connect(self, choose):

        # VERIFICA QUAL OPÇÃO O USUÁRIO ESCOLHEU E REDIRECIONA PARA A FUNÇÃO JÁ
        self.choose = str(choose)

        match self.choose:
            case "1": # CRIAR CONTA
                self.create_account()

            case "2": # LOGIN
                if_login = self.login()
                if if_login == True:
                    return True

            case "3": # SAIR
                print("Encerrando programa!")

# --------------------------------------------------- ! ----------------------------------------------------
# ----------------------------- LOGIN LÓGICA -----------------------------------------------

    # OBTER OS DADOS DA CONTA E CRIAR ELA, REDIRECIONA PARA A PAGINA DE VALIDAR O USER E PASSWORD
    def create_account(self):

        # PEGAR OS DADOS
        self.username = input("Digite seu usuário: ")
        password = int(input("Digite sua senha: "))
        
        # INSTANCIAR A CLASSE DA LÓGICA DE CRIAR CONTA
        self.validation.create_account(self.username, password)



    def login(self):

        # PEGAR OS DADOS
        self.username = input("Digite seu usuário: ")
        password = int(input("Digite sua senha: "))

        # INSTANCIAR A CLASSE E USAR SUAS FUNÇÕES DA LÓGICA DE LOGIN DA CONTA
        if_login = self.validation.verify_login(self.username, password)
        if if_login == True:
            return True
