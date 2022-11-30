def nVezes(n):
    resultado = []
    for i in range(1,n+1):
        resultado.append(f"{i} "*i)
    return resultado

print(nVezes(8))