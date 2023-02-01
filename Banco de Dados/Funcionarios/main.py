import psycopg2 #Para instalar > pip install psycopg2 

def createTableFuncionario(cur,conexao):

    cur.execute('''
    CREATE TABLE "Funcionarios"(
    "Func_ID" INT GENERATED ALWAYS AS INDENTY PRIMARY KEY,
    "Func_Nome" varchar(255),
    "Func_CPF" char(11) UNIQUE NOT NULL,
    "Func_Salário" money,
    "Dept_ID" INT FOREIGN KEY
    );
    ''')
    conexao.commit()
    
def createTableDepartamento(cur,conexao):

    cur.execute('''
    CREATE TABLE "Departamentos"(
    "Dept_ID" INT GENERATED ALWAYS AS INDENTY PRIMARY KEY,
    "Dept_Nome" varchar(255),
    );
    ''')
    conexao.commit()

def inserirFuncionario(cur,conexao):
    novoNome = input("Insira o nome do novo funcionário: ")

    while True:
        novoCpf = input("Insira o CPF do novo funcionário: ")
        if len(novoCpf) != 11:
            print("Tamanho inválido, o cpf precisa conter 11 digitos")
        else:
            break
        
    novoSalario = input("Insira o Salário do novo funcionário: ")
    
    cur.execute(f'''
    INSERT INTO "Funcionarios"
    VALUES(default, '{novoNome}', '{novoCpf}', {novoSalario})
    ''')
    conexao.commit()
    
def inserirDepartamentos(cur, conexao):
  novoNomeDepartamento = input("Insira o nome do novo departamento")
  cur.execute(f'''
              INSERT INTO "Departamentos" 
              VALUES(DEFAULT, '{novoNomeDepartamento}')
              ''')
  conexao.commit()

def atualizarFuncionario(cur,conexao):
    listarFuncionario(cur,conexao)
    idFunc = int(input("Digite o id do funcionário que deseja modificar: "))

    cur.execute(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Func_ID" = {idFunc}
    ''')
    print("Funcionario escolhido:",cur.fetchone())

    novoNome = input("Digite o novo nome: ")

    while True:
        novoCpf = input("Insira o novo CPF do funcionário: ")
        if len(novoCpf) != 11:
            print("Tamanho inválido, o cpf precisa conter 11 digitos")
        else:
            break

    novoSalario = float(input("Digite o novo salário:"))

    cur.execute(f'''
    UPDATE "Funcionarios"
    SET "Func_Nome" = '{novoNome}', "Func_Salário" = {novoSalario}, "Func_CPF" = '{novoCpf}'
    WHERE "Func_ID" = {idFunc}
    ''')
    conexao.commit()

def atualizarDepartamento(cur, conexao):
  listarDepartamentos(cur, conexao)
  idDept = int(input("Digite o ID do departamento que você quer atualizar: "))
  
  cur.execute(f'''
              SELECT * FROM "Departamentos"
              WHERE "Dept_ID" = {idDept}
              ''')
  print("Departamento escolhido:",cur.fetchone())
  
  novoNomeDepartamento = input("Escreva o novo nome do departamento: ")
  
  cur.execute(f'''
              UPDATE "Departamentos"
              SET "Dept_Nome" = '{novoNomeDepartamento}'
              WHERE "Dept_ID" = '{idDept}'
              ''')
  conexao.commit()
  
def removerFuncionario(cur, conexao):
    listarFuncionario(cur,conexao)
    idFunc = int(input("Digite o id do funcionário que deseja remover: "))
    cur.execute(f'''
        SELECT * FROM "Funcionarios"
        WHERE "ID" = {idFunc}
    ''')
    print("Funcionario escolhido:",cur.fetchone())
    cur.execute(f'''
    DELETE FROM "Funcionarios"
    WHERE "ID" = {idFunc}
    ''')
    conexao.commit()

def removerDepartamento(cur, conexao):
  listarDepartamentos(cur, conexao)
  idDept = int(input("Digite o ID do departamento que você quer remover"))
  
  
  cur.execute(f'''
              SELECT * FROM "Departamentos"
              WHERE "Dept_ID" = {idDept}
              ''')
  print("Departamento escolhido:",cur.fetchone())
  
  cur.execute(f'''
              DELETE FROM "Departamentos"
              WHERE "Dept_ID" = '{idDept}'
              ''')
  conexao.commit()
  
def listarFuncionario(cur, conexao):
    cur.execute('''
    SELECT * FROM "Funcionarios"
    ''')
    funcionarios = cur.fetchall()
    print("ID | Nome | CPF | Salário")
    for funcionario in funcionarios:
        print(f"{funcionario[0]} | {funcionario[1]} | {funcionario[2]} | {funcionario[3]}")
        
    conexao.commit()

def listarDepartamentos(cur, conexao):
  cur.execute('''
              SELECT * FROM "Departamentos"
              ''')
  departamentos = cur.fetchall()
  print("ID | Nome ")
  for departamento in departamentos:
    print(f"{departamento[0]} | {departamento[1]}")
  conexao.commit()

while True:
    try:

        con = psycopg2.connect(database="Empresa",user="postgres", password="123", host="localhost", port="5432")
        #(database="Empresa",user="postgres", password="postgres", host="localhost", port="5432")

        cursor = con.cursor()
        print("Conectado")

        print('''
        1. Ver funcionários
        2. Inserir funcionário
        3. Modificar funcionario
        4. Remover funcionário
        5. Ver departamentos
        6. Inserir departamento
        7. Modificar departamento
        8. Remover departamento
        0. Sair do Programa
        ''')

        opcaoMenu = input("Escolha o que deseja fazer: ")

        match opcaoMenu:
            case "1":
                listarFuncionario(cursor, con)
            case "2":
                inserirFuncionario(cursor, con)
            case "3":
                atualizarFuncionario(cursor, con)
            case "4":
                removerFuncionario(cursor, con)
            case "5":
                listarDepartamentos(cursor, con)
            case "6":
                inserirDepartamentos(cursor, con)
            case "7":
                atualizarDepartamento(cursor, con)
            case "8":
                removerDepartamento(cursor, con)
            case "0":
                print("Você escolheu sair da aplicação. Até mais!")
                break
            case _:
                print("Você inseriu algum valor inválido.")

        input("Tecle Enter para prosseguir")

        cursor.close()
        con.close()

    except(Exception, psycopg2.Error) as error:
        print("Ocorreu um erro -", error)