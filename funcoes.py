import os
import time
import constantes as c



def LimpaTela():
    os.system('cls')

def Aguarda():
    time.sleep(4)

def AguardaeLimpa():
    Aguarda()
    LimpaTela()

def validaTipoConta(pEhListagem = False):
    tipoConta = 0
    if pEhListagem:
        tipoConta = int(input(c.MSG_OPCOES_TIPOS_CONTAS_LISTAGEM))
    else:
        tipoConta = int(input(c.MSG_OPCOES_TIPOS_CONTAS)) 
    while ( not tipoConta in [1,2,3,4]):
        print(c.MSG_OPCAO_INVALIDA)
        AguardaeLimpa()
        if pEhListagem:
            tipoConta = int(input(c.MSG_OPCOES_TIPOS_CONTAS_LISTAGEM))
        else:
            tipoConta = int(input(c.MSG_OPCOES_TIPOS_CONTAS))
    return tipoConta

def menuOperacoes(pTipoConta, valor = 0): #1 - Corrente | 2 - Salario | 3 - Poupança
    opcao = 1
    AguardaeLimpa()
    print('Operação desejada\n'
        '----------------------\n')
    match pTipoConta:
        case 1:
            opcao = int(input('1 - Sacar      |2 - Depositar\n'
                            '3 - Transferir |4 - Ver Saldo\n'
                            '         5 - Encerrar\n')) 
            while (not opcao in[1,2,3,4,5]):
                print(c.MSG_OPCAO_INVALIDA)
                opcao = int(input('1 - Sacar      |2 - Depositar\n'
                            '3 - Transferir |4 - Ver Saldo\n'
                            '         5 - Encerrar\n'))    
            return opcao
        case 3:
            while (not opcao in[1,2,3,4,5]):
                print(c.MSG_OPCAO_INVALIDA)
                AguardaeLimpa()
                opcao = int(input('1 - Sacar      |2 - Depositar\n'
                            '3 - Transferir |4 - Ver Saldo\n'
                            '         5 - Encerrar\n'))    
            return opcao
        case 2:
            while not(opcao in [1,2]):
                return (c.MSG_OPCAO_INVALIDA)
            return int(input('1- Sacar  |2- Ver Sando\n'
                                '       3 - Encerrar\n'))
        case outrocaso:
            pass

def EhContaValida(pConta):
    if len(pConta) !=c.TAM_VALIDO_CONTA:
        print(c.MSG_NUMERO_CONTA_INVALIDO)
    return len(pConta) ==c.TAM_VALIDO_CONTA

def ExisteConta(pNumero,pConta,pEhCadastro=False):
    if not pEhCadastro:
        if not pNumero in pConta:
            print(c.MSG_CONTA_INEXISTENTE)
    else:
        if pNumero in pConta:
            print(c.MSG_CONTA_EXISTENTE)
    return pNumero in pConta

def ExisteContaCadastrada(pConta,pTipoConta):
    if len(pConta)==0:
        if pTipoConta ==1:
            print(c.MSG_SEM_CONTA_CORRENTE)
        elif pTipoConta ==2:
            print(c.MSG_SEM_CONTA_SALARIO)
        else:
            print(c.MSG_SEM_CONTA_POUPANCA)
    return len(pConta) > 0