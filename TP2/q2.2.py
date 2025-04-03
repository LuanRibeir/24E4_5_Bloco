import random

class Estudante:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return f"{self.nome}: {self.nota}"

def quicksort_estudantes(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2].nota
    left = [x for x in arr if x.nota < pivot]
    middle = [x for x in arr if x.nota == pivot]
    right = [x for x in arr if x.nota > pivot]

    return quicksort_estudantes(left) + middle + quicksort_estudantes(right)

# Criando estudantes aleatórios
estudantes = [Estudante(f"Aluno {i}", random.randint(0, 100)) for i in range(10)]
print("Antes da ordenação:")
[print(e) for e in estudantes]

# Ordenando por nota
estudantes_ordenados = quicksort_estudantes(estudantes)
print("\nDepois da ordenação:")
[print(e) for e in estudantes_ordenados]


