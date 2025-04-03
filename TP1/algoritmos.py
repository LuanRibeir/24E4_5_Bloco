import time
import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):  # Número de passadas
        for j in range(n - 1 - i):  # Comparações até o último elemento não ordenado
            if lista[j] > lista[j + 1]:  # Se estiver fora de ordem, troca
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  

def selection_sort(arr):
    n = len(arr)
    for i in range(n):  # Percorre a lista
        min_index = i  # Assume que o menor elemento está na posição i
        for j in range(i + 1, n):  # Busca o menor elemento na parte não ordenada
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Troca os elementos

def insertion_sort(arr):
    for i in range(1, len(arr)):  # Começa do segundo elemento
        key = arr[i]  
        j = i - 1  
        while j >= 0 and key < arr[j]:  # Move os elementos maiores para frente
            arr[j + 1] = arr[j]  
            j -= 1
        arr[j + 1] = key  # Insere o elemento na posição correta

# Ler arquivo ls_out.txt
def ler_arquivo(caminho):
    with open(caminho, 'r') as f:
        return [linha.strip() for linha in f.readlines()]

# Medir o tempo de execução várias vezes e calcular média
def medir_tempo(func, arr, repeticoes=5):
    tempos = []
    for _ in range(repeticoes):
        copia_arr = arr[:]  # Evita modificar a lista original
        inicio = time.perf_counter()  # Medida mais precisa
        func(copia_arr)
        fim = time.perf_counter()
        tempos.append(fim - inicio)
    return np.mean(tempos), np.std(tempos)  # Retorna média e desvio padrão

# App (Testes e Execução)
if __name__ == "__main__":
    listagem = "ls_out.txt"
    arquivos = ler_arquivo(listagem)

    tamanhos = [1500, 3000, 4500, 6000, 7500, 9000, 10500]
    
    algoritmos = [("Bubble Sort", bubble_sort), 
                  ("Selection Sort", selection_sort), 
                  ("Insertion Sort", insertion_sort)]

    resultados = {algoritmo: ([], []) for algoritmo, _ in algoritmos}  # (médias, desvios)
    
    n_repeticoes = 5

    # Testar cada algoritmo para diferentes tamanhos 
    for tamanho in tamanhos:
        sublista = arquivos[:tamanho]
        for algoritmo, func in algoritmos:
            media, desvio = medir_tempo(func, sublista, n_repeticoes)
            
            resultados[algoritmo][0].append(media)
            resultados[algoritmo][1].append(desvio)
            
            print(f"{algoritmo} - Tamanho {tamanho}: {media:.6f} ± {desvio:.6f} segundos")
        print("")

    # Criar gráfico
    plt.figure(figsize=(10, 6))
    for algoritmo, (medias, desvios) in resultados.items():
        plt.errorbar(tamanhos, medias, yerr=desvios, marker='x', label=algoritmo, capsize=3)

    plt.title("Comparação de Algoritmos de Ordenação por Tamanho do Array")
    plt.xlabel("Tamanho do Array")
    plt.ylabel("Tempo Médio de Execução (segundos)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

