class Colecao:
  def __init__(self, id, id_colecao, id_jogo ):
    self.id = id
    self.id_colecao = id_colecao
    self.id_jogo = id_jogo
    
  def inserirColecao(self):
    query = (f'''
             INSERT INTO colecao_jogos (id_colecao, id_jogo)
                                          VALUES('{self.id_colecao}', '{self.id_jogo}')
             ''')
    return query