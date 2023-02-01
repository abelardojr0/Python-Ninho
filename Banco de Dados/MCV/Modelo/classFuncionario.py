class Funcionario:
  def __init__(self, id, nome, cpf):
    self.id = id
    self.nome = nome
    self.cpf = cpf
    
  def imprimirFuncionario(self):
    print(f'''
          Informações do Funcionário:
          ID - {self.id}
          Nome - {self.nome}
          CPF - {self.cpf}
          ''')
  def inserirFuncionario(self, tabela):
    query = (f'''
             INSERT INTO "{tabela}"
             VALUES (default, '{self.nome}', '{self.cpf}')
             ''')
    return query
    