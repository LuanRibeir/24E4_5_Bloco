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

# Testando cm 10 listas e 5 valores diferentes de k
for i in range(10):
    lista = [random.randint(1, 1000) for _ in range(10000)]
    print(f"\nLista {i+1}:")
    for k in [1, 10, 100, 500, 1000]:  # Valores de k para testar
        resultado = quickselect(lista, k-1)  # Índices começam em 0
        print(f"{k}-ésimo menor elemento: {resultado}")

