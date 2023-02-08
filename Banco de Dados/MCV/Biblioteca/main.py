from psycopg2 import Error
from Controle.classConexao import Conexao
from Modelo.classLivro import Livro
from Modelo.classCliente import Cliente
  
# DROP TABLE IF EXISTS clientes
# CREATE TABLE clientes(
# 	id INT GENERATED ALWAYS AS IDENTITY,
# 	nome VARCHAR(255) NOT NULL,
# 	cpf CHAR(11) NOT NULL UNIQUE,
# 	PRIMARY KEY (id)
	
# );

# DROP TABLE IF EXISTS livros
# CREATE TABLE livros(

# 	id INT GENERATED ALWAYS AS IDENTITY,
# 	nome VARCHAR(255) NOT NULL,
# 	autor VARCHAR(255) NOT NULL,
# 	PRIMARY KEY(id)
# );

# DROP TABLE IF EXISTS aluguel;
# CREATE TABLE aluguel(
#         id int GENERATED ALWAYS AS IDENTITY,
#         id_cliente int NOT NULL,
#         id_livro int NOT NULL,
#         data_aluguel TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#         Primary Key(id),
	
#         Constraint fk_cliente
#             FOREIGN KEY (id_cliente)
#             REFERENCES clientes (id)
#             ON DELETE CASCADE
#             ON UPDATE NO ACTION
#             ,
#         Constraint fk_livro
#             FOREIGN KEY (id_livro)
#             REFERENCES livros (id)
#             ON DELETE SET NULL
#             ON UPDATE NO ACTION
            
#     );
  
  
def menuClientes(conexao):
    print("Lista de clientes: ")
    resultado = conexao.consultarBanco('''
    Select * FROM clientes
    ORDER BY id ASC
    ''')
    print("ID | Nome")
    for cliente in resultado:
        print(f"{cliente[0]} | {cliente[1]}")

    print(f'''
    Escolha uma das opções:
    1. Ver cliente específico
    2. Inserir novo cliente
    0. Voltar para o menu principal
    ''')
    opcoes = int(input("Digite o número da opção desejada:"))
    match opcoes:
        case 1:
            while True:
                clienteID = input("Digite o ID do cliente")
                clienteEscolhido = Cliente(clienteID, None, None)
                resultado = conexao.consultarBanco(clienteEscolhido.consultarClientePorID())
                if resultado != []:
                    clienteEscolhido._nome = resultado[0][1]
                    clienteEscolhido._cpf = resultado[0][2]
                    clienteEscolhido.imprimirCliente()

                    while True:
                        print(f'''
                        Escolha uma das opções:
                        1. Ver alugueis
                        0. Voltar para o menu principal
                        ''')
                        opcoes = input("Digite o numero da opção:")
                        match opcoes:
                            case "1":
                                resultado = conexao.consultarBanco(clienteEscolhido.consultarAlugueis())
                                if resultado != []:
                                    print("ID | Data")
                                    for aluguel in resultado:
                                        print(f"{aluguel[0]} | {aluguel[3]}")
                                else:
                                    print("Esse usuário não possui alugueis")
                                input("Tecle ENTER para continuar")
                            case "0":
                                print("Saindo do menu cliente.")
                                break
                            case _:
                                print("Você escolheu uma opção inválida")

                    break
                else:
                    print("Você escolheu um ID inválido")



while True:
    try:
        con = Conexao("Biblioteca", "postgres", "postgres", "localhost","5432")
        break

    except (Error) as error:
        print("Ocorreu um erro -", error)


while True:
    try:
        print("Bem vindo a biblioteca 'Biblioteca dos Livros' ")

        print(f'''
    Escolha uma das opções:
    1. Ver Clientes
    2. Ver Livros
    3. Ver Alugueis
    0. Sair
        
        ''')
        opcoes = input("Digite o número da opção do menu:")

        match opcoes:
            case "1":
              menuClientes(con)
            case "2":
                print("Vendo Livros")
            case "3":
                print("Vendo Alugueis")
            case "0":
                print("Saindo da aplicação...")
                break
            case _:
                print("Você digitou uma opção inválida.")

        input("Pressione qualquer tecla para continuar")

        con.fechar()

    except (Error) as error:
        print("Ocorreu um erro -",error)