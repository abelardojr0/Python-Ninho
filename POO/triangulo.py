class Triangulo():
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
        
        
    def calcularPerimetro(self):
        self.perimetro = self.ladoA + self.ladoB + self.ladoC
        return self.perimetro
    
    
    def getMaiorLado(self):
        self.maiorLado = 0
        if(self.ladoA > self.ladoB and self.ladoA > self.ladoC):
            self.maiorLado = self.ladoA
        elif(self.ladoB > self.ladoA and self.ladoB > self.ladoC):
            self.maiorLado = self.ladoB
        elif(self.ladoC > self.ladoA and self.ladoC > self.ladoA):
            self.maiorLado = self.ladoC
        elif(self.ladoC == self.ladoA and self.ladoC == self.ladoA):
            self.maiorLado = False
        return self.maiorLado
    
    
triangulo1 = Triangulo(10,5,5)
print(triangulo1.calcularPerimetro())
print(triangulo1.getMaiorLado())