from Controle.Conexao import Conexao
from Modelo.Jogo import Jogo
from Modelo.Usuario import Usuario
from psycopg2 import Error

try:
  con = Conexao("Luderia", "postgres", "postgres", "localhost", "5432") #CRIANDO CONEXÃO COM O BANCO
  
  def mostrar(tipo): #FUNÇÃO PARA MOSTRAR ID E NOME DE UMA TABELA
    if tipo == "Jogos":
      lista = con.consultaCompleta("jogos") #CONSULTACOMPLETA É UMA FUNÇÃO QUE DA CLASS CONEXÃO QUE FAZ UM SELECT * EM UMA TABELA ORDENANDO POR ID.
    elif tipo == "Usuarios":
      lista = con.consultaCompleta("usuarios")
    for item in lista: #LOOP PARA MOSTRAR NO PRINT ID E NOME DOS CAMPOS CAPTURADOS PELA CONSULTA
      print(f"""
            ID - {item[0]}
            Nome - {item[1]}
            """)

  
  def criarObjeto(acao, tabela, tipo):
    escolha = int(input(f"Escolha pelo ID qual {tipo} você quer {acao}: "))  #RECEBO UM NÚMERO DA ESCOLHA
    opcaoEscolhida = con.consultarBanco(con.consultaPorId(tabela,escolha)) #ESSA VARIAVEL SERÁ UM ARRAY COM TODOS OS ITENS FILTRADOS DA CONSULTABANCO NA TABLEA "jogos" QUE TENHAM O ID QUE FOI DIGITADO ACIMA
    if tipo == "jogo": 
      objetoCriado = Jogo(opcaoEscolhida[0][0], opcaoEscolhida[0][1], opcaoEscolhida[0][2], opcaoEscolhida[0][3], opcaoEscolhida[0][4], opcaoEscolhida[0][5]) #CRIA UM OBJETO DA CLASSE JOGO, E PASSSA OS DADOS DA LISTA COMO PARAMETRO
    elif tipo == "usuario":
      objetoCriado = Usuario(opcaoEscolhida[0][0], opcaoEscolhida[0][1], opcaoEscolhida[0][2], opcaoEscolhida[0][3], opcaoEscolhida[0][4], opcaoEscolhida[0][5])  #CRIA UM OBJETO DA CLASSE USUARIO, E PASSSA OS DADOS DA LISTA COMO PARAMETRO
    # novoObjeto = criarObjeto(opcaoEscolhida, "Jogo") #POR FIM EU CRIO UM OBJETO PASSANDO O ARRAY E O TIPO DE OBJETO QUE ELE TEM QUE CRIAR
    return objetoCriado
  
  
  def gerarMenu(titulo, campos): #FUNÇÃO FEITA PARA GERAR MENUS DURANTE A APLICAÇÃO
    print(f"""      
        MENU {titulo}
Escolha o que você deseja fazer""") #PRINT APENAS DECORATIVO
    for i in range(len(campos)): #LOOP QUE VAI CRIAR OS CAMPOS DE ACORDO COM A LISTA PASSADA NA VARIAVEL CAMPOS
      print(f"{i+ 1} - {campos[i]}")
    print("0 - Sair") # INDEPENDENTE DO MENU, TODOS VÃO TER ESSA OPÇÃO 0 PARA SAIR
    escolhaMenuGerado = int(input("Digite o número da opção escolhida: ")) #INPUT QUE VAI GUARDAR A ESCOLHA DO USUÁRIO
    return escolhaMenuGerado #RETORNA JUSTAMENTE ESSE NÚMERO INTEIRO ESCOLHIDO
        
  escolhaMenuPrincipal = 1 #DECLARO A VARIAVEL COM UM NÚMERO ALEATÓRIO, APENAS PARA ESCAPAR DO WHILE
  while escolhaMenuPrincipal != 0: #LOOP QUE VAI SER EXECUTADO ATÉ O USUARIO DECIDIR SAIR DIGITANDO O NÚMERO ZERO
    escolhaMenuPrincipal = gerarMenu("PRINCIPAL", ["Manipular Jogos", "Manipular Usuários", "Manipular coleção"]) #VARIAVEL QUE IRÁ RETORNAR O MENU DE ESCOLHAS E A ESCOLHA DO USUARIO SERÁ SEU VALOR (INT)
    match escolhaMenuPrincipal:
      case 1: #CASO ELE ESCOLHA MANIPULAR OS JOGOS
        escolhaMenuJogos = 1 #MESMA TÁTICA PARA ESCAPAR DO WHILE
        while escolhaMenuJogos !=0: #MESMA TÁTICA DE LOOP
          escolhaMenuJogos = gerarMenu("DE JOGOS", ["Inserir novo jogo", "Visualizar jogo", "Atualizar jogo", "Deletar jogo"]) #CRIANDO OUTRO MENU, AGORA PARA OS JOGOS, A VARIAVEL VAI RETORNARU UM INT ASSIM COMO OS OUTROS.
          match escolhaMenuJogos:
            case 1: # INSERIR JOGO ---------------------------------------------------------------------------------------------------------------------------------------
              novoJogo = Jogo(None, input("Nome: "), input("Duração: "), input("Número de jogadores: "), input("Idade mínima: "), input("Editora: ")) #VARIÁVEL SERÁ UM OBJETO COM OS DADOS PASSADOS PELO INPUT
              con.manipularBanco(novoJogo.inserirJogo()) #MANIPULANDO O BANCO, PASSANDO A QUERY DE INSERT DECLARADA NO MÉTODO INSERIRJOGO NA CLASSE JOGO
              print("Jogo cadastrado com sucesso!")
            case 2: #VISUALIZAR JOGO ---------------------------------------------------------------------------------------------------------------------------------------
              mostrar("Jogos") #MOSTRA UMA LISTA COM TODOS OS JOGOS PRESENTES NO BANCO, COM ID E NOME
              novoObjeto = criarObjeto(acao="visualizar", tabela="jogos", tipo="jogo") #CRIO UM NOVO OBJETO, QUE VEM JUNTO COM UM INPUT PARA RECEBER O ID DO OBJETO, ENTÃO PASSO COMO PARAMETRO A AÇÃO QUE VAI SER PARTE DO TEXTO DO INPUT, QUAL TABELA ELE FARÁ A CONSULTA E QUAL TIPO DE OBJETO SE DEVE CRIAR
              novoObjeto.visualizarJogo() #MÉTODO DA CLASSE JOGO QUE IMPRIME OS DETALHES DO JOGO SELECIONADO
            case 3: #ATUALIZAR JOGO ---------------------------------------------------------------------------------------------------------------------------------------
              mostrar("Jogos") #MOSTRA UMA LISTA COM TODOS OS JOGOS PRESENTES NO BANCO, COM ID E NOME
              novoObjeto = criarObjeto(acao="atualizar", tabela="jogos", tipo="jogo") #CRIO UM NOVO OBJETO, QUE VEM JUNTO COM UM INPUT PARA RECEBER O ID DO OBJETO, ENTÃO PASSO COMO PARAMETRO A AÇÃO QUE VAI SER PARTE DO TEXTO DO INPUT, QUAL TABELA ELE FARÁ A CONSULTA E QUAL TIPO DE OBJETO SE DEVE CRIAR
              escolhaMenu = gerarMenu("DE CAMPOS", ["Nome", "Duração", "Número de Jogadores", "Idade Mínima", "Editora"]) #AQUI EU TO CRIANDO UM SUBMENU, PARA O USUÁRIO DECIDIR QUAL QUAL ELE QUER ALTERAR
              match escolhaMenu:
                case 1: #ALTERAR NOME
                  novoObjeto.setNome(input("Digite o novo nome: ")) #SETO NO OBJETO O NOVO NOME DIGITADO
                case 2: #ALTERAR DURAÇÃO
                  novoObjeto.setDuracao(input("Digite a nova duração: ")) #SETO NO OBJETO A NOVA DURAÇÃO DIGITADO
                case 3: #ALTERAR NÚMERO DE JOGADORES 
                  novoObjeto.setNumJogadores(input("Digite o novo número de jogadores: ")) #SETO NO OBJETO O NOVO NÚMERO DE JOGADORES DIGITADO
                case 4: #ALTERAR IDADE
                  novoObjeto.setIdade(input("Digite a nova idade mínima: ")) #SETO NO OBJETO A NOVA IDADE DIGITADO
                case 5: #ALTERAR EDITORA
                  novoObjeto.setEditora(input("Digite a nova editora: ")) #SETO NO OBJETO A NOVA EDITORA DIGITADO
              con.manipularBanco(novoObjeto.atualizarJogo()) #ATUALIZO O BANCO DE DADOS COM OS DADOS QUE FORAM ALTERADOS
              print("Jogo atualizado com sucesso!")
            case 4: #DELETAR JOGO ---------------------------------------------------------------------------------------------------------------------------------------
              mostrar("Jogos") #MOSTRA UMA LISTA COM TODOS OS JOGOS PRESENTES NO BANCO, COM ID E NOME
              novoObjeto = criarObjeto(acao="deletar", tabela="jogos", tipo="jogo") #CRIO UM NOVO OBJETO, QUE VEM JUNTO COM UM INPUT PARA RECEBER O ID DO OBJETO, ENTÃO PASSO COMO PARAMETRO A AÇÃO QUE VAI SER PARTE DO TEXTO DO INPUT, QUAL TABELA ELE FARÁ A CONSULTA E QUAL TIPO DE OBJETO SE DEVE CRIAR
              con.manipularBanco(novoObjeto.deletarJogo()) #DELETO O OBJETO SELECIONADO   
              print("Jogo deletado com sucesso!")
              
      case 2: #MANIPULANDO USUÁRIO (TODOS OS PROCEDIMENTOS AQUI EM BAIXO SÃO IGUAIS AOS DO CRUD ACIMA POR ISSO NÃO ESTÃO COMENTADOS)
        escolhaMenuUsuarios = 1
        while escolhaMenuUsuarios !=0:
          escolhaMenuUsuarios = gerarMenu("DE USUÁRIOS", ["Inserir novo usuário", "Visualizar usuário", "Atualizar usuário", "Deletar usuário"])
          match escolhaMenuUsuarios:
            case 1:
              novoUsuario = Usuario(None, input("Nome: "), input("CPF: "),input("Data de nascimento: "), input("Login: "), input("Senha: "))
              con.manipularBanco(novoUsuario.inserirUsuario())
              print("Usuário cadastrado com sucesso!")
            case 2:
              mostrar("Usuarios")
              novoObjeto = criarObjeto(acao="visualizar", tabela="usuarios", tipo="usuario")
              novoObjeto.visualizarUsuario()
            case 3:
              mostrar("Usuarios")
              novoObjeto = criarObjeto(acao="atualizar", tabela="usuarios", tipo="usuario")
              escolhaMenu = gerarMenu("DE CAMPOS", ["Nome", "CPF", "Data de nascimento", "Login", "Senha"])
              match escolhaMenu:
                case 1:
                  novoObjeto.setNome(input("Digite o novo nome: "))
                case 2:
                  novoObjeto.setCpf(input("Digite a nova CPF: "))
                case 3:
                  novoObjeto.setAnoNasc(input("Digite a nova Data de Nascimento: "))
                case 4:
                  novoObjeto.setLogin(input("Digite o novo login: "))
                case 5:
                  novoObjeto.setSenha(input("Digite a nova senha: "))
              con.manipularBanco(novoObjeto.atualizarUsuario())
              print("Usuário atualizado com sucesso!")
            case 4:
              mostrar("Usuarios")
              novoObjeto = criarObjeto(acao="deletar", tabela="usuarios", tipo="usuario")
              con.manipularBanco(novoObjeto.deletarUsuario())
              print("Usuário deletado com sucesso!")

        
except(Error) as error:
  print("Ocorreu um erro", error)