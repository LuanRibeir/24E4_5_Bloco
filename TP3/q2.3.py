import multiprocessing
import time
import matplotlib.pyplot as plt

def eh_primo(n):
    # Verifica se um número é primo.
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos_parcial(intervalo):
    # Conta primos dentro de um intervalo.
    return sum(1 for n in intervalo if eh_primo(n))

def contar_primos_paralelo(limite, num_processos):
    tamanho = limite // num_processos
    intervalos = [range(i * tamanho, (i + 1) * tamanho) for i in range(num_processos)] # Divide o trabalho

    with multiprocessing.Pool(num_processos) as pool:
        resultados = pool.map(contar_primos_parcial, intervalos) # Conta primos em cada parte

    return sum(resultados) # Soma o total de primos encontrados

# Definindo intervalo
limite = 100000

# Tempo sequencial
inicio_seq = time.time()
contagem_seq = sum(1 for i in range(limite) if eh_primo(i))
tempo_seq = time.time() - inicio_seq
print(f"Primos Encontrados: {contagem_seq}")
print(f"Tempo de execução sequencial: {tempo_seq:.6f}s")

# Tempo paralelo
num_processos = multiprocessing.cpu_count()
inicio_par = time.time()
contagem_par = contar_primos_paralelo(limite, num_processos)
tempo_par = time.time() - inicio_par
print(f"Primos Encontrados: {contagem_par}")
print(f"Tempo de execução paralelo: {tempo_par:.6f}s")

# Exibindo gráfico
plt.bar(["Sequencial", "Paralela"], [tempo_seq, tempo_par], color=['red', 'blue'])
plt.ylabel("Tempo (s)")
plt.title("Contagem de Primos: Sequencial vs Paralela")
plt.show()

