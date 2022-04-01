from ClasseContaCorrente import ContaCorrente
from ClasseContaPoupanca import ContaPoupanca
from ClasseContaSalario import ContaSalario
import funcoes as f

contasC = {} #Conta Corrente
contasS = {} #Conta Salário
contasP = {} #Conta Poupança

op = 0
tipoConta = 0

f.LimpaTela()
while op != 5:
    print('Banco Proway\n'
          '1- Criar Conta\n'
          '2- Listar Contas\n'
          '3- Excluir Conta\n'
          '4- Operações\n'
          '5- Sair')
    op = int(input('Informe a opção desejada: '))
    f.LimpaTela()
    match op:
        case 1:            
            tipoConta = f.validaTipoConta()
            f.LimpaTela()
            numero = input('Informe o número da conta: ')
            if len(numero) != 5:
                print('Número inválido')
                f.AguardaeLimpa()
            else:
                match tipoConta:
                    case 1:                    
                        if numero in contasC:
                            print('Conta Corrente já existente')
                        else:
                            c = ContaCorrente(numero)
                            contasC[c.conta] = 0
                            print('Conta Corrente cadastrada com sucesso')
                            del(c)
                    case 2:
                        if numero in contasS:
                            print('Conta Salário já existente')
                        else:
                            c = ContaSalario(numero)
                            contasS[c.conta] = 0
                            print('Conta Salário cadastrada com sucesso')
                            del(c)
                    case outrocaso:
                        if numero in contasP:
                            print('Conta Poupança já existente')
                        else:
                            c = ContaPoupanca(numero)
                            contasP[c.conta] = 0
                            print('Conta Poupança cadastrada com sucesso')
                            del(c)
            f.AguardaeLimpa()
        case 2:
            tipoConta = f.validaTipoConta()
            f.LimpaTela()
            match tipoConta:
                case 1:
                    if len(contasC) == 0:
                        print('Não há contas Corrente cadastradas')
                    else:
                        print(contasC)
                case 2:
                    if len(contasS) == 0:
                        print('Não há contas Salário cadastradas')
                    else:
                        print(contasS)
                case 3:
                    if len(contasP) == 0:
                        print('Não há contas Poupança cadastradas')
                    else:
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
                    if len(contasC) == 0:
                        print('Não há contas Corrente cadastradas')
                    else:
                        numero = input('Número da conta que deseja excluir: ')
                        if len(numero) != 5:
                            print('Número inválido')
                        else:
                            if not numero in contasC:
                                print('Conta inexistente')
                            else:
                                c = ContaCorrente(numero)
                                contasC.pop(c.conta)
                                print('Conta excluída com sucesso')
                                del(c)
                case 2:
                    if len(contasS) == 0:
                        print('Não há contas Salário cadastradas')
                    else:
                        numero = input('Número da conta que deseja excluir: ')
                        if len(numero) != 5:
                            print('Número inválido')
                        else:
                            if not numero in contasS:
                                print('Conta inexistente')
                            else:
                                c = ContaSalario(numero)
                                contasS.pop(c.conta)
                                print('Conta excluída com sucesso')
                                del(c)
                case outrocaso:
                    if len(contasP) == 0:
                        print('Não há contas Poupança cadastradas')
                    else:
                        numero = input('Número da conta que deseja excluir: ')
                        if len(numero) != 5:
                            print('Número inválido')
                        else:
                            if not numero in contasP:
                                print('Conta inexistente')
                            else:
                                c = ContaPoupanca(numero)
                                contasP.pop(c.conta)
                                print('Conta excluída com sucesso')
                                del(c)
            f.AguardaeLimpa()
        case 4:
            tipoConta = f.validaTipoConta()
            match tipoConta:
                case 1,3: #Conta Corrente
                    op = f.menuOperacoes(tipoConta)
                    match op:
                        case 1:
                            pass
                        case 2:
                            pass
                        case 3:
                            pass
                        case 4:
                            pass
                        case outrocaso:
                            pass
                case outrocaso: #Conta Poupança
                    op = f.menuOperacoes(tipoConta)
                    match op:
                        case 1:
                            pass
                        case 2:
                            pass
                        case outrocaso:
                            pass
        case 5:
            print('Obrigado por usar o sistema!!!')
            f.AguardaeLimpa()
            break
        case outrocaso:
            print('Opção inválida')
            f.AguardaeLimpa()