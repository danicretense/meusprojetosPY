#  Nova função adicionada:
# Agora o usuario irá poder realizar transferências apartir de R$10,00         
menu= """ Digite uma opção:
1-Depositar
2-Sacar  
3-Extrato
4-Transferência 
5-Sair
===> """
saldo=0
limite=500
extrato=" "
numero_saques=0
numero_trans=0
LIMITE_TRANS=3
LIMITE_SAQUE= 4
while True:
 
 opcao = int(input(menu))
   
 if opcao==1:
      print("Deposito :")
      print("Digite 0 caso queira cancelar a operação")
      valorD=float(input("Qual valor deseja depositar?"))
      if valorD>=5:
          print("Deposito realizado com sucesso!")
          saldo+=valorD
          extrato += "Depósito:R$%d\n"%(valorD)
          print("Operaçao Realizada: Deposito\nValor:%d"%(valorD))
      elif valorD==0:
          print("Operação cancelada com sucesso!")
          continue
          
                
      else:      
       print("O valor digitado é invalido!\nO valor minimo de deposito é R$5.00")

      
 elif opcao==2:
      print("Saque:") 
      print("Digite 0 caso queira cancelar a operação") 
      valorS=float(input("Qual valor deseja sacar? "))
      excedeu_saldo= valorS>saldo
      excedeu_limite = valorS > limite
      excedeu_saques = numero_saques>=LIMITE_SAQUE
      if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

      elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")

      elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
      elif valorS>0:
          saldo-=valorS  
          extrato += " Saque:R$%d\n"%(valorS)
          numero_saques+=1  
          print("Saque realizado com sucesso!")
          print("Operaçao Realizada: Saque\nValor:%d" %(valorS))
      elif valorS==0:
          print("Operação cancelada com sucesso")   
      else:      
          print("O valor informado é invalido!") 
 elif opcao==3:
     print(" Extrato:")  
     print("Não foram realizadas movimentações."if not extrato else extrato)
     print(" Saldo:R$%d"%(saldo))
          
 elif opcao==4:
     if saldo<10:
         print("Você não possui saldo suficiente!")
     else:    
      valorT=float(input("Digite o valor que deseja transferir: "))
      excedeu_trans = numero_trans>=LIMITE_TRANS
      excedeu_saldo=saldo<valorT
      print("Transferência:")
      if excedeu_trans:
         print("Você execedeu o numero de transferências!")
      elif valorT<10 and valorT>0:
         print("❌❌❌ A transferência minima é de R$10,00")    
      
      elif excedeu_saldo:
         print("você não possui saldo para esta operação!")    
      elif valorT<0:
         print("O valor digitado é inválido!")  
      else:
         numero_trans+=1  
         saldo-=valorT 
         extrato += " Transferência:R$%d\n"%(valorT)
         print("Transferência realizada com sucesso!")
         print("Operaçao Realizada: Transferência\nValor:%d" %(valorT))    

          
 elif opcao==5:
        print("Obrigado por utilizar o nosso serviço, Até Logo😉")
        break
 else:
  print("Operação inválida, por favor selecione a operação desejada") 