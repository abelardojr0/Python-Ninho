alfabeto = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
especiais = ("!","#",".","'","@","$","%","&","*","(",")","-","_","=","+","^","~",";",":","?","/", "|", '"',"£","¢","¬","§","ª","º","°","<",">","`",)
alfaMaiusculo = [letra.upper() for letra in alfabeto]

contNum = 0
contAlfa = 0
contEspec = 0
contMaiusc = 0

def comparaPalavras(n1,n2):
    global contNum
    global contAlfa
    global contEspec
    global contMaiusc
    if(len(n1) > len(n2)):
        for digito in n1:
            if digito in alfabeto:
                contAlfa += 1
            elif digito in especiais:
                contEspec +=1
            elif digito.isnumeric():
                contNum +=1
            elif digito in alfaMaiusculo:
                contMaiusc +=1
        print(f"A maior palavra é {n1}, e ela tem {len(n2)} dígitos nos quais:\n{contNum} são Números,\n{contAlfa} são minúsculos\n{contMaiusc} são maiúsculos\n{contEspec} são caracteres especiais.")
    elif(len(n2) > len(n1)):
        for digito in n2:
            if digito in alfabeto:
                contAlfa += 1
            elif digito in especiais:
                contEspec +=1
            elif digito.isnumeric():
                contNum +=1
            elif digito in alfaMaiusculo:
                contMaiusc +=1
        print(f"A maior palavra é {n2}, e ela tem {len(n2)} dígitos nos quais:\n{contNum} são Números,\n{contAlfa} são minúsculos\n{contMaiusc} são maiúsculos\n{contEspec} são caracteres especiais.")
        
    else:
        print(f"As duas palavras digitadas possuem o mesmo número de caracteres, {len(n1)}")
        
    
        
nome1 = input("Digite a primeira palavra: ")
nome2 = input("Digite a segunda palavra: ")

comparaPalavras(nome1,nome2)