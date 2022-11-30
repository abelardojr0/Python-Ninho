def potencializar(num1,num2):
    
    #usando for
    # resposta = 1
    # for i in range(1,num2+1):
    #     resposta *= num1
    
    #usando while
    # resposta = 1
    # while(num2 > 0):
    #     resposta *= num1
    #     num2 -= 1
    
    #usando operador lógico
    resposta = num1**num2
    
    return resposta
print(potencializar(2,10))