import mysql.connector
from datetime import datetime

conexao = mysql.connector.connect(
                host='localhost',
                user='root',
                password='765FHJyjd$_@',
                database='db_floor',
            )
cursor = conexao.cursor()
data=[datetime.now()]
comando = 'INSERT INTO registros (entradas) VALUES(%s)'
v=(data)
cursor.execute(comando,v)
#outra_data=datetime.now()

conexao.commit()
cursor.close()