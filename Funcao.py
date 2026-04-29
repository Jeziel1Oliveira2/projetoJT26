def somar(a, b):
    return a + b

resultado = somar(5, 3)
print(f"O resultado da soma e: {resultado}")

def saudacao(nome):          # Cabeçalho: nome da função e parâmetro
    print(f"Olá, {nome}!")   # Corpo: o que a função faz

# Chamando a função
saudacao("Jeziel")           # Saída: Olá, Jeziel!

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Usando a função
meu_imc = calcular_imc(80, 1.80)
print(f"Seu IMC e: {meu_imc:.2f}")

