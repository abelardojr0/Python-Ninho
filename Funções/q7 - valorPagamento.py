def valorPagamento(valor, atraso):
    valorFinal = 0
    if(atraso != 0):
        valorFinal = valor + (valor * 0.3)
        valorFinal = valorFinal + (0.01*atraso)
    return valorFinal
relatorio = []
prestacao = 1
while(prestacao !=0):
    prestacao = float(input("Digite o valor da prestação: "))
    if prestacao == 0:
        break
    else:
        atraso = float(input("Digite quantos dias de atraso: "))
    relatorio.append(valorPagamento(prestacao,atraso))
    
print(relatorio)
total = sum(relatorio)
print(f"Total: {total}")
