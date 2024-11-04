import functions

functions.conect()

lista_tabelas = functions.get_tables_name()

# Criando menu de alternativas

print("Bem vindo. Selecione a alternativa que deseja executar.\n")
alternativa = input("(1) CADASTRAR DADOS.\n"
                    "(2) PESQUISAR DADOS.\n"
                    "(3) ATUALIZAR DADOS.\n"
                    "(4) DELETAR DADOS.\n")

if alternativa == '1':
    for t in lista_tabelas:
        print(f"Tabela {t}")
    table = input("Qual tabela deseja dadastrar dados?\n")
    functions.create(table)

if alternativa == '2':
    for t in lista_tabelas:
        print(f"Tabela {t}")
    table = input("Qual tabela deseja pesquisar?\n")
    functions.read(table)

if alternativa == '3':
    for t in lista_tabelas:
        print(f"Tabela {t}")
    table = input("Qual tabela deseja atualizar?\n")
    functions.update(table)

if alternativa == '4':
    for t in lista_tabelas:
        print(f"Tabela {t}")
    table = input("Qual tabela deseja deletar algum dado?\n")
    functions.delete(table)