import time
import random

class BinarySearchTree:
    class Node:
        # Classe interna para representar um nó da árvore
        def __init__(self, data):
            self.data = data  # Valor do nó
            self.left = None   # Ponteiro para o filho esquerdo
            self.right = None  # Ponteiro para o filho direito

    def __init__(self):
        # Inicializa a árvore binária com a raiz vazia
        self.root = None  

    def insert(self, data):
        # Insere um novo valor na árvore
        if not self.root:
            # Se a árvore estiver vazia, cria a raiz
            self.root = self.Node(data)
        else:
            # Caso contrário, chama o método auxiliar para encontrar a posiçao correta
            self._insert(self.root, data)

    def _insert(self, node, data):
        # Método recursivo para inserir um valor na posição correta
        if data < node.data:  # Se o valor for menor, vai para a esquerda
            if node.left:
                self._insert(node.left, data)  # Continua descendo
            else:
                node.left = self.Node(data)  # Insere como filho esquerdo
        else:  # Se o valor for maior ou igual, vai para a direita
            if node.right:
                self._insert(node.right, data)  # Continua descendo
            else:
                node.right = self.Node(data)  # Insere como filho direito

    def inorder(self):
        # Retorna os elementos em ordem crescente (Esquerda -> Raiz -> Direita)
        result = []  # Lista para armazenar os valores ordenados
        self._inorder(self.root, result)  # Chama método auxiliar
        return result

    def _inorder(self, node, result):
        # Percorre a árvore em ordem crescente (esquerda -> raiz -> direita)
        if node:
            self._inorder(node.left, result)  # Visita a subárvore esquerda
            result.append(node.data)         # Adiciona o valor da raiz
            self._inorder(node.right, result) # Visita a subárvore direita

    def preorder(self):
        # Retorna os elementos na ordem pré-fixada (Raiz -> Esquerda -> Direita)
        result = []  # Lista para armazenar os valores
        self._preorder(self.root, result)  # Chama método auxiliar
        return result

    def _preorder(self, node, result):
        # Percorre a árvore na ordem (raiz -> esquerda -> direita)
        if node:
            result.append(node.data)         # Adiciona a raiz primeiro
            self._preorder(node.left, result)  # Visita a subárvore esquerda
            self._preorder(node.right, result) # Visita a subárvore direita

    def postorder(self):
        # Retorna os elementos na ordem pós-fixada (Esquerda -> Direita -> Raiz)
        result = []  # Lista para armazenar os valores
        self._postorder(self.root, result)  # Chama método auxiliar
        return result

    def _postorder(self, node, result):
        # Percorre a árvore na ordem (esquerda -> direita -> raiz)
        if node:
            self._postorder(node.left, result)  # Visita a subárvore esquerda
            self._postorder(node.right, result) # Visita a subárvore direita
            result.append(node.data)           # Adiciona a raiz por ultimo

def medir_tempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fim = time.time()
    return resultado, fim - inicio

# Testes
bst = BinarySearchTree()
elements = [50, 30, 70, 20, 40, 60, 80]

# Inserção dos elementos na árvore
for elem in elements:
    bst.insert(elem)

print(f"In-order: {bst.inorder()}")
print(f"Pre-order: {bst.preorder()}")
print(f"Post-order: {bst.postorder()}")

valores_grandes = list(range(10000))
random.shuffle(valores_grandes)       # Embaralha os valores

bst_grande = BinarySearchTree()

# Mede o tempo de inserção
def inserir_elementos():
    for v in valores_grandes:
        bst_grande.insert(v)

_, tempo_insercao = medir_tempo(inserir_elementos)
print(f"Tempo de inserção de 10.000 elementos: {tempo_insercao:.6f} segundos")

# Mede o tempo dos percursos
_, tempo_inorder = medir_tempo(bst_grande.inorder)
print(f"Tempo de percurso in-order: {tempo_inorder:.6f} segundos")

_, tempo_preorder = medir_tempo(bst_grande.preorder)
print(f"Tempo de percurso pre-order: {tempo_preorder:.6f} segundos")

_, tempo_postorder = medir_tempo(bst_grande.postorder)
print(f"Tempo de percurso post-order: {tempo_postorder:.6f} segundos")

