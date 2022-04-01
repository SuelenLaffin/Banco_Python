import os
import time



def LimpaTela():
    os.system('cls')

def Aguarda():
    time.sleep(4)

def AguardaeLimpa():
    Aguarda()
    LimpaTela()

def validaTipoConta():
    tipoConta = 0
    tipoConta = int(input('Informe o tipo da conta desejada: \n'
                                  '1- Conta Corrente\n' + 
                                  '2- Conta Salário\n' 
                                  '3- Conta Poupança\n'
                                  '4- Todas'))
    while ( not tipoConta in [1,2,3,4]):
        print('Opção inválida!')
        AguardaeLimpa()
        tipoConta = int(input('Informe o tipo da conta desejada: \n'
                            '1- Conta Corrente\n' + 
                            '2- Conta Salário\n' 
                            '3- Conta Poupança\n'
                            '4- Todas'))
    return tipoConta

def menuOperacoes(pTipoConta, valor = 0): #1 - Corrente | 2 - Salario | 3 - Poupança
    opcao = 0
    AguardaeLimpa()
    print('Operação desejada\n'
        '----------------------\n')
    match pTipoConta:
        case 1,3:
            while (not opcao in[1,2,3,4,5]):
                print('Opção inválida!')
            return  int(input('1 - Sacar      |2 - Depositar\n'
                             '3 - Transferir |4 - Ver Saldo\n'
                             '         5 - Voltar'))    
        case 2:
            while not(opcao in [1,2]):
                print('Opção inválida!')
            return int(input('1- Sacar  |2- Ver Sando\n'
                                  '       3 - Voltar'))
        case outrocaso:
            pass