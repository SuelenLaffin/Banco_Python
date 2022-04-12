from ClasseConta import Conta
import constantes as c

class ContaPoupanca(Conta):
    def transferir(self, valor):
        try:
            if valor > self.saldo:
                return c.MSG_SALDO_INSUFICIENTE
            self.saldo -= valor
            return c.MSG_SUCESSO_TRANSFERENCIA
        except:
            return c.MSG_ERRO_TRANSFERENCIA

    def depositar(self, valor):
        try:
            self.saldo += valor
            return c.MSG_SUCESSO_DEPOSITO
        except:
            return c.MSG_ERRO_DEPOSITO