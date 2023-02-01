from Controle.classConexao import Conexao
from Modelo.classFuncionario import Funcionario
from psycopg2 import Error

try:
  con = Conexao("Empresa", "postgres", "123", "localhost", "5432")

  print(con.consultarBanco('''
                     SELECT * FROM funcionarios
                     '''))
  
  con.manipularBanco('''
                     INSERT INTO funcionarios (Func_nome, Func_cpf)
                      VALUES
                      ('Abelardo Júnior', '12345678901'),
                      ('Andressa Alencar', '12345678902'),
                      ('Maria Marineide', '12345678903')
                     ''')
  
  con.manipularBanco('''
                                   UPDATE funcionarios
                                   SET "func_nome" = 'Júnior'
                                    WHERE "func_nome" = 'Abelardo'
                                   ''')
  
  funcionario1 = Funcionario(None, 'Abel Jr', '12345678904')
  funcionario1.imprimirFuncionario()
  con.manipularBanco(funcionario1.inserirFuncionario("funcionarios"))
  
  con.limparDadosRepetidos("funcionarios","Func_ID","Func_nome")
  
  print(con.consultarBanco('''
                     SELECT Func_nome as "Nome do Funcionário",
                            Func_cpf as "CPF do funcionario"
                     FROM funcionarios
                     '''))
  
  con.fecharConexao()
except(Error) as error:
  print("Conexão falhou", error)