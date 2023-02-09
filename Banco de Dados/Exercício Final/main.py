from Controle.Conexao import Conexao
from Modelo.Jogo import Jogo
from Modelo.Usuario import Usuario
from psycopg2 import Error

try:
  con = Conexao("Luderia", "postgres", "postgres", "localhost", "5432")
  
  def mostrarJogos():
    listaDeJogos = con.consultaCompleta("jogos")
    for jogo in listaDeJogos:
      print(f"""
            ID - {jogo[0]}
            Nome - {jogo[1]}
            """)
      
  def mostrarUsuarios():
    listaDeUsuarios = con.consultaCompleta("usuarios")
    for jogo in listaDeUsuarios:
        print(f"""
            ID - {jogo[0]}
            Nome - {jogo[1]}
            """)
        
  def criarObjeto(lista, tipo):        
    if tipo == "Jogo":
      objetoCriado = Jogo(lista[0][0], lista[0][1], lista[0][2], lista[0][3], lista[0][4], lista[0][5])
    elif tipo == "Usuario":
      objetoCriado = Usuario(lista[0][0], lista[0][1], lista[0][2], lista[0][3])
    return objetoCriado
      
        
  escolhaMenuPrincipal = input()
  while escolhaMenuPrincipal != 0:
    escolhaMenuPrincipal = int(input("""
                             MENU PRINCIPAL
                        Escolha o que você deseja fazer:
                        1 - Manipular Jogos
                        2 - Manipular Usuarios
                        0 - Sair
                        """))
    match escolhaMenuPrincipal:
      case 1:
        escolhaMenuJogos = input()
        while escolhaMenuJogos !=0:
          escolhaMenuJogos = int(input("""
                                             MENU DE JOGOS
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
              jogoEscolhidoVisualizar = con.consultarBanco(con.consultaPorId("jogos",escolhaVisualizar))
              novoJogoVisualizar = criarObjeto(jogoEscolhidoVisualizar, "Jogo")
              novoJogoVisualizar.visualizarJogo()
            case 3:
              mostrarJogos()
              
              escolhaAtualizar = int(input("Escolha pelo ID qual jogo você quer atualizar: "))
              jogoEscolhidoAtualizar = con.consultarBanco(con.consultaPorId("jogos",escolhaAtualizar))
              
              novoJogoAtualizar = criarObjeto(jogoEscolhidoAtualizar, "Jogo")
              
              escolhaMenuAtualizar = int(input("""
                                                MENU DE CAMPOS DE ALTERAÇÃO DE JOGOS
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
                case 2:
                  novoJogoAtualizar.setDuracao(input("Digite a nova duração: "))
                case 3:
                  novoJogoAtualizar.setNumJogadores(input("Digite o novo número de jogadores: "))
                case 4:
                  novoJogoAtualizar.setIdade(input("Digite a nova idade mínima: "))
                case 5:
                  novoJogoAtualizar.setEditora(input("Digite a nova editora: "))
                  
              con.manipularBanco(novoJogoAtualizar.atualizarJogo())
            case 4: 
              mostrarJogos()
              escolhaDeletar = int(input("Escolha pelo ID qual jogo você quer deletar: "))
              jogoEscolhidoDeletar = con.consultarBanco(con.consultaPorId("jogos",escolhaDeletar))
              
              novoJogoDeletar = criarObjeto(jogoEscolhidoDeletar, "Jogo")
              
              con.manipularBanco(novoJogoDeletar.deletarJogo())
      case 2:
        escolhaMenuUsuarios = input()
        while escolhaMenuUsuarios !=0:
          escolhaMenuUsuarios = int(input("""
                                          MENU DE USUÁRIOS
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
              usuarioEscolhidoVisualizar = con.consultarBanco(con.consultaPorId("usuarios",escolhaVisualizarUsuarios))
              
              novoUsuarioVisualizar = criarObjeto(usuarioEscolhidoVisualizar, "Usuario")
              
              novoUsuarioVisualizar.visualizarUsuario()
            case 3:
              mostrarUsuarios()
              
              escolhaAtualizarUsuario = int(input("Escolha pelo ID qual usuário você quer atualizar: "))
              usuarioEscolhidoAtualizar = con.consultarBanco(con.consultaPorId("usuarios",escolhaAtualizarUsuario))
              
              novoUsuarioAtualizar = criarObjeto(usuarioEscolhidoAtualizar, "Jogo")
              
              escolhaMenuAtualizarUsuario = int(input("""
                                               MENU DE CAMPOS DE ALTERAÇÃO DE USUÁRIOS
                                              Escolha qual campo você deseja atualizar: 
                                              1 - Nome
                                              2 - CPF
                                              3 - Data de nascimento
                                              """))
              match escolhaMenuAtualizarUsuario:
                case 1:
                  novoUsuarioAtualizar.setNome(input("Digite o novo nome: "))
                case 2:
                  novoUsuarioAtualizar.setDuracao(input("Digite a nova duração: "))
                case 3:
                  novoUsuarioAtualizar.setNumJogadores(input("Digite o novo número de jogadores: "))
                case 4:
                  novoUsuarioAtualizar.setIdade(input("Digite a nova idade mínima: "))
                case 5:
                  novoUsuarioAtualizar.setEditora(input("Digite a nova editora: "))
              con.manipularBanco(novoUsuarioAtualizar.atualizarJogo())
            case 4:
              mostrarUsuarios()
              escolhaDeletarUsuario = int(input("Escolha pelo ID qual jogo você quer deletar: "))
              usuarioEscolhidoDeletar = con.consultarBanco(con.consultaPorId("usuarios",escolhaDeletarUsuario))
              
              novoUsuarioDeletar = criarObjeto(usuarioEscolhidoDeletar, "Usuario")
              
              con.manipularBanco(novoUsuarioDeletar.deletarJogo())
except(Error) as error:
  print("Ocorreu um erro", error)