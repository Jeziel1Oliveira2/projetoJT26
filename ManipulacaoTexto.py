# --- DECLARAÇÃO DE VARIÁVEIS ---
# Atribuímos valores de texto (Strings). Lembre-se: o '=' é atribuição.
nome = "katia"
sobrenome = "gonçalves de paula"

# --- CONCATENAÇÃO ---
# Forma antiga: usando '+'. O " " é essencial para não "colar" as palavras.
nomeCompleto = nome + " " + sobrenome
print(f"Concatenação clássica: {nomeCompleto}")

# Forma moderna: F-Strings. Muito mais legível e profissional.
print(f"F-String: {nome} {sobrenome}")


# --- TRANSFORMAÇÃO DE TEXTO ---
# IMPORTANTE: Strings são imutáveis. O método não altera a original, 
# por isso precisamos reatribuir: nome = nome.upper()
nome = nome.upper()
print(f"Upper: {nome}")

nome = nome.lower()
print(f"Lower: {nome}")

nome = nome.capitalize()
print(f"Capitalize: {nome}")

nomeCompleto = nomeCompleto.title()
print(f"Title (Nomes próprios): {nomeCompleto}")

# --- LIMPEZA DE DADOS ---
# Remove espaços vazios antes ou depois do texto (muito usado em formulários).
nomeCompleto = nomeCompleto.strip()
print(f"Strip (limpo): {nomeCompleto}")

# --- MANIPULAÇÃO DE CONTEÚDO ---
# Substitui um trecho do texto por outro.
nomeCompleto = nomeCompleto.replace("Oliveira" , "Silva")
print(f"Replace: {nomeCompleto}")

# --- ANÁLISE DE DADOS ---
print(f"Contagem da letra 'i': {nomeCompleto.count('i')}")
print(f"Posição do primeiro 'i': {nomeCompleto.find('i')}")

# --- VALIDAÇÕES (Retornam Booleanos: True ou False) ---
print(f"Começa com 'j'? {nomeCompleto.startswith('j')}")
print(f"Termina com 'j'? {nomeCompleto.endswith('j')}")

# --- ESTRUTURA DE DADOS (Transformação) ---
# O .split() transforma a string em uma LISTA (quebra nos espaços).
lista_nome = nomeCompleto.split()
print(f"Lista gerada pelo split: {lista_nome}")

# O .join() faz o caminho inverso: junta itens da lista em uma única string.
nomeCompleto = " ".join(lista_nome)
print(f"Reconstruído com join: {nomeCompleto}")

# --- CHECAGEM DE TIPO ---
print(f"É só número? {nomeCompleto.isdigit()}")
print(f"É só letra? {nomeCompleto.isalpha()}")
print(f"É alfanumérico? {nomeCompleto.isalnum()}")
print(f"Está tudo minúsculo? {nomeCompleto.islower()}")
print(f"Está tudo maiúsculo? {nomeCompleto.isupper()}")