import psycopg2

try:
  con = psycopg2.connect(database="Empresa",user="postgres",password="123",host="localhost",port="5432")
  print("Conectado")
  
  cursor = con.cursor()
  
  
  # cursor.execute('''
  #                CREATE TABLE Funcionarios (
  #                   Func_Id SERIAL PRIMARY KEY,
  #                   Func_nome VARCHAR(255),
  #                   Func_cpf CHAR(11),
  #                   Func_salario MONEY
  #                );
  #                ''')
  # con.commit()
  
  cursor.execute('''
                   INSERT INTO funcionarios (Func_Id, Func_nome, Func_cpf, Func_salario) VALUES (1, 'Abelardo', '12345678901', '1500,05')
                   ''')
  # con.commit()
  # cursor.execute('''
  #                DROP TABLE funcionarios
  #                ''')
  
  cursor.execute('''
                 SELECT * FROM "funcionarios";
                 ''')
  
  funcionarios = cursor.fetchall()
  
  for funcionario in funcionarios:
    print(f"""
          Func_Id: {funcionario[0]}
          Func_nome: {funcionario[1]}
          Func_cpf: {funcionario[2]}
          """)
  con.commit()
  
  con.close()
  
except(Exception,psycopg2.Error) as error:
  print("Conexão falhou", error) 