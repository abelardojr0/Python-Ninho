num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 == num2:
    print("Os dois números são iguais")
else:
    print("Os dois números são diferentes")
if num1 > num2:
    print(f"O primeiro valor {num1} é maior")
    print(f"O segundo valor {num2} é menor")
elif num2 > num1:
    print(f"O segundo valor {num2} é maior")
    print(f"O primeiro valor {num1} é menor")
