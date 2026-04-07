import mysql.connector

def conectar():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',      # seu usuário do MySQL
            password='', # sua senha do MySQL
            database='projeto_integrador'
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Erro ao conectar: {err}")
        return None

if __name__ == "__main__":
    conexao = conectar()
    if conexao:
        print("Conectado com sucesso ao banco de dados!")
        conexao.close()
    else:
        print("Falha na conexão.")