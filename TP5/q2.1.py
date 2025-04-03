def mochila_gulosa(itens, capacidade):
    # Ordena os itens pela razão valor/peso em ordem decrescente
    itens.sort(key=lambda item: item[2] / item[1], reverse=True)
   
    # Inicializa a mochila e valor
    mochila = []
    peso_atual = 0
    valor_total = 0
    
    for nome, peso, valor in itens:
        # Adiciona item na mochila
        if peso_atual + peso <= capacidade:
            mochila.append(nome)
            peso_atual += peso
            valor_total += valor
    
    return mochila, valor_total

# Exemplo de uso
itens_disponiveis = [
    ("item1", 2, 40),
    ("item2", 3, 50),
    ("item3", 5, 100),
    ("item4", 4, 90)
]
capacidade_mochila = 8

itens_selecionados, valor_total = mochila_gulosa(itens_disponiveis, capacidade_mochila)

print("Itens selecionados:", itens_selecionados)
print("Valor total:", valor_total)
