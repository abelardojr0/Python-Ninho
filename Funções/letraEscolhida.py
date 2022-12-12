def letraEscolhida(palavra,letra):
    if(letra in palavra):
        print("Existe")
    else:
        print("Não existe")
        
palavra = input("Digite uma palavra: ")
letra = input("Digite a letra: ")

letraEscolhida(palavra,letra)