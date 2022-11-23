import random

print("Tente advinhar o número que eu estou pensando")

numeros = []
for i in range(1, 10):
    numeros.append(i)
sorteado = random.choice(numeros)


numero = int(input("Digite um número de 1 a 9:  "))
if (numero == sorteado):
    print(
        f"Parabéns você advinhou! o número que eu estava pensando é o : {numero}")
else:
    while (numero != sorteado):
        numero = int(input("Digite um número de 1 a 9:  "))
        if (numero == sorteado):
            print(
                f"Parabéns você advinhou! o número que eu estava pensando é o : {numero}")
