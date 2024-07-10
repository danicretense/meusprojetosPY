def lendo_arquivo():
    """pega a data e a hora que esta guardada na função ponto_entrada"""
    with open('entradas.txt', 'r') as lendo:
        valores = lendo.readline().strip()
    return valores
def covertendo(entrada):
    c1=datetime.strptime(entrada,'%d/%m/%Y %H:%M')
   
    return c1

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
    print(covertendo(lendo_arquivo()),da)
else:
    print('Opção inválida. Digite "e" para entrada ou "s" para saída.')
