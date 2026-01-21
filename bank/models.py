class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    

class BankAccount:
    def __init__(self, user, account_id):
        self.user = user
        self.balance = 0.0
        self.account_id = account_id
