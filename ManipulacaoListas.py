#Lista de nomes
listaNome = ["Joao", 'Claudio', "Ana", "Beto", "Caio"]

listaNome.append("Maria") # Adiciona "Maria" ao final da lista
listaNome.sort()          # Organiza os nomes em ordem alfabetica
totalNomes = len(listaNome) # Armazena a quantidade de itens (6)

 
podio = listaNome[:3]     # Extrai os 3 primeiros (indices 0, 1 e 2)
ultimos = listaNome[-2:]   # Extrai os 2 ultimos da lista

#Lista de numeros
listaNumeros = [2, 3, 5, 6, 2, 7]

listaNumeros.insert(0, 1)  # Insere o numero 1 na posicao inicial (indice 0)
listaNumeros.index(2)      # Retorna a primeira posicao onde o numero 2 aparece
listaNumeros.count(2)      # Conta quantas vezes o numero 2 existe na lista
listaNumeros.reverse()     # Inverte a ordem atual dos elementos
listaNumeros.sort()        # Reorganiza em ordem crescente

# Funcoes Matematicas
max(listaNumeros)          # Retorna o maior valor (7)
min(listaNumeros)          # Retorna o menor valor (1)
sum(listaNumeros)          # Soma todos os elementos da lista

#Lista de variaveis
variavelUm = "um"
variavelDois = "dois"
variavelTres = 'tres'

listaVariaveis = [variavelUm, variavelDois, variavelTres]
listaVariaveis.pop(2)      # Remove o item da posicao 2 (variavelTres)

#Lista misturada
listaMisturada = [variavelUm, False, 2, "Ana"]

listaMisturada.remove(False) # Remove o valor booleano 'False' da lista
listaMisturada.clear()       # Remove todos os itens, deixando a lista vazia []