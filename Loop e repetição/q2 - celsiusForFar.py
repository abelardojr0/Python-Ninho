temperatura = (input("Digite a temperatura: "))
tipo = temperatura[-1]  # pega o último dvalor de um array
valor = int(temperatura[:-1])
convertido = 0
tipoConvertido = ""
siglaConvertido = ""
# pega todos o valores anteriores ao digitado ( nessa caso antes do último, ou seja, todos menos o último)

if tipo.upper() == "F":
    convertido = int(((valor - 32) * 5) / 9)
    tipoConvertido = "Celsius"
    siglaConvertido = "C"
elif tipo.upper() == "C":
    convertido = int((9 * valor) / 5 + 32)
    tipoConvertido = "Fahrenheit"
    siglaConvertido = "F"
else:
    print("Digite um temperatura válida, terminada em C se for Celsius (ex: 25C), ou em F se for Fahrenheit (ex: 69F")
    exit()

print(f"{temperatura} convertido para {tipoConvertido} fica: {convertido}{siglaConvertido}")
