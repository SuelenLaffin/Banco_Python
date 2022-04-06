from ClasseContaCorrente import ContaCorrente
from ClasseContaPoupanca import ContaPoupanca
from ClasseContaSalario import ContaSalario
import funcoes as f
import constantes as cons

contasC = {} #Conta Corrente
contasS = {} #Conta Salário
contasP = {} #Conta Poupança

op = 0
tipoConta = 0
valor = 0

f.LimpaTela()
while op != 5:
    print('Banco Proway\n'
        '1- Criar Conta\n'
        '2- Listar Contas\n'
        '3- Excluir Conta\n'
        '4- Operações\n'
        '5- Sair\n')
    op = int(input('Informe a opção desejada: '))
    f.LimpaTela()
    match op:
        case 1:            
            tipoConta = f.validaTipoConta(True)
            f.LimpaTela()
            numero = input(cons.MSG_CONTA_PARA_CADASTRAR)
            if (not(f.EhContaValida(numero))):
                f.AguardaeLimpa()
            else:
                match tipoConta:
                    case 1:                    
                        if (not (f.ExisteConta(numero,contasC, True))):
                            c = ContaCorrente(numero)
                            contasC[c.conta] = 0
                            print(cons.MSG_SUCESSO_CADASTRAR)
                            del(c)
                    case 2:
                        if (not (f.ExisteConta(numero,contasS, True))):
                            c = ContaSalario(numero)
                            contasS[c.conta] = 0
                            print(cons.MSG_SUCESSO_CADASTRAR)
                            del(c)
                    case outrocaso:
                        if (not (f.ExisteConta(numero,contasP, True))):
                            c = ContaPoupanca(numero)
                            contasP[c.conta] = 0
                            print(cons.MSG_SUCESSO_CADASTRAR)
                            del(c)
            f.AguardaeLimpa()
        case 2:
            tipoConta = f.validaTipoConta()
            f.LimpaTela()
            match tipoConta:
                case 1:
                    if (f.ExisteContaCadastrada(contasC, tipoConta)):
                        print(contasC)
                case 2:
                    if (f.ExisteContaCadastrada(contasS, tipoConta)):
                        print(contasS)
                case 3:
                    if (f.ExisteContaCadastrada(contasP, tipoConta)):
                        print(contasP)
                case outrocaso:
                    print('Conta Corrente')
                    print(contasC)
                    print('Conta Salário')
                    print(contasS)
                    print('Conta Poupança')
                    print(contasP)
            f.AguardaeLimpa() 
        case 3:
            tipoConta = f.validaTipoConta()
            f.LimpaTela()
            match tipoConta:
                case 1:
                    if f.ExisteContaCadastrada(contasC,tipoConta):
                        numero = input(cons.MSG_CONTA_PARA_EXCLUIR)
                        if f.EhContaValida(numero):
                            if f.ExisteConta(numero,contasC):
                                c = ContaCorrente(numero)
                                contasC.pop(c.conta)
                                print(cons.MSG_SUCESSO_EXCLUIR)
                                del(c)
                case 2:
                    if f.ExisteContaCadastrada(contasS,tipoConta):
                        numero = input(cons.MSG_CONTA_PARA_EXCLUIR)
                        if f.EhContaValida(numero):
                            if f.ExisteConta(numero,contasS):
                                c = ContaSalario(numero)
                                contasS.pop(c.conta)
                                print(cons.MSG_SUCESSO_EXCLUIR)
                                del(c)
                case outrocaso:
                    if f.ExisteContaCadastrada(contasP,tipoConta):
                        numero = input(cons.MSG_CONTA_PARA_EXCLUIR)
                        if f.EhContaValida(numero):
                            if f.ExisteConta(numero,contasP):
                                c = ContaPoupanca(numero)
                                contasP.pop(c.conta)
                                print(cons.MSG_SUCESSO_EXCLUIR)
                                del(c)
            f.AguardaeLimpa()
        case 4:
            tipoConta = f.validaTipoConta()
            f.LimpaTela
            match tipoConta:
                case 1: #Conta Corrente 
                    op = f.menuOperacoes(tipoConta)
                    match op:
                        case 1: #Sacar 
                            valor = int(input(cons.MSG_VALOR_SAQUE))
                        case 2:
                            valor = int(input(cons.MSG_VALOR_DEPOSITO))
                        case 3:
                            valor = int(input(cons.MSG_VALOR_TRANSFERENCIA))
                        case 4:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.EhContaValida(numero):
                                if f.ExisteConta(numero,contasC):
                                    print(contasC[numero])
                        case outrocaso:
                            break
                        
                case 2: #Conta Salário
                    op = f.menuOperacoes(tipoConta)
                    match op:
                        case 1:
                            pass
                        case 2:
                            numero =input(cons.MSG_NUMERO_CONTA)
                            if f.EhContaValida(numero):
                                if f.ExisteConta(numero,contasS):
                                    print(contasS[numero])
                        case outrocaso:
                            pass
                case outrocaso: #Conta Poupança
                            op = f.menuOperacoes(tipoConta)
                            match op:
                                case 1: #Sacar 
                                    valor = int(input(cons.MSG_VALOR_SAQUE))
                                case 2:
                                    valor = int(input(cons.MSG_VALOR_DEPOSITO))
                                case 3:
                                    valor = int(input(cons.MSG_VALOR_TRANSFERENCIA))
                                case 4:
                                    numero = input(cons.MSG_NUMERO_CONTA)
                                    if f.EhContaValida(numero):
                                        if f.ExisteConta(numero,contasP):
                                            print(contasP[numero])
                                case outrocaso:
                                    break
        case 5:
            print(cons.MSG_ENCERRA_SISTEMA)
            f.AguardaeLimpa()
            break
        case outrocaso:
            print(cons.MSG_OPCAO_INVALIDA)
            f.AguardaeLimpa()