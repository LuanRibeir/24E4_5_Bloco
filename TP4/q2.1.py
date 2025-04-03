class TrieNode:
    def __init__(self):
        self.filhos = {}  # Armazenar os filhos do nó
        self.fim_palavra = False  # Indica se o nó marca o fim de uma palavra

class Trie:
    def __init__(self):
        # Inicializa a Trie com um nó raiz vazio
        self.raiz = TrieNode()

    def inserir(self, palavra):
        node = self.raiz  # Começa a partir da raiz
        for char in palavra:
            # Se o caractere não existe nos filhos -> cria um novo nó
            if char not in node.filhos:
                node.filhos[char] = TrieNode()
            # Avança para o próximo nó
            node = node.filhos[char]
        # Marca o final da palavraa
        node.fim_palavra = True

    def exibir_trie(self, node=None, prefix=""):
        if node is None:
            node = self.raiz  # Começa a partir da raiz
        
        # Se o nó marca o fim de uma palavra, imprime o prefixo acumulado
        if node.fim_palavra:
            print(prefix)
        
        # Percorre todos os filhos do nó atual
        for letra, filho in node.filhos.items():
            # Chama recursivamente para cada filho, adicionando o caractere ao prefixo
            self.exibir_trie(filho, prefix + letra)

# Teste 
trie = Trie()

palavras = ["casa", "casamento", "casulo", "cachorro"]

for palavra in palavras:
    trie.inserir(palavra)

print("##### Palavras #####")
trie.exibir_trie()

