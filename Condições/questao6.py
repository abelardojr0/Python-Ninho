import math
numero = float(input("Digite um número: "))
if numero >= 0:
    raiz = math.sqrt(numero)
    print(f"Seu número é positivo e a raiz quadrada dele é: {raiz:.2f}")
else:
    print(numero**2)
