from bank.data import *
import sqlite3

class Validation:
    def __init__(self):
        
        # CRIANDO OS SELFS PARA RECEBER O USER E PASSWORD DOS INPUTS
        self.conn = sqlite3.connect("bank/database.db")
        self.cursor = self.conn.cursor()



    # CRIAR CONTA LÓGICA
    def create_account(self, username, password):
        try:
            self.cursor.execute(
                "INSERT INTO bank (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("Esse usuário ja existe, não foi possível criar uma conta :( !")



    # LOGIN CONTA LÓGICA

    
    def verify_login(self, username, password):
        self.cursor.execute(
            "SELECT id FROM bank WHERE username = ? AND password = ?",
            (username, password)
        )

        if self.cursor.fetchone() is None:
            print("Usuário ou senha incorretos")
            return False

        print("Login realizado com sucesso")
        return True