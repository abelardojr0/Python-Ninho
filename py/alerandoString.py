# texto = "Este é um texto"
# arryT = texto.split()
# arryT[0] = "este"
# texto = " ".join(arryT)
# print (texto)

# nome = input("Digite seu nome: ")

# lista = list(nome)
# lista.reverse()
# print("".join(lista))

# nomeTratado = nome.replace(" ", "")

# print(len(nomeTratado))

# from collections import Counter
# texto = input("Insira seu texto: ")
# print(Counter(texto))


inicio = 0
proximo = 1
print(inicio)
while proximo < 50:
    print(proximo)
    anterior = inicio  # recebe o valor inicial
    inicio = proximo  # o valor inicial se torna o proximo
    proximo = anterior + proximo  # e o próximo se torna ele mesmo + o anterior
