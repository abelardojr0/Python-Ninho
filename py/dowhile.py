meta = 5
cont = 0

while True:
    num = int(input("Digite um número: "))
    cont += 1
    if num == meta:
        print("Acertou")
        break
    if num != meta and cont == 5:
        break
