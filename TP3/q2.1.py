import multiprocessing
import time
import matplotlib.pyplot as plt

def soma_parcial(lista):
    # Calcula a soma de uma parte da lista
    return sum(lista)

def soma_paralela(lista, num_processos):
    # Divide a lista em partes e calcula a soma de cada uma em paralelo
    tamanho = len(lista)
    partes = [lista[i::num_processos] for i in range(num_processos)]  # Divide a lista em partes
    
    with multiprocessing.Pool(processes=num_processos) as pool:
        resultados = pool.map(soma_parcial, partes)  # Calcula a soma de cada parte

    return sum(resultados)  # Soma os resultados parciais

# Criando lista de 1 a 10 milhões
numeros = list(range(1, 10000001))

# Medindo tempo da soma sequencial
inicio_seq = time.time()
soma_seq = sum(numeros)
tempo_seq = time.time() - inicio_seq
print(f"Tempo de execução sequencial: {tempo_seq:.6f}s") 

# Medindo tempo da soma paralela
num_processos = multiprocessing.cpu_count()
print(num_processos)
inicio_par = time.time()
soma_par = soma_paralela(numeros, num_processos)
tempo_par = time.time() - inicio_par
print(f"Tempo de execução paralela: {tempo_par:.6f}s")

# Gráfico
plt.bar(["Sequencial", "Paralela"], [tempo_seq, tempo_par], color=['red', 'blue'])
plt.ylabel("Tempo (s)")
plt.title("Soma Sequencial vs Paralela")
plt.show()

