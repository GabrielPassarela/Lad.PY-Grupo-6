import mysql.connector

def conectar():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='11121976jR@', # senha do MySQL
            database='projeto_integrador'
        )
        return conn
    except mysql.connector.Error:
        print(f"Erro ao conectar: {mysql.connector.Error}")

minha_conexao = conectar()
if minha_conexao:
    print("Conectado")
    minha_conexao.close()
