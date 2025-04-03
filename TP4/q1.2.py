class MinHeap:
    def __init__(self):
        # Inicializa uma heap vazia.
        self.heap = []

    def criar_heap(self, lista):
        # Transforma uma lista em uma min-heap usando heapify manual.
        self.heap = lista[:]
        for i in range(len(self.heap) // 2, -1, -1):
            self.heapify_down(i)

    def exibir_heap(self):
        # Retorna a heap em formato de lista.
        return self.heap

    def inserir_elemento(self, elemento):
        # Insere um novo elemento na heap e mantém a estrutura válida.
        print(f"Heap antes da inserção: {self.heap}")
        self.heap.append(elemento)
        self.heapify_up(len(self.heap) - 1)
        print(f"Heap após a inserção: {self.heap}")
    
    def heapify_up(self, index):
        # Corrige a heap subindo o elemento até a posição correta.
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def heapify_down(self, index):
        # Mantém a propriedade da heap ao descer um elemento.
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)
            

# Exemplo de uso
lista = [5, 2, 3, 7, 1]
heap = MinHeap()
heap.criar_heap(lista)
print("Heap criada:", heap.exibir_heap())

heap.inserir_elemento(0)
print("Heap final:", heap.exibir_heap())
