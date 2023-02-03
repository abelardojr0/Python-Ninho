from Controle.classConexao import Conexao
from Modelo.classFuncionario import Funcionario
from psycopg2 import Error

def mostrarFuncionarios(conexao):
    listaFuncionarios = conexao.consultarBanco('''
    SELECT * FROM "funcionarios"
    ORDER BY "id" ASC
    ''')
    print("ID | Nome")
    for func in listaFuncionarios:
        print(f"{func[0]} - {func[1]} \n")

try:
  con = Conexao("Empresa", "postgres", "postgres", "localhost", "5432")

  mostrarFuncionarios(con)
  
  funcionarioEscolhido = input("Escolha o id do funcionario que deseja alterar: ")

  funcionarioConsulta = con.consultarBanco(f'''
    SELECT * FROM "funcionarios"
    WHERE "id" = '{funcionarioEscolhido}'
    ''')
  
  funcionario = Funcionario(funcionarioConsulta[0][0], funcionarioConsulta[0][1], funcionarioConsulta[0][2], funcionarioConsulta[0][3], funcionarioConsulta[0][4])

  print("Funcionario escolhido foi:")
  print(funcionario.imprimirFuncionario())

  opcoes = 1
  while(opcoes != 0):
    opcoes = int(input("""O que você deseja alterar?
                  Informações basicas(1)
                  Departamento(2)
                  Sair(0)
                  """))

    match opcoes:
          case 1:
              funcionario.nome = input("Escreva o novo nome: ")
              funcionario.cpf = input("Escreva o novo cpf: ")
              funcionario.salario = input("Escreva o novo salário: ")

              con.manipularBanco(funcionario.atualizarFuncionario("funcionarios"))
          case 2: 
              funcionario.idDepartamento = input("Insira o id do novo Departamento: ")
              con.manipularBanco(funcionario.atualizarDepartamentoFuncionario("funcionarios"))

  print(funcionario.imprimirFuncionario())

  mostrarFuncionarios(con)

  con.fecharConexao()

  
  
  
  
  
  
  
  
  
  
  # print(con.consultarBanco('''
  #                    SELECT * FROM funcionarios
  #                    '''))
  
  # con.manipularBanco('''
  #                     INSERT INTO departamentos (Nome)
  #                     VALUES 
  #                       ('TI'),
  #                       ('RH'),
  #                       ('Financeiro')
  #                    ''')
  # con.manipularBanco('''
  #                    INSERT INTO funcionarios (Nome, CPF, Salário, ID_Departamento)
  #                     VALUES
  #                       ('Abelardo Júnior', '12345678901', '2000', '1'),
  #                       ('Andressa Alencar', '12345678902', '3000', '1'),
  #                       ('Maria Marineide', '12345678903', '1500', '2')
  #                    ''')
  
  # con.manipularBanco('''
  #                                  UPDATE funcionarios
  #                                  SET nome = 'Júnior'
  #                                   WHERE nome = 'Abelardo'
  #                                  ''')
  
  # funcionario1 = Funcionario(None, 'Abel Jr', '12345678904', '4000', '1')
  # funcionario1.imprimirFuncionario()
  # con.manipularBanco(funcionario1.inserirFuncionario("funcionarios"))
  
  # con.limparDadosRepetidos("funcionarios","ID","Nome")
  # con.limparDadosRepetidos("departamentos","ID","Nome")
  
  # print(con.consultarBanco('''
  #                    SELECT Nome as "Nome do Funcionário",
  #                           CPF as "CPF do funcionario"
  #                    FROM funcionarios
  #                    '''))
  
  # con.fecharConexao()
except(Error) as error:
  print("Conexão falhou", error)