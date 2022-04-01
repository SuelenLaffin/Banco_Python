import constantes as c

class Conta():
    def __init__(self,conta):
        self.conta = conta
        self.saldo = 0
    
    def verSaldo(self):
        return f'Saldo atual: {self.saldo:,.2f}'

    def sacar(self,valor, EhCorrente = False):
        try:
            if EhCorrente:
                if valor +(valor * 0.05 ) >self.saldo:
                    return c.MSG_SALDO_INSUFICIENTE
                self.saldo -=valor
            else:
                if valor > self.saldo:
                    return c.MSG_SALDO_INSUFICIENTE
                self.saldo -= valor
            return c.MSG_SUCESSO_SAQUE
        except: 
            return c.MSG_ERRO_SAQUE

    
        
        
    