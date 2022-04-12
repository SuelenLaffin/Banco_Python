import mysql.connector

class Conexao ():
    def __init__(self, host, banco,usuario,senha):
        self.host = host
        self.banco = banco
        self.usuario = usuario
        self.senha = senha