from Controle.Conexao import Conexao
from Modelo.Jogo import Jogo
from Modelo.Usuario import Usuario
from psycopg2 import Error

try:
  con = Conexao("Luderia", "postgres", "123", "localhost", "5432")
  
  def mostrarJogos():
    listaDeJogos = con.consultarBanco('''
                        SELECT * FROM jogos
                          ORDER BY id ASC
                      ''')
    for jogo in listaDeJogos:
      print(f"""
            ID - {jogo[0]}
            Nome - {jogo[1]}
            """)
      
  def buscarJogoEscolhido(id):
    query = (f'''
            SELECT * FROM jogos
              WHERE id = {id}
            ''')
    return query
  
  def buscarUsuarioEscolhido(id):
    query = (f'''
            SELECT * FROM usuarios
              WHERE id = {id}
            ''')
    return query
  
  def mostrarUsuarios():
    listaDeUsuarios = con.consultarBanco('''
                        SELECT * FROM usuarios
                          ORDER BY id ASC
                      ''')
    for jogo in listaDeUsuarios:
        print(f"""
            ID - {jogo[0]}
            Nome - {jogo[1]}
            """)
        
  escolhaMenuPrincipal = 1
  while escolhaMenuPrincipal != 0:
    escolhaMenuPrincipal = int(input("""
                        Escolha o que você deseja fazer:
                        1 - Manipular Jogos
                        2 - Manipular Usuarios
                        0 - Sair
                        """))
    match escolhaMenuPrincipal:
      case 1:
        escolhaMenuJogos = 1
        while escolhaMenuJogos !=0:
          escolhaMenuJogos = int(input("""
                                      Escolha o que você deseja fazer:
                                      1 - Inserir um novo Jogo
                                      2 - Visualizar dados deu um Jogo
                                      3 - Atualizar Jogo
                                      4 - Deletar Jogo
                                      0 - Voltar ao menu principal
                                      """))
          match escolhaMenuJogos:
            case 1:
              novoNome = input("Digite o nome do jogo: ")
              novaDuracao = input("Digite a duração do jogo: ")
              novoNumJogadores = input("Digite o número de jogadores do jogo: ")
              novaIdade = input("Digite a idade mínima do jogo: ")
              novaEditora = input("Digite a editora do jogo: ")
              
              novoJogo = Jogo(None, novoNome, novaDuracao,novoNumJogadores, novaIdade, novaEditora)
              con.manipularBanco(novoJogo.inserirJogo())
            case 2:
              mostrarJogos()
              
              escolhaVisualizar = int(input("Escolha pelo ID qual jogo você quer visualizar: "))
              jogoEscolhidoVisualizar = con.consultarBanco(buscarJogoEscolhido(escolhaVisualizar))
              
              novoJogoVisualizar = Jogo(jogoEscolhidoVisualizar[0][0], jogoEscolhidoVisualizar[0][1], jogoEscolhidoVisualizar[0][2], jogoEscolhidoVisualizar[0][3], jogoEscolhidoVisualizar[0][4], jogoEscolhidoVisualizar[0][5])
              
              novoJogoVisualizar.visualizarJogo()
            case 3:
              mostrarJogos()
              
              escolhaAtualizar = int(input("Escolha pelo ID qual jogo você quer atualizar: "))
              jogoEscolhidoAtualizar = con.consultarBanco(buscarJogoEscolhido(escolhaAtualizar))
              
              novoJogoAtualizar = Jogo(jogoEscolhidoAtualizar[0][0], jogoEscolhidoAtualizar[0][1], jogoEscolhidoAtualizar[0][2], jogoEscolhidoAtualizar[0][3], jogoEscolhidoAtualizar[0][4], jogoEscolhidoAtualizar[0][5])
              
              escolhaMenuAtualizar = int(input("""
                                              Escolha qual campo você deseja atualizar: 
                                              1 - Nome
                                              2 - Duração
                                              3 - Número de Jogadores
                                              4 - Idade Mínima
                                              5 - Editora
                                              """))
              match escolhaMenuAtualizar:
                case 1:
                  novoJogoAtualizar.setNome(input("Digite o novo nome: "))
                  con.manipularBanco(novoJogoAtualizar.atualizarJogo())
                case 2:
                  novoJogoAtualizar.setDuracao(input("Digite a nova duração: "))
                  con.manipularBanco(novoJogoAtualizar.atualizarJogo())
                case 3:
                  novoJogoAtualizar.setNumJogadores(input("Digite o novo número de jogadores: "))
                  con.manipularBanco(novoJogoAtualizar.atualizarJogo())
                case 4:
                  novoJogoAtualizar.setIdade(input("Digite a nova idade mínima: "))
                  con.manipularBanco(novoJogoAtualizar.atualizarJogo())
                case 5:
                  novoJogoAtualizar.setEditora(input("Digite a nova editora: "))
                  con.manipularBanco(novoJogoAtualizar.atualizarJogo())
            case 4: 
              mostrarJogos()
              escolhaDeletar = int(input("Escolha pelo ID qual jogo você quer deletar: "))
              jogoEscolhidoDeletar = con.consultarBanco(buscarJogoEscolhido(escolhaDeletar))
              
              novoJogoDeletar = Jogo(jogoEscolhidoDeletar[0][0], jogoEscolhidoDeletar[0][1], jogoEscolhidoDeletar[0][2], jogoEscolhidoDeletar[0][3], jogoEscolhidoDeletar[0][4], jogoEscolhidoDeletar[0][5])
              
              con.manipularBanco(novoJogoDeletar.deletarJogo())
      case 2:
        escolhaMenuUsuarios = 1
        while escolhaMenuUsuarios !=0:
          escolhaMenuUsuarios = int(input("""
                                      Escolha o que você deseja fazer:
                                      1 - Inserir um novo Usuário
                                      2 - Visualizar dados deu um Usuário
                                      3 - Atualizar Usuário
                                      4 - Deletar Usuário
                                      0 - Voltar ao menu principal
                                      """))
          match escolhaMenuUsuarios:
            case 1:
              novoNome = input("Digite o nome do usuário: ")
              novoCpf = input("Digite o CPF do usuário: ")
              novaData = input("Digite a data de nascimento do usuário: ")
              
              novoUsuario = Usuario(None, novoNome, novoCpf,novaData)
              con.manipularBanco(novoUsuario.inserirUsuario())
            case 2:
              mostrarUsuarios()
              
              escolhaVisualizarUsuarios = int(input("Escolha pelo ID qual usuário você quer visualizar: "))
              usuarioEscolhidoVisualizar = con.consultarBanco(buscarUsuarioEscolhido(escolhaVisualizarUsuarios))
              
              novoUsuarioVisualizar = Usuario(usuarioEscolhidoVisualizar[0][0], usuarioEscolhidoVisualizar[0][1], usuarioEscolhidoVisualizar[0][2], usuarioEscolhidoVisualizar[0][3])
              
              novoUsuarioVisualizar.visualizarUsuario()
            case 3:
              mostrarUsuarios()
              
              escolhaAtualizarUsuario = int(input("Escolha pelo ID qual usuário você quer atualizar: "))
              usuarioEscolhidoAtualizar = con.consultarBanco(buscarUsuarioEscolhido(escolhaAtualizarUsuario))
              
              novoUsuarioAtualizar = Usuario(usuarioEscolhidoAtualizar[0][0], usuarioEscolhidoAtualizar[0][1], usuarioEscolhidoAtualizar[0][2], usuarioEscolhidoAtualizar[0][3])
              
              escolhaMenuAtualizarUsuario = int(input("""
                                              Escolha qual campo você deseja atualizar: 
                                              1 - Nome
                                              2 - CPF
                                              3 - Data de nascimento
                                              """))
              match escolhaMenuAtualizarUsuario:
                case 1:
                  novoUsuarioAtualizar.setNome(input("Digite o novo nome: "))
                  con.manipularBanco(novoUsuarioAtualizar.atualizarJogo())
                case 2:
                  novoUsuarioAtualizar.setDuracao(input("Digite a nova duração: "))
                  con.manipularBanco(novoUsuarioAtualizar.atualizarJogo())
                case 3:
                  novoUsuarioAtualizar.setNumJogadores(input("Digite o novo número de jogadores: "))
                  con.manipularBanco(novoUsuarioAtualizar.atualizarJogo())
                case 4:
                  novoUsuarioAtualizar.setIdade(input("Digite a nova idade mínima: "))
                  con.manipularBanco(novoUsuarioAtualizar.atualizarJogo())
                case 5:
                  novoUsuarioAtualizar.setEditora(input("Digite a nova editora: "))
                  con.manipularBanco(novoUsuarioAtualizar.atualizarJogo())
            case 4:
              mostrarUsuarios()
              escolhaDeletarUsuario = int(input("Escolha pelo ID qual jogo você quer deletar: "))
              usuarioEscolhidoDeletar = con.consultarBanco(buscarUsuarioEscolhido(escolhaDeletarUsuario))
              
              novoUsuarioDeletar = Usuario(usuarioEscolhidoDeletar[0][0], usuarioEscolhidoDeletar[0][1], usuarioEscolhidoDeletar[0][2], usuarioEscolhidoDeletar[0][3])
              
              con.manipularBanco(novoUsuarioDeletar.deletarJogo())
except(Error) as error:
  print("Ocorreu um erro", error)