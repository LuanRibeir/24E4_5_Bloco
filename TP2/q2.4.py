import random

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    if k < len(less):
        return quickselect(less, k)
    elif k < len(less) + len(equal):
        return pivot
    else:
        return quickselect(greater, k - len(less) - len(equal))


def encontrar_mediana(arr):
    n = len(arr)
    meio = n // 2
    if n % 2 == 1:
        return quickselect(arr, meio)
    else:
        return (quickselect(arr, meio - 1) + quickselect(arr, meio)) / 2

def encontrar_menor(arr, k):
    kth_smallest = quickselect(arr, k - 1)
    
    menores = [x for x in arr if x <= kth_smallest]
    
    return menores[:k]

# Teste
lista_teste = [random.randint(1, 1000) for _ in range(10)]
print(f"Lista Gerada: {lista_teste}")

# Encontrando a mediana
mediana = encontrar_mediana(lista_teste)
print(f"Mediana da lista: {mediana}")

# Encontrando os 10 menores elementos
k_menores = encontrar_menor(lista_teste, 4)
print(f"4 menores elementos: {k_menores}")

