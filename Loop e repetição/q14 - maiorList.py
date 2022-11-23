def maiorNumero(arr):
    maior = 0
    for num in arr:
        if (num > maior):
            maior = num
    return maior


print(maiorNumero([10, 3, 265, 1, 25]))
