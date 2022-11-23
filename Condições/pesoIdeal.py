altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite o seu sexo F ou M: ")
peso = 0
if sexo == "F":
    peso = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é: {peso: .2f} KG")
elif sexo == "M":
    peso = (72.7 * altura) - 58
    print(f"Seu peso ideal é: {peso: .2f} KG")
else:
    print("Digite um sexo válido")
