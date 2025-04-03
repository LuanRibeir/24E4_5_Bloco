import numpy as np
import multiprocessing
import time
import matplotlib.pyplot as plt

def multiplica_linha(args):
    # Multiplica uma linha da matriz A pela matriz B e retorna o resultado
    i, A, B = args
    return [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]

def multiplicacao_paralela(A, B, num_processos):
    # Multiplica duas matrizes em paralelo, processando cada linha separadamente
    num_linhas = A.shape[0]
    with multiprocessing.Pool(processes=num_processos) as pool:
        C = pool.map(multiplica_linha, [(i, A, B) for i in range(num_linhas)])

    return np.array(C)  # Retorna a matriz resultante

# Criando matrizes 3x3
A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

# Exibindo resultado e gráfico
print("Matriz A:\n", A)
print("Matriz B:\n", B)

# Medindo tempo da multiplicação sequencial
inicio_seq = time.perf_counter()
C_seq = np.dot(A, B)
tempo_seq = time.perf_counter() - inicio_seq
print(f"Tempo de execução sequencial: {tempo_seq:.6f}s")
print("Matriz Resultado (Paralela):\n", C_seq)

# Medindo tempo da multiplicação paralela
num_processos = multiprocessing.cpu_count()
inicio_par = time.perf_counter()
C_par = multiplicacao_paralela(A, B, num_processos)
tempo_par = time.perf_counter() - inicio_par
print(f"Tempo de execução paralela: {tempo_par:.6f}s")
print("Matriz Resultado (Paralela):\n", C_par)

plt.bar(["Sequencial", "Paralela"], [tempo_seq, tempo_par], color=['red', 'blue'])
plt.ylabel("Tempo (s)")
plt.title("Multiplicação Sequencial vs Paralela")
plt.show()

