import datetime
dataAtual = datetime.datetime.now()
data = dataAtual.date()
ano = data.year
anoNascimento = int(input("Digite sua data de nascimento: "))
idade = ano - anoNascimento
print("Sua idade é: ", idade)
if idade >= 18:
    nome = input("Digite seu nome: ")
    print(nome, "sua entrada foi permitida")
else:
    print("Como você é menor de 18 anos, sua entrada foi negada")
