from bank.data import Data

class Validation:
    def __init__(self):
        
        # CRIANDO OS SELFS PARA RECEBER O USER E PASSWORD DOS INPUTS
        self.validation_user = None
        self.validation_password = None

        # INSTANCIANDO A CLASSE PARA UTILIZAR ELA NAS VERIFICAÇÕES
        self.data = Data()

    # CRIAR CONTA LÓGICA
    def create_account_verify_user(self, username, password):
        self.validation_user = username
        self.validation_password = password

        # COMPARA SE JA EXISTE UM USUÁRIO E SE EXISTE, NEGA ACESSO
        if self.validation_user in self.data.data_username:
            print("Impossível criar um usuário com esse nome, pois já é existente!")
        else:
            # VERIFICA SE O USER É MAIOR QUE 4 CARACTERES
            if len(self.validation_user) < 4:
                print("Username pequeno demais, tente novamente!")
            else:
                self.create_account_verify_password()

    def create_account_verify_password(self):
        # ADICIONAR LÓGICA DE PASSWORD MAIOR QUE 8 LETRAS, TER NÚMEROS E LETRAS
        if len(str(self.validation_password)) < 8:
            print("Senha curta demais")
        else:
            self.data.data_username.append(self.validation_user)
            self.data.data_password.append(self.validation_password)
            print("Conta criada com sucesso!")





    # LOGIN CONTA LÓGICA

    
    def verify_login(self, username, password):
        self.validation_user = username
        self.validation_password = password


        if self.validation_user in self.data.data_username:
            print("Usuário encontrado, verificando senha...")
            index_user = self.data.data_username.index(self.validation_user)
            if self.validation_password == self.data.data_password[index_user]:
                print("Login Autenticado!") # REDIRECIONAR PARA A A INTERFACE
            else:
                print("Senha incorreta! Tente novamente")

        else:
            print("Usuário não encontrado")


# teste = Validation('tevoo', 123)
#teste.create_account_verify_user()
        