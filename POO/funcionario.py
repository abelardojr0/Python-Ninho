class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def aumentarSalario(self,porcentagem):
        self.salario = self.salario + (self.salario * (porcentagem /100))
        
        
funcionario1 = Funcionario("Abelardo", 3000)
print(funcionario1.salario)
funcionario1.aumentarSalario(10)
print(funcionario1.salario)