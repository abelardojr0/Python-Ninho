i = 0
maior = 0
print("Digite 0 para encerrar o programa")
valor = float(input("Digite um número positivo maior que zero: "))
while valor != 0:
    valor = float(input("Digite um número positivo maior que zero: "))
    if valor > maior:
        maior = valor
print("O maior valor digitado foi: ", maior)
