def menu():
    print(""" 
    Escolha uma opção:
    1-Depositar
    2-Sacar  
    3-Extrato
    4-Transferência
    5-Sair 
    ===> """) 
    return int(input())

def depositar(saldo, valorD, extrato):
    if valorD >= 5:
        print("Deposito realizado com sucesso!")
        saldo += valorD
        extrato += "Depósito: R$%.2f\n" % valorD
        print("Operaçao Realizada: Deposito\nValor: R$%.2f" % valorD)
    elif valorD == 0:
        print("Operação cancelada com sucesso!")
    else:      
        print("O valor digitado é inválido! O valor mínimo de depósito é R$5.00")
    return saldo, extrato    

def sacar(saldo, valorS, extrato, numero_saques, limite, LIMITE_SAQUE): 
    excedeu_saldo = valorS > saldo
    excedeu_limite = valorS > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUE

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excedeu o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valorS > 0:
        saldo -= valorS  
        extrato += "Saque: R$%.2f\n" % valorS
        numero_saques += 1  
        print("Saque realizado com sucesso!")
        print("Operaçao Realizada: Saque\nValor: R$%.2f" % valorS)
    else:      
        print("O valor informado é inválido!") 
    return saldo, extrato, numero_saques  

def exibindo_extrato(saldo, extrato):
    print("Extrato:")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("Saldo: R$%.2f" % saldo)

def transferencia(saldo, valort, extrato, numero_trans, LIMITE_TRANS):
    excedeu_Limitet = numero_trans >= LIMITE_TRANS

    if excedeu_Limitet:
        print("Você excedeu o limite de transferências")
    elif saldo <= 0:
        print("Você não tem saldo suficiente") 
    elif valort > saldo:
        print("Você não possui saldo para esta operação")
    elif valort <= 0:
        print("O valor digitado é inválido") 
    else:
        saldo -= valort
        numero_trans += 1
        print("Transferência realizada com sucesso!")
        print("Operaçao Realizada: Transferência\nValor: R$%.2f" % valort)           
        extrato += "Transferência: R$%.2f\n" % valort

    return saldo, extrato, numero_trans        

def principal():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_trans = 0
    LIMITE_TRANS = 3
    LIMITE_SAQUE = 3

    while True:
        opcao = menu()
        # ----OPÇÃO 1
        if opcao == 1:
            print("Deposito :")
            valorD = float(input("Qual valor deseja depositar? "))
            saldo, extrato = depositar(saldo, valorD, extrato)

        # -----OPÇÃO 2 
        elif opcao == 2:
            print("Saque:") 
            valorS = float(input("Qual valor deseja sacar? "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valorS=valorS,
                extrato=extrato,
                numero_saques=numero_saques,
                limite=limite,
                LIMITE_SAQUE=LIMITE_SAQUE
            )
        #----OPCÃO 3
        elif opcao == 3:
            exibindo_extrato(saldo, extrato=extrato)
        # ----OPÇÃO 4     
        elif opcao == 4:
            print("Transferência:") 
            valort = float(input("Qual valor deseja transferir? "))
            saldo, extrato, numero_trans = transferencia(
                saldo, valort, extrato, numero_trans, LIMITE_TRANS
            )
        elif opcao == 5:
            print("Obrigado por usar nosso serviço")
            break
        else:
            print("Opção inválida!")

principal()
