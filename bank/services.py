from bank.validation import Validation

class Services:
    def __init__(self):
        self.validation = Validation()

    def main_method_connect(self, choose):
        self.choose = str(choose)

        match self.choose:
            case "1": # CRIAR CONTA
                self.create_account()
            case "2": # LOGIN
                self.login()
            case "3": # SAIR
                print("Encerrando programa!")


    
    def create_account(self):

        # PEGAR OS DADOS
        username = input("Digite seu usuário: ")
        password = int(input("Digite sua senha: "))
        
        # INSTANCIAR A CLASSE DA LÓGICA DE CRIAR CONTA
        self.validation.create_account_verify_user(username, password)

    def login(self):
        # PEGAR OS DADOS
        username = input("Digite seu usuário: ")
        password = int(input("Digite sua senha: "))

        
        # INSTANCIAR A CLASSE E USAR SUAS FUNÇÕES DA LÓGICA DE LOGIN DA CONTA
        self.validation.verify_login(username, password)


                
    def main_to_do_accountbank(self):
            pass


        

    def deposit(self):
       pass # VER E DEPOSITAR
                
    def withdrawaw(self):
        pass # VER E SACAR

    def view_money(self):
          pass # SÓ VER O DINHEIRO