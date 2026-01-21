from bank.validation import Validation

class Services:
    def __init__(self, user_index):
        self.data = Validation.data
        self.index = user_index

    def deposit(self, value):
        self.data.data_balance[self.index] += value
        self.data.data_history[self.index].append(f"Depósito: +{value}")
        print("Depósito realizado.")

    def withdraw(self, value):
        if value > self.data.data_balance[self.index]:
            print("Saldo insuficiente.")
            return

        self.data.data_balance[self.index] -= value
        self.data.data_history[self.index].append(f"Saque: -{value}")
        print("Saque realizado.")

    def balance(self):
        print(f"Saldo atual: {self.data.data_balance[self.index]}")

    def history(self):
        print("Histórico:")
        for h in self.data.data_history[self.index]:
            print("-", h)