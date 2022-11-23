inicio = 0
proximo = 1
print(inicio)
while proximo < 50:
    print(proximo)
    anterior = inicio  # recebe o valor inicial
    inicio = proximo  # o valor inicial se torna o proximo
    proximo = anterior + proximo  # e o próximo se torna ele mesmo + o anterior
