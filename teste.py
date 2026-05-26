# --- BANCO DE DADOS EM MEMÓRIA (Variáveis Globais) ---
# Estas listas e variáveis armazenam os dados do programa enquanto ele estiver rodando.

books = ["Game of Thrones", "O Senhor dos Anéis", "Harry Potter", "O Hobbit"] # Lista de livros do acervo
clients = [] # Lista vazia para armazenar clientes cadastrados
employees = ["Ana", "Bruno", "Carlos", "Diana", "Jeziel"] # Lista de funcionários padrão
administrators = [] # Lista vazia para armazenar usuários promovidos a administrador
donoEmpresa = "Eduardo" # Variável de texto (string) que define quem é o Dono (nível de acesso máximo)


# --- FUNÇÕES DO SISTEMA ---

def emploees():
    """
    Função de acesso nível 'Funcionário'.
    Permite visualizar e modificar a lista de livros (Adicionar, Deletar, Atualizar).
    """
    print("Acessando a área de funcionários...")
    # Captura a escolha do usuário e guarda na variável 'switch'
    switch = input("Digite o número da opção desejada:\n1 - Listar livros\n2 - Adicionar livro\n3 - Deletar livro\n4 - Atualizar livro\n5 - Voltar\nEscolha: ")
    
    if switch == "1":
        print("\nLista de livros:")
        for book in books: # Percorre cada item da lista 'books' e imprime na tela
            print(f"- {book}")
            
    elif switch == "2":
        name = input("Digite o nome do livro: ")
        books.append(name) # .append() adiciona o novo livro ao final da lista
        print("Livro adicionado com sucesso!")
        
    elif switch == "3":
        name = input("Digite o nome do livro que deseja deletar: ")
        if name in books: # Verifica se o livro digitado realmente existe na lista
            books.remove(name) # .remove() exclui o item específico da lista
            print("Livro deletado com sucesso!")
        else:
            print("Livro não encontrado.")
            
    elif switch == "4":
        name = input("Digite o nome do livro que deseja atualizar: ")
        if name in books:
            new_name = input("Digite o novo nome do livro: ")
            # .index() acha a posição do livro antigo na lista e o substitui pelo novo nome
            books[books.index(name)] = new_name 
            print("Livro atualizado com sucesso!")
        else:
            print("Livro não encontrado.")
            
    elif switch == "5":
        print("Voltando ao menu anterior...")


def employeesAdministration(nome_usuario):
    """
    Função de acesso nível 'Administrador' (também acessível ao Dono).
    Requer o parâmetro 'nome_usuario' para verificar quem está tentando acessar.
    Gerencia Clientes e outros Funcionários, além de ter atalho para Livros.
    """
    admin = False # Variável de controle (flag) que começa como Falsa
    admin_name = nome_usuario # Guarda o nome de quem chamou a função

    # Verifica se o usuário atual tem permissão para usar esta área
    if nome_usuario in administrators:
        admin = True
    elif nome_usuario == donoEmpresa:
        admin = True
        
    # Se a verificação acima for verdadeira (True), libera o acesso
    if admin:
        print(f"\nBem-vindo, administrador! {admin_name}")
        switch = input("Deseja acessar a administração? (s/n) ")
        if switch.lower() == "s": # .lower() garante que vai aceitar 'S' maiúsculo ou 's' minúsculo
            print("Acessando a administração...")
            case = input("Digite o número da opção desejada:\n1 - Clientes\n2 - Livros\n3 - Funcionários\n4 - Sair\nEscolha: ")
            
            # Sub-menu de Clientes
            if case == "1":
                case_clients = input("Digite o número da opção desejada:\n1 - Cadastrar cliente\n2 - Listar clientes\n3 - Atualizar cliente\n4 - Deletar cliente\n5 - Voltar\nEscolha: ")
                if case_clients == "1":
                    name = input("Digite o nome do cliente: ")
                    clients.append(name.capitalize()) # .capitalize() deixa a primeira letra maiúscula
                    print("Cliente cadastrado com sucesso!")
                elif case_clients == "2":
                    print("\nLista de clientes:")
                    for client in clients:
                        print(f"- {client}")
                elif case_clients == "3":
                    name = input("Digite o nome do cliente que deseja atualizar: ")
                    if name.capitalize() in clients:
                        new_name = input("Digite o novo nome do cliente: ")
                        clients[clients.index(name.capitalize())] = new_name.capitalize()
                        print("Cliente atualizado com sucesso!")
                    else:
                        print("Cliente não encontrado.")
                elif case_clients == "4":
                    name = input("Digite o nome do cliente que deseja deletar: ")
                    if name.capitalize() in clients:
                        clients.remove(name.capitalize())
                        print("Cliente deletado com sucesso!")
                    else:
                        print("Cliente não encontrado.")
                elif case_clients == "5":
                    print("Voltando ao menu anterior...")
                    
            # Sub-menu de Livros (chama a outra função)
            elif case == "2":
                emploees() 
                
            # Sub-menu de Funcionários
            elif case == "3":
                case_employees = input("Digite o número da opção desejada:\n1 - Cadastrar funcionário\n2 - Listar funcionários\n3 - Atualizar funcionário\n4 - Deletar funcionário\n5 - Voltar\nEscolha: ")
                if case_employees == "1":
                    name = input("Digite o nome do funcionário: ")
                    employees.append(name.capitalize())
                    print("Funcionário cadastrado com sucesso!")
                elif case_employees == "2":
                    print("\nLista de funcionários:")
                    for employee in employees:
                        print(f"- {employee}")
                elif case_employees == "3":
                    name = input("Digite o nome do funcionário que deseja atualizar: ")
                    if name.capitalize() in employees:
                        new_name = input("Digite o novo nome do funcionário: ")
                        employees[employees.index(name.capitalize())] = new_name.capitalize()
                        print("Funcionário atualizado com sucesso!")
                    else:
                        print("Funcionário não encontrado.")
                elif case_employees == "4":
                    name = input("Digite o nome do funcionário que deseja deletar: ")
                    # Regra de negócio: Impede que alguém delete um administrador ou o dono por aqui
                    if name.capitalize() in administrators or name.capitalize() == donoEmpresa:
                        print("Você não pode deletar um administrador/dono por aqui.")
                    elif name.capitalize() in employees:
                        employees.remove(name.capitalize())
                        print("Funcionário deletado com sucesso!")
                    else:
                        print("Funcionário não encontrado.")                       
                elif case_employees == "5":
                    print("Voltando ao menu anterior...")
            elif case == "4":
                print("Saindo da administração...")
    else:        
        print("Acesso negado. Você não é um administrador.")


def promo_administration():
    """
    Função de acesso exclusivo do 'Dono da Empresa'.
    Permite promover funcionários a administradores e gerenciar a lista de admins.
    """
    print(f"\nBem-vindo, dono da livraria: {donoEmpresa}")
    switch = input("Deseja acessar a administração de cargos? (s/n) ")
    if switch.lower() == "s":
        case = input("Digite o número da opção desejada:\n1 - Adicionar administrador\n2 - Listar administradores\n3 - Atualizar administrador\n4 - Deletar administrador\n5 - Função dos administradores\n6 - Voltar\nEscolha: ")
        
        if case == "1":
            name = input("Digite o nome do administrador: ")
            # Adiciona na lista de admins se não estiver lá
            if name.capitalize() not in administrators:
                administrators.append(name.capitalize())
            # Adiciona na lista de funcionários (pois todo admin é um funcionário)
            if name.capitalize() not in employees:
                employees.append(name.capitalize())
            print("Administrador adicionado com sucesso!")
            
        elif case == "2":
            print("\nLista de administradores:")
            for admin in administrators:
                print(f"- {admin}")
                
        elif case == "3":
            name = input("Digite o nome do administrador que deseja atualizar: ")
            if name.capitalize() in administrators:
                new_name = input("Digite o novo nome do administrador: ")
                # Atualiza o nome na lista de administradores
                administrators[administrators.index(name.capitalize())] = new_name.capitalize()
                # Atualiza o nome também na lista de funcionários para manter a consistência
                if name.capitalize() in employees:
                    employees[employees.index(name.capitalize())] = new_name.capitalize()
                print("Administrador atualizado com sucesso!")
            else:
                print("Administrador não encontrado.")
                
        elif case == "4":
            name = input("Digite o nome do administrador que deseja deletar: ")
            if name.capitalize() in administrators:
                administrators.remove(name.capitalize())
                # Se deletou o admin, ele também sai da lista de funcionários
                if name.capitalize() in employees:
                    employees.remove(name.capitalize())
                print("Administrador deletado com sucesso!")
            else:
                print("Administrador não encontrado.")
                
        elif case == "5":
            # Permite ao dono testar/usar as ferramentas do Administrador
            employeesAdministration(donoEmpresa) 
            
        elif case == "6":
            print("Voltando ao menu anterior...")  


# --- FLUXO PRINCIPAL DO PROGRAMA (LOOP) ---

# Solicita o login do usuário logo ao iniciar
user = input("Digite seu nome: ").capitalize() 
print(f"Bem-vindo à livraria, {user}!")

# Variável que mantém o programa rodando (True). Quando virar False, o programa encerra.
opcao = True 

# Loop infinito do sistema até que o usuário decida sair
while opcao:
    
    # ROTA 1: Acesso de Dono
    if user == donoEmpresa:
        print(f"\n[Menu do Dono - {user}]")
        variavel = input("O que deseja acessar?\n1 - Promoção de funcionário\n2 - Administração Geral\n3 - Sair\nEscolha: ")
        if variavel == "1":
            promo_administration()
        elif variavel == "2":
            employeesAdministration(user) 
        elif variavel == "3":
            print("Saindo do sistema...")
            opcao = False # Quebra o loop While
        else:
            print("Opção inválida. Tente novamente.")
            
    # ROTA 2: Acesso de Administrador
    elif user in administrators:
        print(f"\n[Menu de Administrador - {user}]")
        employeesAdministration(user) 
        # Pergunta se quer deslogar após usar a função
        if input("\nDeseja continuar no sistema? (s/n): ").lower() != 's':
            opcao = False
            
    # ROTA 3: Acesso de Funcionário
    elif user in employees:
        print(f"\n[Menu de Funcionário - {user}]")
        emploees()
        # Pergunta se quer deslogar após usar a função
        if input("\nDeseja continuar no sistema? (s/n): ").lower() != 's':
            opcao = False
            
    # ROTA 4: Acesso de Cliente (Nome não encontrado em nenhuma lista acima)
    else:
        print(f"\n[Menu do Cliente - {user}]")
        print("Menu de clientes em desenvolvimento. Volte logo!")
        opcao = False # Encerra o loop para clientes, pois ainda não há funcionalidades