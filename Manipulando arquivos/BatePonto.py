import csv
from datetime import datetime, timedelta

def covertendo(saida, entrada):
    c1 = datetime.strptime(entrada, '%d/%m/%Y %H:%M')
    diferenca = saida - c1
    return diferenca

def formatar_timedelta(td):
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours} horas, {minutes} minutos, {seconds} segundos"

def ponto_entrada(entrada):
    """Guarda a data e horário de entrada no arquivo de texto."""
    with open('entradas.txt', 'w') as guardando:
        guardando.write(entrada)

def lendo_arquivo():
    """Pega a data e a hora que está guardada na função ponto_entrada."""
    with open('entradas.txt', 'r') as lendo:
        valores = lendo.readline().strip()
    return valores

def pega_data(data, df):
    """Escreve a data e o horário de entrada e saída no arquivo CSV."""
    diferenca = covertendo(datetime.strptime(df, '%d/%m/%Y %H:%M'), data)
    with open('Folha de ponto.csv', 'a', newline='') as novo:
        escrevendo = csv.writer(novo)
        escrevendo.writerow([data, df, formatar_timedelta(diferenca)])
        
        
def inicializa_csv():
    """Inicializa o arquivo CSV com o cabeçalho, caso ainda não exista."""
    try:
        with open('Folha de ponto.csv', 'r') as file:
            pass
    except FileNotFoundError:
        with open('Folha de ponto.csv', 'w', newline='') as novo:
            escrevendo = csv.writer(novo)
            escrevendo.writerow(['Data de Entrada', 'Data de Saída', 'Tempo Trabalhado'])

inicializa_csv()        

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
    entrada = lendo_arquivo()
    pega_data(entrada, df)
    diferenca = covertendo(da, entrada)
    formatar_timedelta(diferenca)
else:
    print('Opção inválida. Digite "e" para entrada ou "s" para saída.')
 
