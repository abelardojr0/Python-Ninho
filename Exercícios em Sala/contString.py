from collections import Counter
def contString(string):
    contando = Counter(string.lower())
    letraA = contando["a"]
    return letraA
print(contString("Abelardo"))