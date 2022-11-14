maior = 0
for i in range(1, 4):
    num = float(input(f"Digite o {i} valor: "))
    if num > maior:
        maior = num
print(f"O maior valor digitado foi: {maior}")
