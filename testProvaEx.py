import pandas as pd

# 1. Carregar o arquivo
# O Classroom costuma colocar informações extras nas primeiras linhas, 
# se o erro 'ParserError' ocorrer, tente adicionar skiprows=1 ou 2.
try:
    df = pd.read_csv('notas_baixadas.csv')
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")
    exit()

# 2. Organizar os Nomes (O Classroom separa Nome e Sobrenome)
# Vamos criar uma coluna única 'Nome Completo' para facilitar
if 'Nome' in df.columns and 'Sobrenome' in df.columns:
    df['Nome Completo'] = df['Nome'] + ' ' + df['Sobrenome']
else:
    # Caso o arquivo já tenha uma coluna 'Nome' completa
    df['Nome Completo'] = df.get('Nome', 'Estudante Sem Nome')

# 3. Tratar a coluna de Nota
# O Classroom pode exportar notas como texto ou com nomes de colunas específicos
# Substitua 'Pontuação total' pelo nome exato que aparecer no seu CSV
coluna_nota = 'Pontuação total' 

# Garantir que as notas sejam números (converte erros em NaN e depois para 0)
df[coluna_nota] = pd.to_numeric(df[coluna_nota], errors='coerce').fillna(0)

# 4. Aplicar a Regra de Negócio (70% de 135 = 94.5)
df['Status Final'] = df[coluna_nota].apply(lambda x: 'APROVADO' if x >= 94.5 else 'REPROVADO')

# 5. Selecionar apenas o que interessa para o Excel final
df_final = df[['Nome Completo', coluna_nota, 'Status Final']]

# 6. Exportar para Excel
df_final.to_excel('Resultado_Final_Estudantes.xlsx', index=False)

print("Relatório gerado com sucesso!")