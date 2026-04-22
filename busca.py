def buscar_eleitor(conexao):
    print("\n--- Buscar Eleitor ---")
    
    cpf = input("Digite o CPF para buscar: ")

    cursor = conexao.cursor()

    try:
        comando = "SELECT * FROM eleitores WHERE cpf = %s"
        cursor.execute(comando, (cpf,))

        resultado = cursor.fetchone()

        if resultado:
            print("\nEleitor encontrado:")
            print("ID:", resultado[0])
            print("Nome:", resultado[1])
            print("CPF:", resultado[2])
            print("Título:", resultado[3])
        else:
            print("Eleitor não encontrado.")

    except:
        print("Erro ao buscar eleitor.")

    cursor.close()
