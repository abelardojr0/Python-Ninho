from psycopg2 import Error
from Controle.classConexao import Conexao
from Modelo.classLivro import Livro
from Modelo.classAutor import Autor

try:
  con = Conexao("Biblioteca", "postgres", "123", "localhost", "5432")
  
  
  # con.manipularBanco('''
  #                    CREATE TABLE "autores"(
  #                      id INT GENERATED ALWAYS AS IDENTITY,
  #                      nome VARCHAR(255),
                      
  #                      PRIMARY KEY(id)
                      
  #                    );
  #                    ''')
  
  # con.manipularBanco('''
  #                    CREATE TABLE "livros"(
  #                      id INT GENERATED ALWAYS AS IDENTITY,
  #                      nome VARCHAR(255),
  #                      paginas INT,
  #                      anoLancamento DATE,
  #                      id_autor INT,
  #                      CONSTRAINT fk_autor
  #                       FOREIGN KEY("id_autor")
  #                       REFERENCES autores ("id")
  #                       ON DELETE NO ACTION
  #                       ON UPDATE NO ACTION,
  #                     PRIMARY KEY (id) 
  #                    );
  #                    ''')
  
  # autor1 = Autor(None, 'J.R.R Tolkien')
  # autor2 = Autor(None, 'J.K Rowling')
  # autor3 = Autor(None, 'George R.R Martin')
  # livro1 = Livro(None , 'O Senhor dos Aneis - As Duas Torres', '360', '1954-01-01', 1 )
  # livro2 = Livro(None , 'Harry Potter e a Pedra Filosofal', '300', '1997-01-01', 2 )
  # livro3 = Livro(None , 'Game of Thones - O Festim dos Corvos', '600', '1985-03-03', 19 )
  
  # con.manipularBanco(autor1.inserirAutor()) 
  # con.manipularBanco(autor2.inserirAutor())
  # con.manipularBanco(autor3.inserirAutor())
  # con.manipularBanco(livro1.inserirLivro())
  # con.manipularBanco(livro2.inserirLivro())
  # con.manipularBanco(livro3.inserirLivro())
  
  def mostrarLivros(conexao):
    listaDeLivros = conexao.consultarBanco('''
                                           SELECT * FROM "livros"
                                            ORDER BY "id" ASC
                                          ''')
    print("ID | Nome")
    for livro in listaDeLivros:
      print(f'{livro[0]} | {livro[1]}')
      
  def mostrarAutores(conexao):
      listaDeAutores = conexao.consultarBanco('''
                                            SELECT * FROM "autores"
                                              ORDER BY "id" ASC
                                            ''')
      print("ID | Nome")
      for autor in listaDeAutores:
        print(f'{autor[0]} | {autor[1]}')

  escolha = 1
  while(escolha!=0):
    escolha = int(input("""O que você quer manipular?
                        1 - Livros
                        2 - Autores
                        0 - Sair
                        """))
    
    match escolha:
      case 1:      
        opcoes = 1
        while(opcoes!=0):
          opcoes = int(input("""O que você deseja fazer?
                                1 - Inserir novo livro
                                2 - Visualizar livro
                                3 - Atualizar livro
                                4 - Deletar livro
                                0 - Voltar
                            """))
          match opcoes:
            case 1:
              nome = input("Digite o nome do novo livro: ")
              paginas = input("Digite a quantidade de paginas do livro: ")
              data = input("Digite a data de lancamento do livro: ")
              
              mostrarAutores(con)
              autor = int(input("Digite o ID do autor: "))
              
              novoLivro = Livro(None, nome, paginas, data, autor)
              con.manipularBanco(novoLivro.inserirLivro())
              
            case 2:
              mostrarLivros(con)
              
              escolhaVisualizar = int(input("Escolha o livro que você deseja visualizar (digite o id do livro): ")) 
              
              livroSelecionadoVisualizar = con.consultarBanco(f'''
                                                    SELECT * FROM "livros"
                                                      WHERE "id" = '{escolhaVisualizar}'
                                                    ''')
              
              novoLivroVisualizar = Livro(livroSelecionadoVisualizar[0][0], livroSelecionadoVisualizar[0][1], livroSelecionadoVisualizar[0][2], livroSelecionadoVisualizar[0][3], livroSelecionadoVisualizar[0][4])
              
              novoLivroVisualizar.selecionarLivro()
              
            case 3:
              mostrarLivros(con)
              
              escolhaAtualizar = int(input("Escolha o livro que você deseja alterar (digite o id do livro): "))
              
              livroSelecionado = con.consultarBanco(f'''
                                                    SELECT * FROM "livros"
                                                      WHERE "id" = '{escolhaAtualizar}'
                                                    ''')
              novoLivroAtualizar = Livro(livroSelecionado[0][0], livroSelecionado[0][1], livroSelecionado[0][2], livroSelecionado[0][3], livroSelecionado[0][4])
              
              escolhaCampoAtualizar = int(input("""Qual campo você deseja atualizar?
                                                1 - Nome
                                                2 - Paginas
                                                3 - Data
                                                4 - Autor
                                                """))
              
              match escolhaCampoAtualizar:
                case 1:
                    novoLivroAtualizar.setNome(input("Digite o novo nome: "))
                    con.manipularBanco(novoLivroAtualizar.atualizarLivro())
                case 2:
                  novoLivroAtualizar.setPaginas(input("Digite a nova quantidade de páginas: "))
                  con.manipularBanco(novoLivroAtualizar.atualizarLivro())
                case 3:
                  novoLivroAtualizar.setData(input("Digite a nova data: (YYYY-MM-DD) "))
                  con.manipularBanco(novoLivroAtualizar.atualizarLivro())
                case 4:
                  novoLivroAtualizar.setIdAutor(int(input("Digite o novo ID do autor: ")))
                  con.manipularBanco(novoLivroAtualizar.atualizarLivro())
                  
            case 4: 
              mostrarLivros(con)
              escolhaDelete = int(input("Escolha o livro que você deseja deletar (digite o id do livro): "))
              
              livroSelecionadoDeletar = con.consultarBanco(f'''
                                                    SELECT * FROM "livros"
                                                      WHERE "id" = '{escolhaDelete}'
                                                    ''')
              
              livroDeletar = Livro(livroSelecionadoDeletar[0][0], livroSelecionadoDeletar[0][1], livroSelecionadoDeletar[0][2], livroSelecionadoDeletar[0][3], livroSelecionadoDeletar[0][4])
              
              con.manipularBanco(livroDeletar.deletarLivro())
          
      case 2:
        opcoesAutor = 1
        while(opcoesAutor!=0):
          opcoesAutor = int(input("""O que você deseja fazer?
                                1 - Inserir novo autor
                                2 - Listar autores
                                3 - Atualizar autor
                                4 - Deletar autor
                                0 - Voltar
                            """))
          match opcoesAutor:
            case 1:
              nomeAutor = input("Digite o nome do novo autor: ")
              novoAutor = Autor(None, nomeAutor)
              con.manipularBanco(novoAutor.inserirAutor())
              
            case 2:
              mostrarAutores(con)
              
            case 3:
              mostrarAutores(con)
              escolhaAtualizarAutor = int(input("Escolha o autor que você deseja alterar (digite o id do autor): "))
              
              autorSelecionado = con.consultarBanco(f'''
                                                    SELECT * FROM "autores"
                                                      WHERE "id" = '{escolhaAtualizarAutor}'
                                                    ''')
              novoAutorAtualizar = Autor(autorSelecionado[0][0], autorSelecionado[0][1])
              
              novoAutorAtualizar.setNome(input("Digite o novo nome: "))
              con.manipularBanco(novoAutorAtualizar.atualizarAutor())
              
              
            case 4: 
              mostrarAutores(con)
              escolhaDeleteAutor = int(input("Escolha o autor que você deseja deletar (digite o id do autor): "))
              
              con.manipularBanco(f'''
                                DELETE FROM "autores"
                                  WHERE "id" = '{escolhaDeleteAutor}'
                                ''')
          
  con.limparDadosRepetidos("livros","id", "nome")
  con.limparDadosRepetidos("autores","id", "nome")
  
  print("Conexão bem sucedida")
  
except(Error) as error:
  print("Falha ao se conectar, error: ", error)