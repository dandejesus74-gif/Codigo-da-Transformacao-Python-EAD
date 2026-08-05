# Desafio Extra: Agenda de contatos usando dicionários
agenda = {}

while True:
    print("\n--- AGENDA DE CONTATOS ---")
    print("1. Adicionar contato")
    print("2. Remover contato")
    print("3. Buscar contato")
    print("4. Listar todos os contatos")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        agenda[nome] = telefone
        print(f"Contato '{nome}' adicionado com sucesso!")
        
    elif opcao == '2':
        nome = input("Digite o nome do contato que deseja remover: ")
        if nome in agenda:
            del agenda[nome]
            print(f"Contato '{nome}' removido com sucesso!")
        else:
            print("Contato não encontrado na agenda.")
            
    elif opcao == '3':
        nome = input("Digite o nome do contato que deseja buscar: ")
        if nome in agenda:
            print(f"Contato encontrado -> Nome: {nome} | Telefone: {agenda[nome]}")
        else:
            print("Contato não encontrado.")
            
    elif opcao == '4':
        print("\n--- LISTA DE CONTATOS ---")
        if len(agenda) == 0:
            print("A agenda está vazia.")
        else:
            for nome, telefone in agenda.items():
                print(f"Nome: {nome} - Telefone: {telefone}")
                
    elif opcao == '5':
        print("Saindo da agenda de contatos. Até logo!")
        break
    else:
        print("Opção inválida! Escolha entre 1 e 5.")