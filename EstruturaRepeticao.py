#Criando a lista de nomes
listaNomes = ["João", "Maria", "Pedro", "Ana", "Carlos"]

#Estrutura de repetição para cumprimentar cada pessoa da lista
for nome in listaNomes:
    print(f"Olá, {nome}!\nBem-vindo(a) ao curso de Python!")



indice = 0 # Começamos na posição 0 (João)

# Enquanto o índice for menor que o tamanho da lista (5)
while indice < len(listaNomes):
    nome = listaNomes[indice]
    print(f"Olá, {nome}!\nBem-vindo(a) ao curso de Python!!!!!!")
    
    indice += 1 # Adicionamos 1 ao índice para ir para o próximo nome na próxima rodada