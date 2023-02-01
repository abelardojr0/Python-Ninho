n1 = float(input("Digite a 1ª nota: "))
n2 = float(input("Digite a 2ª nota: "))
n3 = float(input("Digite a 3ª nota: "))
n4 = float(input("Digite a 4ª nota: "))
media = (n1 + n2 + n3 + n4)/4
if media >= 5:
    print(f"O aluno foi aprovado com a média {media:.2f}")
else:
    print(f"O aluno foi reprovado com a média {media:.2f}")
