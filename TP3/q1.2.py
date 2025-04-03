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

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        # Método auxiliar para remoção de um nó.
        if node is None:
            return node  # Retorna None se o nó não for encontrado

        if data < node.data:  # O valor está na subárvore esquerda
            node.left = self._delete(node.left, data)
        elif data > node.data:  # O valor está na subárvore direita
            node.right = self._delete(node.right, data)
        else:
            # Caso 1 -> Nó sem filhos
            if node.left is None and node.right is None:
                return None  # Remove o nó
            
            # Caso 2 -> Nó com apenas um filho
            if node.left is None:
                return node.right  # Retorna o filho direito
            elif node.right is None:
                return node.left  # Retorna o filho esquerdo

            # Caso 3 -> Nó com dois filhos
            min_larger_node = self._get_min(node.right)  # Encontra o sucessor in-order
            node.data = min_larger_node.data  # Substitui o valor do nó pelo sucessor
            node.right = self._delete(node.right, min_larger_node.data)  # Remove o sucessor

        return node

    def _get_min(self, node):
        # Encontra o menor valor da subárvore direita (sucessor in-order).
        current = node
        while current.left:
            current = current.left
        return current


# Teste

elements = [50, 30, 70, 20, 40, 60, 80]
bst = BinarySearchTree()
for elem in elements:
    bst.insert(elem)

print("In-order antes da remoção:", bst.inorder())

bst.delete(20)
print("In-order após remover 20:", bst.inorder())

bst.delete(30)
print("In-order após remover 30:", bst.inorder())

bst.delete(50)
print("In-order após remover 50:", bst.inorder())

def medir_tempo(func, *args):
    """Mede o tempo de execução de uma função."""
    inicio = time.time()
    resultado = func(*args)
    fim = time.time()
    return resultado, fim - inicio

# Gerando uma árvore grande com 10.000 elementos
valores_grandes = list(range(10000))
random.shuffle(valores_grandes)  # Embaralha os valores

bst_grande = BinarySearchTree()

# Mede o tempo de inserção
def inserir_elementos():
    for v in valores_grandes:
        bst_grande.insert(v)

_, tempo_insercao = medir_tempo(inserir_elementos)
print(f"\nTempo de inserção de 10.000 elementos: {tempo_insercao:.6f} segundos")

# Mede o tempo dos percursos
_, tempo_inorder = medir_tempo(bst_grande.inorder)
print(f"Tempo de percurso in-order: {tempo_inorder:.6f} segundos")

_, tempo_preorder = medir_tempo(bst_grande.preorder)
print(f"Tempo de percurso pre-order: {tempo_preorder:.6f} segundos")

_, tempo_postorder = medir_tempo(bst_grande.postorder)
print(f"Tempo de percurso post-order: {tempo_postorder:.6f} segundos")

