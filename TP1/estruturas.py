import time
import tracemalloc
from collections import deque

# Ler a listagem do arquivo
def ler_arquivo(caminho):
    with open(caminho, 'r') as f:
        return [linha.strip() for linha in f.readlines()]

# Medir tempo e memória de execução
def medir_tempo_memoria(func, *args):
    tracemalloc.start()
    inicio = time.time()
    resultado = func(*args)
    fim = time.time()
    memoria_usada = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return resultado, fim - inicio, memoria_usada

# Funções para manipular estruturas
def manipular_hashtable(arquivos):
    hashtable = {i: arquivo for i, arquivo in enumerate(arquivos)}
    return hashtable

def manipular_pilha(arquivos):
    pilha = list(arquivos)
    return pilha

def manipular_fila(arquivos):
    fila = deque(arquivos)
    return fila

# Recuperar itens
def recuperar_itens(estrutura, posicoes):
    return [estrutura[p] if isinstance(estrutura, dict) else estrutura[p] for p in posicoes]


# Programa principal
if __name__ == "__main__":
    arquivo_listagem = "ls_out.txt"
    arquivos = ler_arquivo(arquivo_listagem)
    posicoes = [1, 100, 1000, 5000, len(arquivos) - 1]

    # Testar cada estrutura
    for nome, func in [("Hashtable", manipular_hashtable), 
                       ("Pilha", manipular_pilha), 
                       ("Fila", manipular_fila)]:
        estrutura, tempo, memoria = medir_tempo_memoria(func, arquivos)
        print(f"{nome}: Tempo para criação = {tempo:.6f}s, Memória usada = {memoria} bytes")
        
        # Recuperar itens
        itens, tempo_rec, memoria_rec = medir_tempo_memoria(recuperar_itens, estrutura, posicoes)
        print(f"{nome}: Recuperação = {tempo_rec:.6f}s, Memória usada = {memoria_rec} bytes\n")
        
    
    