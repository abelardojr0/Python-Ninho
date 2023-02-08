class Usuario:
  def __init__(self, id, nome, cpf, anoNasc):
    self.id = id
    self.nome = nome
    self.cpf = cpf
    self.anoNasc = anoNasc
  
  def setNome(self, novoNome):
    self.nome = novoNome
  def getNome(self):
    return self.nome
  
  def setCpf(self, novoCpf):
    self.cpf = novoCpf
  def getCpf(self):
    return self.cpf
  
  def setAnoNasc(self, novoAnoNasc):
    self.anoNasc = novoAnoNasc
  def getAnoNasc(self):
    return self.anoNasc
  
  
  def inserirUsuario(self):
    query = (f'''
            INSERT INTO "usuarios"
              VALUES(DEFAULT, '{self.nome}','{self.cpf}', '{self.anoNasc}' )
            ''')
    return query
  
  def visualizarUsuario(self):
    print(f'''
          ID - {self.id}
          Nome - {self.nome}
          CPF - {self.cpf}
          Ano de Nascimento - {self.anoNasc}
          ''')
    
  def atualizarJogo(self):
    query = (f'''
            UPDATE "usuarios"
              SET "nome" = '{self.nome}',
                  "cpf" = '{self.cpf}',
                  "anonasc" = '{self.anoNasc}'
              WHERE "id" = '{self.id}'
            ''')
    return query
  
  def deletarJogo(self):
    query = (f'''
            DELETE FROM "usuarios"
              WHERE "id" = {self.id}
            ''')
    return query
  
