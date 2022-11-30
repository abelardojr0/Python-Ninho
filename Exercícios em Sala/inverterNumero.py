def inverterNumero(num):
    lista = []
    lista[:0] = str(num)
    lista.reverse()
    return "".join(lista)

print(inverterNumero(123))