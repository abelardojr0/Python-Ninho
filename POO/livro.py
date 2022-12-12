class Livro():
    def __init__(self, nome, qtdePaginas, autor, preco):
        self.nome = nome
        self.qtdePagina = qtdePaginas
        self.autor = autor
        self.preco = "R$" + str(preco)
        
    def getPreco(self):
        return self.preco
    
    def setPreco(self,novoPreco):
        self.preco = "R$" + str(novoPreco)
        return self.preco
        
livro1 = Livro("O senhor dos aneis", 352, "JRR Tolkien", 49.99)
print(livro1.getPreco())
livro1.setPreco("R$59,99")
print(livro1.getPreco())

