from psycopg2 import Error
from Controle.classConexao import Conexao

try:
  con = Conexao("Biblioteca", "postgres", "postgres", "localhost", "5432")
  
  
  con.manipularBanco('''
                     CREATE TABLE "autor"(
                       id INT GENERATED ALWAYS AS IDENTITY,
                       nome VARCHAR(255)
                     );
                     ''')
  
  con.manipularBanco('''
                     CREATE TABLE "livros"(
                       id INT GENERATED ALWAYS AS IDENTITY,
                       nome VARCHAR(255),
                       paginas INT,
                       anoLancamento DATE,
                       id_autor INT,
                       CONSTRAINT fk_autor
                        FOREIGN KEY("id_autor")
                        REFERENCES autor ("id")
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION,
                      PRIMARY KEY (id) 
                     );
                     ''')
  
  
  con.manipularBanco('''
                     INSERT INTO 
                     ''')
  con.limparDadosRepetidos("livros","id", "nome")
  con.limparDadosRepetidos("autor","id", "nome")
  
except(Error) as error:
  print("Falha ao se conectar, error: ", error)