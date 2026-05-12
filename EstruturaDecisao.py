# 1. Nossa lista de pessoas autorizadas (Banco de dados)
autorizados = ["Jeziel", "Ana", "Marcos", "Beatriz"]

# 2. Entrada de dados do usuário
visitante = input("Digite seu nome para entrar: ")

# 3. Estrutura de Decisão verificando a Lista
if visitante in autorizados:
    # Se o nome estiver na lista, o acesso é permitido
    print(f"Acesso Permitido! Bem-vindo(a), {visitante}.")
    
elif visitante == "Admin":
    # Uma exceção: se não estiver na lista, mas for o Administrador
    print("Acesso de Administrador detectado. Abrindo todos os portões.")
    
else:
    # Se não estiver na lista e não for admin
    print("Acesso Negado. Seu nome não consta na lista de autorizados.")

# 4. Verificação extra usando funções de lista
print(f"\nExistem {len(autorizados)} pessoas autorizadas no momento.")