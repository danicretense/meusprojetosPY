import os, shutil

#Lendo um arquivo
mostrar=open('arquivo.txt','r')
#print(mostrar.read())
#print(mostrar.readline())
print(mostrar.readlines())
mostrar.close()
#Escrevendo em um arquivo
m=open('ask.txt','w')
m.writelines('Primeira linha do texto\n')
m.writelines('To make your document look professionally produced.')
m.close()

#------Criando uma pasta
#os.mkdir("Arquivos de textos")
#------Renomendo arquivos
#os.rename('ask.txt','pergunta.txt')

#-----Tratando erros
#@@@@ FileNotFoundError@@@@

#try:
 #abrindo=open('len.txt','r')
#except FileNotFoundError:
 #print("Não existe esse arquivo no diretorio!!!")
#os.mkdir("Arquivos csv")
