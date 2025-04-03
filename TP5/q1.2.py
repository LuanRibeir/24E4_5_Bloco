import heapq

def prim(grafo, inicio):
    # Lista para armazenar as arestas da MST (Árvore Geradora Mínima)
    mst = []

    # Conjunto de vértices visitados
    visitados = set([inicio])
    arestas = [(peso, inicio, vizinho) for vizinho, peso in grafo[inicio]]
    
    heapq.heapify(arestas)  # Transforma a lista em uma fila de prioridade
    
    while arestas:
        peso, origem, destino = heapq.heappop(arestas)
        if destino not in visitados:
            visitados.add(destino)
            mst.append((origem, destino, peso))
            for vizinho, peso in grafo[destino]:
                if vizinho not in visitados:
                    heapq.heappush(arestas, (peso, destino, vizinho))
    
    return mst

# Exemplo de uso
grafo = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 5)],
    'D': [('B', 4), ('C', 5)]
}

vertice_inicial = 'A'
resultado_mst = prim(grafo, vertice_inicial)

# Exibir resultados
for origem, destino, peso in resultado_mst:
    print(f"{origem} - {destino} com peso {peso}")
