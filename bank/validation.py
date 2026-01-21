from bank.data import Data

from bank.data import Data

class Validation:
    data = Data()  # compartilhado entre todos

    def __init__(self, username, password):
        self.validation_user = username
        self.validation_password = password

    def create_account(self):
        if self.validation_user in self.data.data_username:
            print("Usuário já existe.")
            return False

        if len(self.validation_user) < 4:
            print("Usuário pequeno demais.")
            return False

        if len(self.validation_password) < 8:
            print("Senha curta demais.")
            return False

        self.data.data_username.append(self.validation_user)
        self.data.data_password.append(self.validation_password)
        self.data.data_balance.append(0)
        self.data.data_history.append([])

        print("Conta criada com sucesso.")
        return True

    def login(self):
        if self.validation_user not in self.data.data_username:
            print("Usuário não encontrado.")
            return None

        index = self.data.data_username.index(self.validation_user)

        if self.validation_password != self.data.data_password[index]:
            print("Senha incorreta.")
            return None

        print("Login realizado.")
        return index

# teste = Validation('tevoo', 123)
#teste.create_account_verify_user()
        