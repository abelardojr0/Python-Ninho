import psycopg2

try:
    con = psycopg2.connect(database="BancoNinho",user="postgres",password="123",host="localhost",port="5432")
    print("Conectado ao banco de dados")
    cursor = con.cursor()

    # cursor.execute('''
    # DELETE FROM
    # "Alunos2"
    # WHERE "nome" = 'Marcio'
    # ''')
    # con.commit()

    
    cursor.execute(''''
                    CREATE TABLE "Alunos3" (
                        "Func_Id" INT,
                        "Func_nome" VARCHAR(255),
                        "Func_cpf" CHAR(11),
                        "Func_salario" MONEY
                    )
                    ''')
    con.commit()
  
    cursor.execute('''
    INSERT INTO "Alunos3"
    VALUES(default, 'Emilio', '22222')
    
    ''')
    con.commit()


    cursor.execute('''
        SELECT * FROM "Alunos3"
    ''')
    

    alunos = cursor.fetchall()

    for aluno in alunos:
        print(f'''
        Nro Matricula - {aluno[0]}
        CPF - {aluno[1]}
        Nome - {aluno[2]}
        ''')

    con.commit()
    
    con.close()
except:
    print("Deu errado")