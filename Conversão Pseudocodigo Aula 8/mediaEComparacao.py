i = 0
soma = 0
arrayNotas = []
arrayMaiorMedia = []
while (i < 5):
    valor = float(input("Digite a nota: "))
    arrayNotas.append(valor)
    soma += valor
    i += 1
media = soma/5
print("A soma das notas é: ", soma)
print("A média das notas é: ", media)
print("Os valores maiores que a média são: ")
for i in range(0, 5):
    if (arrayNotas[i] > media):
        arrayMaiorMedia.append(arrayNotas[i])
print(arrayMaiorMedia)
