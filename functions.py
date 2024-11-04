import psycopg2

def conect():
    try:
        conn = psycopg2.connect(
            host='localhost',
            dbname='pet_shop',
            user='tiago',
            password='tiago'
        )

        return conn
    except psycopg2.Error as e:
        print(f"Erro na conexão ao PostgreSQL Server: {e}")

def get_tables_name():

    conn = conect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public'
    """)

    tabelas = [row[0] for row in cursor.fetchall()]
    disconect(conn)

    return tabelas

def disconect(conn):
    if conn:
        conn.close()

def create(table):
    conn = conect()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table}')
    dados = cursor.fetchall()
    nomes_colunas = [descricao[0] for descricao in cursor.description]
    colunas_sem_id = nomes_colunas[1:]

    if len(dados) > 0:
        print('Ja existem dados cadastrados.\n')
    else:
        print('Não existem dados cadastrados.\n')
        return

    atualizar = 'SIM'

    while atualizar == 'SIM':
        valor = []
        for i, new in enumerate(colunas_sem_id):
            entry = input(f"Digite o novo valor de {new}: \n")
            valor.append(entry)

        colunas_str = ', '.join(colunas_sem_id)
        valores_str = ', '.join(f"'{v}'" for v in valor)

        command = f"INSERT INTO {table} ({colunas_str}) VALUES ({valores_str})"

        cursor.execute(command)
        conn.commit()

        if cursor.rowcount == 1:
            print("Produto excluído com sucesso.\n")
        else:
            print("Erro ao incluir novo dado.\n")

        atualizar = input("Deseja cadastrar outro dado? (SIM/NAO)\n")

    disconect(conn)

def read(table):

    conn = conect()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table}')
    dados = cursor.fetchall()
    nomes_colunas =  [descricao[0] for descricao in cursor.description]

    if len(dados) > 0:
        print('------------------------')
        for dado in dados:
            for i, name_col in enumerate(nomes_colunas):
                print(f"{name_col}: {dado[i]}")
            print('------------------------')

        print('------------------------')

    else:
        print('Não existem dados cadastrados')
    disconect(conn)

def update(table):

    conn = conect()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table}')
    dados = cursor.fetchall()
    nomes_colunas = [descricao[0] for descricao in cursor.description]
    colunas_sem_id = nomes_colunas[1:]

    if len(dados) > 0:
        print('------------------------')
        for dado in dados:
            for i, name_col in enumerate(nomes_colunas):
                print(f"{name_col}: {dado[i]}")
            print('------------------------')

        print('------------------------')

    else:
        print('Não existem dados cadastrados')
        disconect(conn)
        return

    atualizar = 'SIM'

    while atualizar == 'SIM':
        dado = int(input(f"Digite o {nomes_colunas[0]} a ser atualizado: \n"))
        for new in colunas_sem_id:
            valor = input(f"Digite o novo valor de {new}: \n")
            cursor.execute(f"UPDATE {table} SET {new} = '{valor}' WHERE {nomes_colunas[0]} = {dado}")
            conn.commit()

        if cursor.rowcount == 1:
            print("Produto excluído com sucesso.\n")
        else:
            print(f"Erro ao excluir o produto com id {dado}\n")

        atualizar = input("Deseja atualizar outro dado? (SIM/NAO)\n")

    disconect(conn)

def delete(table):
    conn = conect()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table}')
    dados = cursor.fetchall()
    nomes_colunas = [descricao[0] for descricao in cursor.description]

    if len(dados) > 0:
        print('------------------------')
        for dado in dados:
            for i, name_col in enumerate(nomes_colunas):
                print(f"{name_col}: {dado[i]}")
            print('------------------------')

        print('------------------------')

    else:
        print('Não existem dados cadastrados')
        disconect(conn)
        return

    atualizar = 'SIM'
    while atualizar == 'SIM':
        dado = int(input(f"Digite o {nomes_colunas[0]} a ser deletado: \n"))
        cursor.execute(f"DELETE FROM {table} WHERE {nomes_colunas[0]} = {dado}")
        conn.commit()

        if cursor.rowcount == 1:
            print("Dado excluído com sucesso.\n")
        else:
            print(f"Erro ao excluir o dado com id {dado}\n")

        atualizar = input("Deseja deletar outro dado? (SIM/NAO)\n")

    disconect(conn)







