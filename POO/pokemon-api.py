import json
import requests
import random

listaPokemon = [] # LISTA QUE VAI ARMAZENAR OS POKEMONS

# CRIANDO O POKEMON 
class Pokemon:
    def __init__(self,pokemon):
        self.nome = pokemon["name"]
        self.tipo = pokemon["types"][0]["type"]["name"]
        self.habilidade = pokemon["abilities"][0]["ability"]["name"]
        self.hp = pokemon["stats"][0]["base_stat"]
        self.ataque = pokemon["stats"][1]["base_stat"]
        self.defesa = pokemon["stats"][2]["base_stat"]
        self.ataqueEspecial = pokemon["stats"][3]["base_stat"]
        self.defesaEspecial = pokemon["stats"][4]["base_stat"]
        self.velocidade = pokemon["stats"][5]["base_stat"]
        self.altura = pokemon["height"]
        self.peso = pokemon["weight"]
        
        self.listaVantagens = json.loads(requests.get(pokemon["types"][0]["type"]["url"]).content)["damage_relations"]["double_damage_to"]
        self.vantagens = []
        for nome in self.listaVantagens:
            self.vantagens.append(nome["name"])
            
        self.listaDesvantagens = json.loads(requests.get(pokemon["types"][0]["type"]["url"]).content)["damage_relations"]["double_damage_from"]
        self.desvantagens = []
        for nome in self.listaDesvantagens:
            self.desvantagens.append(nome["name"])
        

#METODO DE EXIBIÇÃO DOS DADOS DO POKEMON
    def getPokemon(self):
        return f"""
    Nome: {self.nome}
    Vida: {self.hp}
    Tipo: {self.tipo}
    Habilidade: {self.habilidade}
    Ataque: {self.ataque}
    Defesa:{self.defesa}
    Ataque Especial: {self.ataqueEspecial}
    Defesa Especial: {self.defesaEspecial}
    Velocidade: {self.velocidade}
    Altura: {self.altura}
    Peso: {self.peso}
    Vantagens: {self.nomesVantagens}
    Desvantagens: {self.nomesDesvantagens}"""

#METODO DE ATAQUE
    def atacar(self):
            print(f"O Pokemon {self.nome} atacou usando {self.habilidade}")

#buscando na API
resultados = json.loads(requests.get("https://pokeapi.co/api/v2/pokemon?offset=0&limit=9").content)["results"]

#JEITO MAIS VERBOSO PARA QUE EU ENTENDA O PROCESSO.
# response = requests.get("https://pokeapi.co/api/v2/pokemon?offset=0&limit=9")
# arquivoJson = json.loads(response.content)
# resultados = arquivoJson["results"]

for item in resultados:   
    listaPokemon.append(Pokemon(json.loads(requests.get(item["url"]).content)))
    
    #JEITO MAIS VERBOSO PARA QUE EU ENTENDA O PROCESSO.
    # resposePokemon = requests.get(pokemon["url"])
    # pokemonJson = json.loads(resposePokemon.content) 
    #listaPokemon.append(pokemonJson)


#MOSTRAR OS DADOS DE TODOS OS POKEMONS
# for pokemon in listaPokemon:
#     print(pokemon.getPokemon())


def checarVantagens(vantagens, inimigo):
    vantagem = False
    if(inimigo.tipo in vantagens):
        vantagem = True
    return vantagem

def batalhaPokemon(pokemon1, pokemon2):
    [hp1,hp2] = [pokemon1.hp, pokemon2.hp]
    [cont1, cont2] = [0,0]

    vantagem1 = checarVantagens(pokemon1.vantagens, pokemon2)
    vantagem2 = checarVantagens(pokemon2.vantagens, pokemon1)
    modVantagem1 = 0
    modVantagem2 = 0
    
    if(vantagem1):
        modVantagem1 = 10
    if(vantagem2):
        modVantagem2 = 10

    while hp1 > 0 and hp2 >0:
        
            [tentativa1, tentativa2] = [random.random() - 0.5, random.random() - 0.5]
            
            if(tentativa1 > 0 and hp1 > 0):
                hp2 -= (pokemon1.ataque  - (pokemon2.defesa * 0.65)) + modVantagem1
                cont1+=1

                
            if(tentativa2 > 0 and hp2 > 0):
                hp1 -= (pokemon2.ataque  - (pokemon1.defesa * 0.65)) + modVantagem2
                cont2+=1
        
    if(hp1 <= 0 and hp2 > hp1):
        print(f"{pokemon2.nome} ganhou de {pokemon1.nome} e sobrou {round(hp2, 2)} pontos de vida")
    elif(hp2 <= 0 and hp1 > hp2):
        print(f"{pokemon1.nome} ganhou de {pokemon2.nome}  e sobrou {round(hp1, 2)} pontos de vida")
    else:
        print("Os pokemons empataram")
        
        
    print(f"O {pokemon1.nome} acertou {cont1} ataques")
    print(f"O {pokemon2.nome} acertou {cont2} ataques")
        
        
    
        
print("Lista de Pokemons:")

for i in range(len(listaPokemon)):
    print(f"{i}: {listaPokemon[i].nome} | HP: {listaPokemon[i].hp} | Ataque: {listaPokemon[i].ataque} | Defesa: {listaPokemon[i].defesa}")


pokemon1 = int(input("Escolha o primeiro pokemon digitando seu número: "))
pokemon2 = int(input("Escolha o segundo pokemon digitando seu número: "))

batalhaPokemon(listaPokemon[pokemon1],listaPokemon[pokemon2])

