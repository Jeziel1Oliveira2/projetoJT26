primeiroNumero = 2
segundoNumero = 2
terceiroNumero = 2.5

# Operacoes basicas 
print(f"Soma: {primeiroNumero + segundoNumero}")
print(f"Subtracao: {primeiroNumero - segundoNumero}")
print(f"Multiplicacao: {primeiroNumero * segundoNumero}")
print(f"Divisao: {primeiroNumero / segundoNumero}")

# Operacoes especiais
print(f"Resto da divisao: {primeiroNumero % segundoNumero}")
print(f"Potencia (usando **): {primeiroNumero ** segundoNumero}")

import math
# Biblioteca Math
print(f"Raiz quadrada de {primeiroNumero}: {math.sqrt(primeiroNumero):.2f}")
print(f"Arredondamento para cima de {terceiroNumero}: {math.ceil(terceiroNumero)}")
print(f"Arredondamento para baixo de {terceiroNumero}: {math.floor(terceiroNumero)}")

# Exemplo corrigido de potencia com math.pow
print(f"Potencia (math.pow): {math.pow(terceiroNumero, 2)}")

# Formatacao para exibicao
valor = 10.5
print(f"Formatacao com F-string (duas casas): {valor:.2f}")

import random 

# Gera um numero inteiro entre o valor inicial e o final (inclusive).
dado = random.randint(1, 10)
print(f"Numero inteiro aleatorio: {dado}")

# A funcao random() retorna um valor float entre 0.0 e 1.0.
probabilidade = random.random()
print(f"Valor de probabilidade (0.0 a 1.0): {probabilidade:.2f}")

# Diferente do randint, o uniform gera numeros com virgula (float).
numeroDecimal = random.uniform(0, 10)
print(f"Numero decimal entre 0 e 10: {numeroDecimal:.2f}")

# Impotando a funcao criada 
from Funcao import calcular_imc

# Executando a  funcao
print(calcular_imc(80, 1.80))