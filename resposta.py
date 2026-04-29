# Ativiades sobre Manipulacao de texto:
#Respostas:
# 1  
nome = input("Digite seu nome completo: ")
print(f"Maiúsculas: {nome.upper()}")
print(f"Minúsculas: {nome.lower()}")
nomes_separados = nome.split()
print(f"Seu primeiro nome é: {nomes_separados[0]}")

# 2  
frase = input("Digite uma frase longa: ")
frase_nova = frase.replace("o", "0").replace("O", "0")
print(f"Frase modificada: {frase_nova}")
print(f"Total de caracteres: {len(frase)}")

#3
nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")
login = nome[:3].lower() + sobrenome[-3:].lower()
print(f"Seu login gerado é: {login}")


#------------------------------------------------------

# Ativiades sobre Manipulacao de numero:
#Respostas:
# 1  
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
print(f"Divisão Real: {n1 / n2}")
print(f"Divisão Inteira: {n1 // n2}")

# 2  
import math
num = float(input("Digite um número decimal (ex: 4.7): "))
print(f"Para cima: {math.ceil(num)}")
print(f"Para baixo: {math.floor(num)}")
print(f"Parte inteira (truncada): {math.trunc(num)}")

#3
import random
import math
minimo = int(input("Valor mínimo: "))
maximo = int(input("Valor máximo: "))
sorteado = random.randint(minimo, maximo)
raiz = math.sqrt(sorteado)
print(f"O número sorteado foi {sorteado} e sua raiz é {raiz:.2f}")


#------------------------------------------------------

# Ativiades sobre Manipulacao de listas:
#Respostas:
# 1  
cidades = ["São Paulo", "Rio de Janeiro", "Curitiba"]
nova_cidade = input("Digite mais uma cidade: ")
cidades.append(nova_cidade)
cidades.sort()
print(f"Cidades organizadas: {cidades}")

# 2  
numeros = [15, 42, 7, 88, 23]
print(f"Soma total: {sum(numeros)}")
print(f"Maior valor: {max(numeros)}")
print(f"Menor valor: {min(numeros)}")

#3
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))
notas = [n1, n2, n3, n4]
media = sum(notas) / len(notas)
notas.sort(reverse=True)
print(f"Média: {media:.2f}")
print(f"Notas do maior para o menor: {notas}")


#------------------------------------------------------

# Ativiades sobre funçoes:
#Respostas:
# 1  
def calcular_dobro(numero):
    return numero * 2

n = int(input("Digite um número: "))
print(f"O dobro é: {calcular_dobro(n)}")

# 2  
def formatar_preco(valor):
    return f"R$ {valor:.2f}"

produto = float(input("Qual o preço do produto? "))
print(f"O valor formatado é: {formatar_preco(produto)}")

#3
def gerar_estatistica(lista):
    total_itens = len(lista)
    soma_total = sum(lista)
    return total_itens, soma_total # Retorna dois valores

meus_numeros = [10, 20, 30, 40, 50]
quantidade, soma = gerar_estatistica(meus_numeros)
print(f"A lista tem {quantidade} números e a soma é {soma}.")