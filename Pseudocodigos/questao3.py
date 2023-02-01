salario = float(input("Digite seu salário: "))
prestacao = float(input("Digite o valro da prestação: "))
if prestacao > (0.2 * salario):
    print("Emprestimo não pode ser concedido")
else:
    print("Emprestimo pode ser concedido")
