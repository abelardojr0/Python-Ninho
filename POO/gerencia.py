class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        
    def getNome(self):
        return self.nome
    def setNome(self,novoNome):
        self.nome = novoNome
        
    def getCpf(self):
        return self.cpf
    def setCpf(self,novoCpf):
        self.cpf = novoCpf   
        
    def getSalario(self):
        return self.salario
    def setSalario(self,novoSalario):
        self.salario = novoSalario   
        
class Gerente(Funcionario):
    
    def __init__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._listaFuncionarios = []
    
    
    def removerFuncionario(self):
        nomeFuncionario = input("Digite o nome do funcionario que você quer remover: ")
        senha = input("Digite a senha do gerente: ")
        
        if(senha == self._senha):
            for i in range(len(self._listaFuncionarios)):
                if self._listaFuncionarios[i].nome == nomeFuncionario:
                    self._listaFuncionarios.pop(i)
                    print(f"Funcionario {nomeFuncionario} removido")
                    return
                
                
    def adicionarFuncionario(self, funcionario):
        senha = input("Digite a senha: ")
        if senha == self._senha:
            self._listaFuncionarios.append(funcionario)
            print(f"Você adicionou o funcionario {funcionario.nome}")
        else:
            print("Senha incorreta")
            
            
    def getListaFuncionarios(self):
        listaNomes = []
        for nome in self._listaFuncionarios:
            listaNomes.append(nome.nome)
        return listaNomes

if __name__ == "__main__":
    gerente = Gerente("Abelardo", "111.111.111-11", 3000, "1234")

    funcionario1 = Funcionario("José", "000.000.000-00", 1500)
    funcionario2 = Funcionario("João", "000.000.000-00", 1500)
    funcionario3 = Funcionario("Pedro", "000.000.000-00", 1500)
    
    gerente.adicionarFuncionario(funcionario1)
    gerente.adicionarFuncionario(funcionario2)
    gerente.adicionarFuncionario(funcionario3)
    
    gerente.removerFuncionario()
    
    print(gerente.getListaFuncionarios())
    
        