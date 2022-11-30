def converter(hora,minuto):
    resposta = f"{hora}:{minuto} A.M"
    if hora > 12:
        convertida = hora - 12
        resposta = f"{convertida}:{minuto} P.M"
    return resposta

sair = False

while(sair == False):
    
    hora = int(input("Digite a hora: "))
    while(hora>24):
        print("Digite uma hora válida, entre 1 e 24")
        hora = int(input("Digite a hora: "))
    
    minutos = int(input("Digite os minutos: "))
    while(minutos > 60):
        print("Digite minutos válidos, entre 1 e 60")
        minutos = int(input("Digite a minutos: "))
    if(minutos == 60):
        minutos = 0
        hora += 1
        print(hora)
        if hora == 24:
            hora = 0
    
    
    print(converter(hora,minutos))
    
    repetir = input("Você deseja digitar uma nova hora? (S/N)")
    if(repetir == "N" or repetir == "n"):
        sair = True
        
print("Volte sempre")