import psycopg2
from faker import Faker

# VARIAVEL QUE VAI DEFINIR EM QUE LINGUAGEM SERÃO GERADO OS DADOS.
fake = Faker(['pt-BR'])

try:  # CASO A REQUISIÇÃO DÊ CERTO...
    con = psycopg2.connect(database="db_abel", user="postgres",
                           password="postgres", host="localhost", port="5432")
    print("Conectado ao banco de dados")

    cursor = con.cursor()

    # COMANDO PARA CRIAR TABELA -------------------------------------------------------------------------------------------------------------
    # cursor.execute('''
    #         CREATE TABLE alunos (
    #             id SERIAL PRIMARY KEY,
    #             nome  VARCHAR(255),
    #             cpf VARCHAR(255)
    #         )
    #                  ''')
    # con.commit()

    # COMANDO PARA INSERIR----------------------------------------------------------------------------------------------------------------------------------
    # cursor.execute('''
    #   INSERT INTO "alunos" (
    #       "nome",
    #       "cpf"
    #       )
    #   VALUES(
    #       'Emilio',
    #       '10987654321'
    #       ),
    #       (
    #       'Abelardo',
    #       '12345678901'
    #       )
    #   ''')
    # con.commit()

    # # COMANDO PARA DELETAR CAMPOS----------------------------------------------------------------------------------------------------------------------------------
    # cursor.execute('''
    #                DELETE FROM "alunos" WHERE "nome" <> 'Abelardo'
    #                ''')
    # con.commit()

    # COMANDO PARA ATUALIZAR -------------------------------------------------------------------------------------------------------------------------------
    # cursor.execute('''
    #         UPDATE "alunos" SET "nome" = 'Emilia Amorim' WHERE "nome" = 'Emilio'
    #                   ''')
    # con.commit()

    # COMANDOS PARA ALTERAR -------------------------------------------------------------------------------------------------------------------------------
    # ADICIONANDO COLUNA
    # cursor.execute('''
    #         ALTER TABLE alunos ADD outro CHAR(11);
    #                 ''')
    # # REMOVENDO COLUNA
    # cursor.execute('''
    #                 ALTER TABLE alunos DROP COLUMN outro
    #                 ''')
    # con.commit()

    # COMANDO PARA APAGAR TABELA -------------------------------------------------------------------------------------------------------------------------------
    # cursor.execute('''
    #                 DROP TABLE alunos
    #                 ''')
    # con.commit()

    # FUNÇÃO PARA ADICIONAR 15 ALUNOS ALETORIOS NO BANCO
    # for i in range(15):
    #         cursor.execute(f'''
    #       INSERT INTO "alunos" (
    #           "nome",
    #           "cpf"
    #           )
    #       VALUES(
    #           '{fake.name()}',
    #           '{fake.cpf()}'
    #           )
    #       ''')
    # con.commit()

    # COMANDO PARA PUXAR OS DADOS DA TABELA -------------------------------------------------------------------------------------------------------------------------------
    cursor.execute('''
        SELECT * FROM "alunos"
            ''')
    con.commit()

    # VARIAVEL QUE VAI PEGAR O CARREGAMENTO COMPLETO FEITO PELO SELECT
    alunos = cursor.fetchall()

    # LOOP QUE VAI PRINTAR TODOS OS ALUNOS COM SEUS DADOS.
    for aluno in alunos:
        print(f'''
          ID - {aluno[0]}
          NOME - {aluno[1]}
          CPF - {aluno[2]}
          ''')

    con.close()  # COMANDO QUE FECHA A CONEXÃO

except(Exception, psycopg2.Error) as error:  # CASO A REQUISICÃO DÊ ERRADO...
    print("Deu errado")
