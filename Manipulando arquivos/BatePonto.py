import csv
from datetime import datetime

def pega_data(data, df):
    """Escreve a data e o horário de entrada e saída no arquivo CSV."""
    with open('Folha de ponto.csv', 'w', newline='') as novo:
        escrevendo = csv.writer(novo)
        escrevendo.writerow([data, df])

def ponto_entrada(entrada):
    """Guarda a data e horário de entrada no arquivo de texto."""
    with open('entradas.txt', 'w') as guardando:
        guardando.write(entrada)

def lendo_arquivo():
    """pega a data e a hora que esta guardada na função ponto_entrada"""
    with open('entradas.txt', 'r') as lendo:
        valores = lendo.readline().strip()
    return valores
def covertendo(saida,entrada):
    c1=datetime.strptime(entrada,'%d/%m/%Y %H:%M')
    diferenca= saida-c1
    return diferenca

data_formatada = None
condicao = input('Ponto de entrada ou de saída? (e/s) ').strip().lower()

if condicao == 'e':
    nome = input('Digite seu nome: ')
    data = datetime.now()
    data_formatada = data.strftime('%d/%m/%Y %H:%M')
    ponto_entrada(data_formatada)
elif condicao == 's':
    nome = input('Digite seu nome novamente: ')
    da = datetime.now()
    df = da.strftime('%d/%m/%Y %H:%M')
    pega_data(lendo_arquivo(), df)
    print(covertendo(da,lendo_arquivo()))
else:
    print('Opção inválida. Digite "e" para entrada ou "s" para saída.')
 
