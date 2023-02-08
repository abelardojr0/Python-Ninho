class Autor:
  def __init__(self, id, nome):
    self.id = id
    self.nome = nome
  
  def setNome(self, novoNome):
    self.nome = novoNome
    
  def getNome(self):
    return self.nome
  
  def inserirAutor(self):
    query = (f'''
             INSERT INTO autores
              VALUES(default, '{self.nome}')
             ''')
    return query
  
  def atualizarAutor(self):
    query = (f'''
             UPDATE autores
              SET "nome" = '{self.nome}'
                WHERE "id" = '{self.id}'
             ''')
    return query
