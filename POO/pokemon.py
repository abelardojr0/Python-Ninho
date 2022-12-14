import random
import json
import requests


Planta = {
    "vantagens": ["Terrestre", "Pedra","Água"],
    "desvantagens": ["Inseto", "Fogo", "Voador", "Gelo", "Venenoso"]
}

Fogo = {
    "vantagens": [ "Inseto", "Planta", "Gelo", "Aço"],
    "desvantagens": ["Pedra", "Terrestre", "Água"]
}



print(Fogo["vantagens"])

class Pokemon():
    def __init__(self, nome, evo1, evo2, tipo, vantagens, desvantagens, ataque, vida):
        self.nome = nome
        self.inicial = nome
        self.evolucao1 = evo1
        self.evolucao2 = evo2
        self.tipo = tipo
        self.vantagens = vantagens
        self.desvantagens = desvantagens
        self.ataque = ataque
        self.vida = vida
        self.estagio = 1
        
    def evoluir(self):
        self.ataque = self.ataque * 2
        self.vida += 10
        
        if(self.estagio == 1):
            self.estagio = 2
            print(f"O {self.nome} evoluiu para {self.evolucao1}")
            self.nome = self.evolucao1
        elif(self.estagio == 2):
            self.estagio = 3
            print(f"O {self.evolucao1} evoluiu para {self.evolucao2}")
            self.nome = self.evolucao2
            
    def imprimir(self):
        print(f"""
        Nome: {self.nome}
        Inicial: {self.inicial}
        Primeira Evolução: {self.evolucao1}
        Segunda Evolução: {self.evolucao2}
        Tipo: {self.tipo}
        Ataque: {self.ataque}
        Vida: {self.vida}""")
        
poke1 = Pokemon("Bulbasaur", "Ivysaur", "Venusaur","Planta", Planta["vantagens"], Planta["desvantagens"], 10, 60)
poke2 = Pokemon("Charmander", "Charmilion", "Charizard","Fogo", Fogo["vantagens"], Fogo["desvantagens"] , 12, 50)

poke1.evoluir()
poke1.imprimir()

def batalhaPokemon(pokemon1, pokemon2):
    hp1 = pokemon1.vida
    hp2 = pokemon2.vida
    cont1 = 0
    cont2 = 0
    print(pokemon1.tipo)
    while hp1 > 0 and hp2 >0:
        tentativa1 = random.random() - 0.5
        tentativa2 = random.random() - 0.5
        
        if(tentativa1 > 0 and hp1 > 0):
            hp2 -= pokemon1.ataque
            cont1+=1
            
        if(tentativa2 > 0 and hp2 > 0):
            hp1 -= pokemon2.ataque
            cont2+=1
            
        print(f"Vida do {pokemon1.nome} é: {hp1}")
        print(f"Vida do {pokemon2.nome} é: {hp2}")
        
        
    if(hp1 <= 0 and hp2 > hp1):
        print(f"{pokemon2.nome} ganhou de {pokemon1.nome} e sobrou {hp2} pontos de vida")
    elif(hp2 <= 0 and hp1 > hp2):
        print(f"{pokemon1.nome} ganhou de {pokemon2.nome}  e sobrou {hp1} pontos de vida")
    else:
        print("Os pokemons empataram")
        
        
    print(f"O {pokemon1.nome} acertou {cont1} ataques")
    print(f"O {pokemon2.nome} acertou {cont2} ataques")
        
        
        
batalhaPokemon(poke1,poke2)
