from datetime import datetime
def menu():
    print(""" 
    Escolha uma opção:
    1-Depositar
    2-Sacar  
    3-Extrato
    4-Transferência         
    5-Criar Usuário
    6-Criar Conta            
    7-Sair 
    ===> """)
    try:
        return int(input())
    except ValueError:
        print("Opção inválida! Por favor, insira um número de 1 a 7.")
        return 0
def mostra_data():
  horario=datetime.now()
  horario_format=horario.strftime("%d/%m %H:%M\n----------")
  return horario_format

def depositar(saldo, valorD, extrato):
    if valorD >= 5:
        print("Deposito realizado com sucesso!")
        saldo += valorD
        extrato += "\nDepósito: R$%.2f\n" % valorD
        extrato+=mostra_data()
        print("Operação Realizada: Depósito\nValor: R$%.2f" %valorD )

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
        extrato += "\nSaque: R$%.2f\n" % valorS
        extrato+= mostra_data()
        numero_saques += 1  
        print("Saque realizado com sucesso!")
        print("Operação Realizada: Saque\nValor: R$%.2f" % valorS)
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
        print("Operação Realizada: Transferência\nValor: R$%.2f" % valort)           
        extrato += "\nTransferência: R$%.2f\n" % valort
        extrato+= mostra_data()

    return saldo, extrato, numero_trans        

def principal():
    AGENCIA = 0
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_trans = 0
    LIMITE_TRANS = 3
    LIMITE_SAQUE = 3
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        #OPÇÃO 1
        if opcao == 1:
            print("Depósito:")
            try:
                valorD = float(input("Qual valor deseja depositar? "))
                saldo, extrato = depositar(saldo, valorD, extrato)
            except ValueError:
                print("Valor inválido! Por favor, insira um número.")
        #OPÇÃO 2
        elif opcao == 2:
            print("Saque:") 
            try:
                valorS = float(input("Qual valor deseja sacar? "))
                saldo, extrato, numero_saques = sacar(
                    saldo=saldo,
                    valorS=valorS,
                    extrato=extrato,
                    numero_saques=numero_saques,
                    limite=limite,
                    LIMITE_SAQUE=LIMITE_SAQUE
                )
            except ValueError:
                print("Valor inválido! Por favor, insira um número.")
           #OPÇÃO 3     
        elif opcao == 3:
            exibindo_extrato(saldo, extrato=extrato)
          #OPÇÃO 4
        elif opcao == 4:
            print("Transferência:") 
            try:
                valort = float(input("Qual valor deseja transferir? "))
                saldo, extrato, numero_trans = transferencia(
                    saldo, valort, extrato, numero_trans, LIMITE_TRANS
                )
            except ValueError:
                print("Valor inválido! Por favor, insira um número.")
           #OPÇÃO 5     
        elif opcao == 5:
            criar_user(usuarios) 
         #OPÇÃO 6
        elif opcao == 6:
            numero_conta = len(contas) + 1
            conta = criar_contas(AGENCIA, numero_conta, usuarios)  
            if conta:
                contas.append(conta)
        #OPÇÃO 7
        elif opcao == 7:
            print("Obrigado por usar nosso serviço")
            break
        ##FIM
        else:
            if opcao != 0:
                print("Opção inválida!")

def criar_user(usuarios):
    try:
        cpf = int(input("Informe seu CPF (SOMENTE NÚMEROS): "))
        usuario = filtrar_user(cpf, usuarios)
        if usuario:
            print("Já existe um usuário com este CPF!")
            return
        nome = input("Digite seu nome completo: ")
        data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")    
        endereco = input("Informe seu endereço (Rua, Bairro, Cidade/Estado): ")
        usuarios.append({"Nome": nome, "Data de Nascimento": data_nascimento, "Endereço": endereco, "CPF": cpf})
        print("Usuário criado com sucesso!")
    except ValueError:
        print("CPF inválido! Por favor, insira um número.")

def filtrar_user(cpf, usuarios): 
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_contas(AGENCIA, numero_conta, usuarios):
    try:
        cpf = int(input("Informe seu CPF (SOMENTE NÚMEROS): "))
        usuario = filtrar_user(cpf, usuarios) 
        if usuario:
            print("Conta criada com sucesso!")
            return {"Agencia": AGENCIA, "Numero da conta": numero_conta, "Usuário": usuario}
        print("Usuário não encontrado!")
    except ValueError:
        print("CPF inválido! Por favor, insira um número.")

principal()
