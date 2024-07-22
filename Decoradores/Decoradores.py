def Decorador_Science(funcao):
   
   def v():
    print('testando')
    funcao()
    
   return v
 

@Decorador_Science    
def testando():
   contador=0
   estados=[]
   while True:
     digitando= input("Dgite um estado,você pode digitar até 03 estados: ")
     estados+=[digitando]
     contador+=1
     if(contador==3):
      break 
   for item in estados:
    # Loop que percorre cada item na lista "itens"
     print(f"- {item}")
testando()  

   
      