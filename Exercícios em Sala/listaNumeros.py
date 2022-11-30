def receberLista(lista,inicio,fim):
    resposta = []
    for numero in lista:
        if numero >=  inicio and numero <= fim:
            resposta.append(numero)
    return resposta

print(receberLista([12,14,15,16,18,20,24,26,28,32,34,38], 13, 26))