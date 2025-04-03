import time
import random

def check_func_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start


def quicksort(arr, pivot_type="first"):
    if len(arr) <= 1:
        return arr

    if pivot_type == "first":
        pivot = arr[0]
    elif pivot_type == "last":
        pivot = arr[-1]
    elif pivot_type == "median":
        pivot = sorted([arr[0], arr[len(arr)//2], arr[-1]])[1]
    else:
        raise ValueError("Tipo de pivô inválido")

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left, pivot_type) + middle + quicksort(right, pivot_type)

# Gerando listas aleatórias de tamanhos diferentes
s = random.sample(range(1, 100001), 100000)
m = random.sample(range(1, 1000001), 1000000)
b = random.sample(range(1, 10000001), 10000000)

lists = [s, m, b]
sizes = [100000, 1000000, 10000000]

# Testando QuickSort Iterativo
for i, array in enumerate(lists):
    print(f"\nLista de Tamanho: {sizes[i]}")

    for pivot in ['last', 'first', 'median']:
        result, exec_time = check_func_time(quicksort, array, pivot)
        print(f"Tempo de execução (com pivô '{pivot}'): {exec_time:.5f} segundos")


