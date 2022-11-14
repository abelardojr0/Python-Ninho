array1 = [8, 9, 7]
array2 = [4, 5, 6]
media1 = 0
media2 = 0
for i in range(0, len(array1)):
    media1 += array1[i] / len(array1)
    media2 += array2[i] / len(array1)
print("A média de 8,9 e 7 é: ", media1)
print("A média de 4,5 e 6 é: ", media2)
soma = media1 + media2
print("E a soma das médias é: ", soma)
