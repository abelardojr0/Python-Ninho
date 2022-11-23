inicio = int(input("Digite o primeiro número do intervalo: "))
fim = int(input("Digite o último número do intervalo: "))
contPar = 0
contImpar = 0
for i in range(inicio, fim + 1):
    if i % 2 == 0:
        contPar += 1
    else:
        contImpar += 1
print(f"Quantidade de números pares: {contPar}")
print(f"Quantidade de números impares: {contImpar}")
