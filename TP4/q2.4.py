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

    def buscar(self, palavra):
        # Inicia a busca a partir da raiz da Trie
        node = self.raiz
        for char in palavra:
            # Se o caractere não estiver nos filhos do nó atual -> a palavra não existe
            if char not in node.filhos:
                return False
            # Avança para o próximo nó
            node = node.filhos[char]
        # Retorna True se o nó final marca o fim é válida
        return node.fim_palavra

    def _auto_ajuda(self, node, prefixo, resultados):
        # Se o nó atual marca o fim de uma palavra -> adiciona ao resultado
        if node.fim_palavra:
            resultados.append(prefixo)
        # Percorre todos os filhos do nó atual
        for char, filho in node.filhos.items():
            # Continua a busca recursivamente, adicionando o caractere ao prefixo
            self._auto_ajuda(filho, prefixo + char, resultados)

    def autocomplete(self, prefixo):
        node = self.raiz
        for char in prefixo:
            # Se um caractere do prefixo não está na Trie, retorna lista vazia
            if char not in node.filhos:
                return []
            # Avança para o próximo nó
            node = node.filhos[char]
    
        # Lista para armazenar as palavras correspondentes ao prefixo
        resultados = []
        # Chama a função auxiliar para encontrar todas as palavras que começam com o prefixo
        self._auto_ajuda(node, prefixo, resultados)
        return resultados

    def remover(self, palavra):
        def _remover(node, palavra, index):
            # Caso base: se chegamos ao final da palavra
            if index == len(palavra):
                # Se a palavra não existe no Trie, retorna False
                if not node.fim_palavra:
                    return False
                # Desmarca o fim da palavra
                node.fim_palavra = False
                # Se o nó não tem filhos -> pode ser removido
                return len(node.filhos) == 0
            
            char = palavra[index]  # Obtém o caractere atual
            # Se o caractere não está nos filhos, a palavra não existe
            if char not in node.filhos:
                return False
            
            # Chama recursivamente para o próximo caractere
            pode_apagar = _remover(node.filhos[char], palavra, index + 1)

            # Se o nó pode ser apagado (não forma outras palavras) -> remove da árvore
            if pode_apagar:
                del node.filhos[char]
                # Retorna True se o nó atual não for fim de outra palavra e não tiver outros filhos
                return len(node.filhos) == 0

            return False  # Mantém a estrutura caso o nó ainda seja necessário

        _remover(self.raiz, palavra, 0)  # Inicia a remoção a partir da raiz do Trie



# Teste 
trie = Trie()

palavras = ["casa", "casamento", "casulo", "cachorro"]
busca = "casa"
prefixo = "cas"

for palavra in palavras:
    trie.inserir(palavra)

print("##### Palavras #####")
trie.exibir_trie()

print(f"\n##### Busca #####\nA palavra '{busca}' existe: {trie.buscar(busca)}")

print(f"\n##### Autocomplete #####\nAutocomplete para '{prefixo}':", trie.autocomplete(prefixo))

print(f"\n##### Remover #####\nRemover '{busca}'")
trie.remover(busca)
print(f"##### Busca #####\nA palavra '{busca}' existe: {trie.buscar(busca)}")
print(f"##### Autocomplete #####\nAutocomplete para '{prefixo}':", trie.autocomplete(prefixo))
