salario = float(input("Digite o valor do salário: "))
financiamento = float(input("Digite o valor do financiamento pretendido: "))
if financiamento <= 5 * salario:
    print("Financiamento concedido, obrigado por nos consultar")
else:
    print("Financiamento negado, obrigado por nos consultar")
