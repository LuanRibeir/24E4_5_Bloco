import heapq

def dijkstra(grafo, origem):
    # Dicionário para armazenar as distâncias mínimas
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[origem] = 0
    
    # Fila de prioridade (min-heap)
    fila_prioridade = [(0, origem)]
    
    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)
        
        # Se a distância atual já for maior, ignoramos
        if distancia_atual > distancias[vertice_atual]:
            continue
        
        for vizinho, peso in grafo[vertice_atual]:
            nova_distancia = distancia_atual + peso
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho))
    
    return distancias

# Exemplo de uso
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

vertice_origem = 'A'
caminhos_minimos = dijkstra(grafo, vertice_origem)

# Exibir resultados
for vertice, distancia in caminhos_minimos.items():
    print(f"Distância até {vertice}: {distancia}")

