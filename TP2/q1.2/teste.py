import numpy as np
import time
import sum_parallel

# Criando vetor aleatório
vetor = np.random.randint(1, 100000, size=10000, dtype=np.int32) # conversão: cython espera int32

# Teste sequencial
inicio = time.time()
resultado_seq = sum_parallel.soma_sequencial(vetor)
fim = time.time()
tempo_seq = fim - inicio

# Teste paralelo
inicio = time.time()
resultado_par = sum_parallel.soma_paralela(vetor)
fim = time.time()
tempo_par = fim - inicio

# Resultados
print(f"Soma Sequencial: {resultado_seq}, Tempo: {tempo_seq:.6f}s")
print(f"Soma Paralela: {resultado_par}, Tempo: {tempo_par:.6f}s")



