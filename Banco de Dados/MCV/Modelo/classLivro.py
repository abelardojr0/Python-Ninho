class Livro:
  def __init__(self, id, nome, paginas, data, idAutor):
    self.id = id
    self.nome = nome
    self.paginas = paginas
    self.data = data
    self.idAutor = idAutor
  
  def setNome(self, novoNome):
    self.nome = novoNome
  def getNome(self):
    return self.nome
  
  def setPaginas(self, novoPaginas):
    self.paginas = novoPaginas
  def getPaginas(self):
    return self.paginas
  
  def setData(self, novoData):
    self.data = novoData
  def getData(self):
    return self.data
  
  def setIdAutor(self, novoIdAutor):
    self.idAutor = novoIdAutor
  def getIdAutor(self):
    return self.idAutor
  
  def inserirLivro(self):
    query = (f'''
            INSERT INTO "livros" 
              VALUES (DEFAULT, '{self.nome}', '{self.paginas}', '{self.data}', '{self.idAutor}')
            ''')
    return query
  
  def selecionarLivro(self):
    print(f"""
          ID - {self.id}
          Nome - {self.nome}
          Páginas - {self.paginas}
          Data - {self.data}
          Autor - {self.idAutor}
          """)
  
  def atualizarLivro(self):
    query = (f'''
            UPDATE "livros"
            SET "nome" = '{self.nome}', "paginas" = '{self.paginas}', "lancamento" = '{self.data}'
            WHERE "id" = '{self.id}'
            ''')
    return query
  
  def deletarLivro(self):
    query = (f'''
            DELETE FROM "livros"
              WHERE "id" = {self.id}
            ''')
    return query