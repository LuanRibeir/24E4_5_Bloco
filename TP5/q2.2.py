import math

class Ponto:
    def __init__(self, x, y, nome):
        self.x = x
        self.y = y
        self.nome = nome

    # Calcula a distancia euclidiana entre dois pontos
    def distancia(self, outro_ponto):
        return math.sqrt((outro_ponto.x - self.x) ** 2 + (outro_ponto.y - self.y) ** 2)

def resolver_tsp(lista_pontos):
    caminho = [lista_pontos[0]]  # Começa no primeiro ponto
    visitados = {lista_pontos[0].nome}  # Armazena nomes das cidades já visitadas
    atual = lista_pontos[0]

    while len(caminho) < len(lista_pontos):  # Continua até visitar todos os pontos
        # Encontra o ponto mais próximo que ainda não foi visitado
        proximo = min(
            (p for p in lista_pontos if p.nome not in visitados),  # Filtra os não visitados
            key=lambda p: atual.distancia(p)  # Escolhe ponto com a menor distância até o atual
        )

        caminho.append(proximo)  # Adiciona ao caminho
        visitados.add(proximo.nome)  # Marca como visitado
        atual = proximo  # Atualiza a posição atual

    return caminho  # Retorna a sequência de pontos percorridos

pontos = [
    Ponto(0, 0, "A"),
    Ponto(1, 5, "B"),
    Ponto(5, 2, "C"),
    Ponto(6, 6, "D"),
    Ponto(8, 3, "E")
]

rota = resolver_tsp(pontos)

print(" -> ".join(p.nome for p in rota))

