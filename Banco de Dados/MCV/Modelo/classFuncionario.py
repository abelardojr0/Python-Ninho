class Funcionario:
  def __init__(self, id, nome, cpf, salario, id_Dept):
    self.id = id
    self.nome = nome
    self.cpf = cpf
    self.salario = salario
    self.id_Dept = id_Dept
        
  def imprimirFuncionario(self):
    print(f'''
          Informações do Funcionário:
          ID - {self.id}
          Nome - {self.nome}
          CPF - {self.cpf}
          Salário - {self.salario}
          ID_Departamento - {self.id_Dept}
          ''')
    
  def inserirFuncionario(self, tabela):
      query = f'''
        INSERT INTO "{tabela}"
        VALUES (default, '{self.nome}', '{self.cpf}','{self.salario}', '{self.id_Dept}')
        '''
      return query
  

  def atualizarFuncionario(self, tabela):
    query = (f'''
             UPDATE "{tabela}"
             SET "nome" = '{self.nome}', "cpf" = '{self.cpf}', "salário" = '{self.salario}'
             WHERE "id" = '{self.id}'
             ''')
    return query
  
  def atualizarDepartamentoFuncionario(self, tabela):
    query = (f'''
             UPDATE "{tabela}"
             SET "id_departamento" = '{self.id_Dept}'
             WHERE "id" = '{self.id_Dept}'
             ''')
    return query