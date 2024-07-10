import csv
from datetime import datetime

def pega_data(data, df):
    """Escreve a data e o horário de entrada e saída no arquivo CSV."""
    with open('Folha de ponto.csv', 'a', newline='') as novo:
        escrevendo = csv.writer(novo)
        escrevendo.writerow([data, df])

def ponto_entrada(entrada):
    """Guarda a data e horário de entrada no arquivo de texto."""
    with open('entradas.txt', 'w') as guardando:
        guardando.write(entrada)

def lendo_arquivo():
    """Lê a data e horário de entrada do arquivo de texto."""
    with open('entradas.txt', 'r') as lendo:
        valores = lendo.readline().strip()
    return valores

data_formatada = None
condicao = input('Ponto de entrada ou de saída? (e/s) ').strip().lower()

if condicao == 'e':
    nome = input('Digite seu nome: ')
    data = datetime.now()
    data_formatada = data.strftime('%d/%m %H:%M')
    ponto_entrada(data_formatada)
elif condicao == 's':
    nome = input('Digite seu nome novamente: ')
    da = datetime.now()
    df = da.strftime('%d/%m %H:%M')
    pega_data(lendo_arquivo(), df)
else:
    print('Opção inválida. Digite "e" para entrada ou "s" para saída.')
