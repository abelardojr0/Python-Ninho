import json
import requests
import random


class Pokemon():
    def __init__(self,pokemon):
        resposePokemon = requests.get(pokemon["url"])
        pokemonJson = json.loads(resposePokemon.content)
        
        self.nome = pokemon["name"]
        self.tipo = pokemonJson["types"][0]["type"]["name"]
        self.hp = pokemonJson["stats"][0]["base_stat"]
        self.ataque = pokemonJson["stats"][1]["base_stat"]
        self.defesa = pokemonJson["stats"][2]["base_stat"]
        self.ataqueEspecial = pokemonJson["stats"][3]["base_stat"]
        self.defesaEspecial = pokemonJson["stats"][4]["base_stat"]
        self.velocidade = pokemonJson["stats"][5]["base_stat"]
        self.altura = pokemonJson["height"]
        self.peso = pokemonJson["weight"]
        
    def getPokemon(self):
        return f"""
    Nome: {self.nome}
    Vida: {self.hp}
    Tipo: {self.tipo}
    Ataque: {self.ataque}
    Defesa:{self.defesa}
    Ataque Especial: {self.ataqueEspecial}
    Defesa Especial: {self.defesaEspecial}
    Velocidade: {self.velocidade}
    Altura: {self.altura}
    Peso: {self.peso}"""

response = requests.get("https://pokeapi.co/api/v2/pokemon?offset=0&limit=9")
arquivoJson = json.loads(response.content)
resultados = arquivoJson["results"]
listaPokemon = []

for item in resultados:
    novoPokemon = Pokemon(item)
    listaPokemon.append(novoPokemon)


# for pokemon in listaPokemon:
#     print(pokemon.getPokemon())



def batalhaPokemon(pokemon1, pokemon2):
    hp1 = pokemon1.hp
    hp2 = pokemon2.hp
    cont1 = 0
    cont2 = 0


    while hp1 > 0 and hp2 >0:
        tentativa1 = random.random() - 0.5
        tentativa2 = random.random() - 0.5
        print(tentativa1)
        print(tentativa2)
        if(tentativa1 > 0 and hp1 > 0):
            hp2 -= pokemon1.ataque - (pokemon1.ataque * 0.8)
            cont1+=1
            
        if(tentativa2 > 0 and hp2 > 0):
            hp1 -= pokemon2.ataque  - (pokemon2.ataque * 0.8)
            cont2+=1
            
        # print(f"Vida do {pokemon1.nome} é: {round(hp1, 2)}")
        # print(f"Vida do {pokemon2.nome} é: {round(hp2, 2)}")
        
        
    if(hp1 <= 0 and hp2 > hp1):
        print(f"{pokemon2.nome} ganhou de {pokemon1.nome} e sobrou {round(hp2, 2)} pontos de vida")
    elif(hp2 <= 0 and hp1 > hp2):
        print(f"{pokemon1.nome} ganhou de {pokemon2.nome}  e sobrou {round(hp1, 2)} pontos de vida")
    else:
        print("Os pokemons empataram")
        
        
    print(f"O {pokemon1.nome} acertou {cont1} ataques")
    print(f"O {pokemon2.nome} acertou {cont2} ataques")
        
        
        
batalhaPokemon(listaPokemon[1],listaPokemon[4])