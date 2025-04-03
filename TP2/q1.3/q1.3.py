import asyncio
import os
import time
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter

# Diret
INPUT_DIR = "imagens_input"
OUTPUT_DIR = "imagens_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

async def processar_imagem(filename, sem):
    # Aplica um filtro blur na imagem e salva o resultado
    async with sem:  # Controle de concorrência
        img = Image.open(os.path.join(INPUT_DIR, filename))
        img = img.filter(ImageFilter.BLUR)
        img.save(os.path.join(OUTPUT_DIR, filename))

async def processar_todas(max_threads):
    # Processa todas as imagens na pasta de entrada
    sem = asyncio.Semaphore(max_threads)  # Limita concorrência
    tasks = [processar_imagem(img, sem) for img in os.listdir(INPUT_DIR)]
    await asyncio.gather(*tasks)

def medir_tempo_processamento(max_threads):
    # Mede o tempo total de processamento para um numero específico de thread
    inicio = time.perf_counter()
    asyncio.run(processar_todas(max_threads))
    fim = time.perf_counter()
    return fim - inicio

# Variando o número de threads
threads_testadas = [1, 2, 4, 6, 8, 10, 12]
tempos = [medir_tempo_processamento(n) for n in threads_testadas]

# Gerando o gráfico
plt.figure(figsize=(8, 5))
plt.plot(threads_testadas, tempos, marker='o', linestyle='-', color='b', label="Tempo de processamento")
plt.xlabel("Número de Threads Assíncronas")
plt.ylabel("Tempo Total (s)")
plt.title("Tempo de Processamento de Imagens vs. Número de Threads")
plt.legend()
plt.grid()
plt.show()


