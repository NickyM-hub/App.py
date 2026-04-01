import pyodbc
import time

server = 'TBS0676757W11-1\\SQLEXPRESS'
database = 'nova_conexao'
username = 'conection_nicky'
password = 'NickyM469'

time.sleep(1)

connection_string = f"""
DRIVER={{ODBC Driver 18 for SQL Server}};
SERVER={server};
DATABASE={database};
UID={username};
PWD={password};
TrustServerCertificate=yes;
"""

try:
    conn = pyodbc.connect(connection_string)
    print("Conexão bem-sucedida!")
except pyodbc.Error as e:
    print("Erro na conexão:")
    for err in e.args:
        print(err)
finally:
    try:
        conn.close()
    except:
        pass