def menorNumero(arr):
    menor = arr[0]
    for num in arr:
        if (num < menor):
            menor = num
    return menor


print(menorNumero([10, 3, 1, 265, 25]))
