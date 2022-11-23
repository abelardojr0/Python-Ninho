fatorial = int(input("Digite o valor que você quer saber o fatorial: "))
resposta = 1
for i in range(1, fatorial+1):
    resposta *= i
print("O fatorial de ", fatorial, " é ", resposta)
