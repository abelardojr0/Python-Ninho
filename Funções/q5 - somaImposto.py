def somaImposto(taxa,custo):
    taxaTratada = float(taxa[:-1])
    custoFinal = custo * (taxaTratada/100) + custo
    return custoFinal
print(somaImposto("13%", 200.5))