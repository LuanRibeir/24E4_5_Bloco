def permutacoes(s, passo=0):  
    if passo == len(s):  # Caso base -> chegou ao fim da permutação
        print("".join(s)) # Converte e imprime
        return

    for i in range(passo, len(s)):  # Troca cada caractere com o atual (passo)
        s[passo], s[i] = s[i], s[passo]
        permutacoes(s, passo + 1)  # Chamada recursiva para o proximo indice
        s[passo], s[i] = s[i], s[passo]  # Desfaz a troca para restaurar o estado original



string = "abcc"
print(f"Permutações de '{string}':")
permutacoes(list(string))

