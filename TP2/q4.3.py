import matplotlib.pyplot as plt
import time

def hanoi(n, origem, destino, auxiliar):
    if n == 1:
        return
    hanoi(n - 1, origem, auxiliar, destino)
    hanoi(n - 1, auxiliar, destino, origem)

num_discos = list(range(1, 31))
tempos = []

for n in num_discos:
    inicio = time.time()
    hanoi(n, 'A', 'C', 'B')
    fim = time.time()
    tempos.append(fim - inicio)
    print(f"Discos: {n} Tempo: {fim-inicio:.7f}")

# Criando o gráfico
plt.figure(figsize=(10, 5))
plt.plot(num_discos, tempos, marker='o', linestyle='-', color='b', label="Tempo de execução")
plt.xlabel("Número de Discos")
plt.ylabel("Tempo (segundos)")
plt.title("Tempo de Execução das Torres de Hanói (1 a 30 discos)")
plt.legend()
plt.grid(True)
plt.show()

