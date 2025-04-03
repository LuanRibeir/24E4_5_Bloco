import asyncio
import aiohttp
import time
import matplotlib.pyplot as plt

URLS = [
    "https://www.google.com",
    "https://www.python.org",
    "https://www.wikipedia.org",
    "https://www.youtube.com",
    "https://www.github.com"
] * 5 # Aumentar carga 

async def fetch(session, url, sem):
    async with sem:  # Limita o número de tarefas simultâneas
        async with session.get(url) as response:
            return await response.text()

async def download_all(urls, max_threads):
    sem = asyncio.Semaphore(max_threads)  
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url, sem) for url in urls]
        return await asyncio.gather(*tasks)

def medir_tempo_download(max_threads):
    inicio = time.time()
    asyncio.run(download_all(URLS, max_threads))
    fim = time.time()
    return fim - inicio

threads_testadas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # Variação de tarefas concorrentes
tempos = [medir_tempo_download(n) for n in threads_testadas]

# Gerando o gráfico
plt.plot(threads_testadas, tempos, marker='o', linestyle='-')
plt.xlabel("Número de Threads Assíncronas")
plt.ylabel("Tempo Total (s)")
plt.title("Tempo de Download Assíncrono vs. Número de Threads")
plt.grid()
plt.show()

