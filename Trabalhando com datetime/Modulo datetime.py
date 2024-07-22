from datetime import date,time,timedelta,datetime
import pytz 

#-----Uso da classe DATE
data=date.today().strftime('%d/%m/%Y')
nome_mes=date(2024,5,21)
#print(data)
#------Mostra o nome do mês
#print(nome_mes.strftime("%B"))

#Convertendo string em objeto Date
dl=date.fromisoformat("2022-05-13")
print(dl.strftime('%d/%m/%Y'))


#Uso da classe DATETIME
p=datetime.now().strftime('Já são: %H:%M')
v=datetime.today()
vt=datetime.now()
#print(vt.year)
#print(v)
#print(p)
n=datetime(2024,4,13).strftime('%d/%m/%Y')
#print(n)
#Convertendo string em um objeto datetime
#data_digitada=input('Data de nascimento: ')
#converter_data=datetime.strptime(data_digitada,'%d/%m/%Y')
#mostrar = converter_data.strftime('%d/%m/%Y')
#print(f"você nasceu no ano de: {mostrar}")


#Uso da classe TIME
hora_digitada=time(hour=20,minute=30)
print(hora_digitada.strftime('%H:%M'))


#----Uso da classe TIMEDELTA
prox_data= date.today()+timedelta(days=7)
pd=prox_data.strftime('%d/%m %A')
print(f'daqui a 7 dias será {pd}')
#---Uso da Biblioteca PYTZ
utc=datetime.now(pytz.timezone("America/Sao_Paulo"))
print(utc)
