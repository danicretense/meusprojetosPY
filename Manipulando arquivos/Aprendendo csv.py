import csv
from pathlib import Path
Root=Path(__file__).parent
#----Lendo arquivos csv
with open('Arquivos csv\Testando.csv','r') as meu: 
  lendo=csv.reader(meu)
  for row in lendo:
      print(row)
      
#---Escrevendo arquivos csv
with open (Root/'Nova tabela.csv','w')as arquivo:
  escrevendo=csv.writer(arquivo) 
  escrevendo.writerow(['Produto','Preço'])
  escrevendo.writerow(['Doritos',3.45])
  escrevendo.writerow(['Ruffles',5.00])
  escrevendo.writerow(['Yulo',2.88])
