palavra = input("Digite uma palavra: ")
inverso = []
for i in palavra:
    inverso.append(i)
inverso.reverse()
print("".join(inverso))
