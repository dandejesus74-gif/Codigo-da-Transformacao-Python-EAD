'''
 Um bloco de comentarios.


Um Bloco de Comentarios

projeto hamburgeria


PO: (como dono do negocio: quero um sistema de vendas para a minha hamburgeria,
para que eu possa controlar as vendas e produtos.)

QA: (como cliente: quero um sistema de vendas para a minha hamburgeria para 
que eu possa comprar meus produtos favoritos de forma facil e rapido.)

Tech: (como programador: quero um sistema de vendas para a minha hamburgeria,
para que eu possa desenvolver um software eficiente e funcional para o negocio.)

Dev: (como programador quero um sistema de vendas para a minha hambuergeria
 para que eu possa implementar as funcionalidades necessarias para atender as 
 necessidades do negocio e dos clientes.)

UX: (como designer de experiencia do usuario: quero um sistema de vendas
 para a minha hambuergeria para que eu possa criar uma interface intuitiva e 
 agradavel para os usuarios, garantindo uma experiencia de compra satisfatoria.)

IA: (como analista de dados: quero um sistema de vendas para a minha hamburgeria,
para que eu possa coletar e analisar os dados de vendas, ajudando a identificar
padrões de consumo e otimizar as estrategias de marketing e estoque.)

'''

# isso é um comentario de linha unica
# print ('ola, mundo! ')



print('\n--------------------------------------------\n')

print ('🍔 ​sistema, hamburgueria🍔 ​')
 
print('\n--------------------------------------------\n')


p1_nome = p2_nome = p3_nome = ""
p1_estoque = p2_estoque = p3_estoque = 0
p1_preco = p2_preco = p3_preco = 0.0
p1_validade = p2_validade = p3_validade = ""
p1_descricao = p2_descricao = p3_descricao = ""

while True:
   
    
    print('❌apenas produtos!')
    print("\n== HAMBURGUERIA ==")
    print("1. Cardápio")
    print("2. Bebidas")
    print("3. Sobremesas")
    print("4. Combos")
    print("5. Cadastrar Produtos")
    print("6. Fazer Pedidos")
    print("7. Combo Infantil")
    print("8. Forma de Pagamento")
    print("9. Combo do Dia")
    print("10. Listar Produtos")
    print("0. Sair")
    print("-" * 50)

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        print("\nCARDÁPIO")
        print("- Hambúrguer de carne")
        print("- Hambúrguer de frango")
        print("- Hambúrguer vegetariano")
        print("- Hambúrguer vegano")
        print("- Batata frita")
        print("- Onion rings")
        print("- Salada")

        cardapio = input("\nDigite o hambúrguer ou acompanhamento desejado: ")
        print("Pedido realizado com sucesso!")

    elif opcao == "2":
        print("\nBEBIDAS")
        print("- Refrigerante")
        print("- Suco natural")
        print("- Água mineral")
        print("- Cerveja")

        bebidas = input("\nDigite a bebida desejada: ")
        print("Pedido realizado com sucesso!")

    elif opcao == "3":
        print("\nSOBREMESAS")
        print("- Milkshake")
        print("- Sorvete")
        print("- Brownie")
        print("- Pudim")

    elif opcao == "4":
        print("\nCOMBOS")
        print("- Combo 1: Hambúrguer + Batata frita + Refrigerante")
        print("- Combo 2: Hambúrguer + Onion rings + Suco natural")
        print("- Combo 3: Hambúrguer + Salada + Água mineral")

    elif opcao == "5":
        print("\nCADASTRO DE PRODUTOS")

        if p1_nome == "":
            p1_nome = input("Nome do produto: ")
            p1_estoque = int(input("Quantidade em estoque: "))
            p1_preco = float(input("Preço: R$ "))
            p1_validade = input("Validade: ")
            p1_descricao = input("Descrição: ")

            print(f"✅ Produto '{p1_nome}' cadastrado na vaga 1!")

        elif p2_nome == "":
            p2_nome = input("Nome do produto: ")
            p2_estoque = int(input("Quantidade em estoque: "))
            p2_preco = float(input("Preço: R$ "))
            p2_validade = input("Validade: ")
            p2_descricao = input("Descrição: ")

            print(f"✅ Produto '{p2_nome}' cadastrado na vaga 2!")

        elif p3_nome == "":
            p3_nome = input("Nome do produto: ")
            p3_estoque = int(input("Quantidade em estoque: "))
            p3_preco = float(input("Preço: R$ "))
            p3_validade = input("Validade: ")
            p3_descricao = input("Descrição: ")

            print(f"✅ Produto '{p3_nome}' cadastrado na vaga 3!")

        else:
            print("❌ Limite de 3 produtos atingido!")

    elif opcao == "6":
        print("\nFAZER PEDIDO")

        combo = input("Digite o número do combo desejado: ")
        pagamento = input("Digite a forma de pagamento: ")

        print("\nPedido realizado com sucesso!")
        print("Combo escolhido:", combo)
        print("Forma de pagamento:", pagamento)

    elif opcao == "7":
        print("\nCOMBO INFANTIL")
        print("- Combo Infantil 1: Hambúrguer de carne + Batata frita + Refrigerante")
        print("- Combo Infantil 2: Hambúrguer de frango + Onion rings + Suco natural")
        print("- Combo Infantil 3: Hambúrguer vegetariano + Salada + Água mineral")

        combo = input("Digite o número do combo infantil desejado: ")
        print("Pedido realizado com sucesso!")

    elif opcao == "8":
        print("\nFORMAS DE PAGAMENTO")
        print("- Dinheiro")
        print("- Cartão de Crédito")
        print("- Cartão de Débito")
        print("- Pix")

        pagamento = input("Escolha a forma de pagamento: ")
        print("Pagamento registrado com sucesso!")

    elif opcao == "9":
        print("\nCOMBO DO DIA")
        print("- Combo do Dia 1: Hambúrguer de carne + Batata frita + Refrigerante")
        print("- Combo do Dia 2: Hambúrguer de frango + Onion rings + Suco natural")
        print("- Combo do Dia 3: Hambúrguer vegetariano + Salada + Água mineral")

        combo_dia = input("Digite o combo desejado: ")
        print("Pedido realizado com sucesso!")

    elif opcao == "10":
        print("\nLISTA DE PRODUTOS")

        if p1_nome == "" and p2_nome == "" and p3_nome == "":
            print("Nenhum produto cadastrado.")

        else:
            if p1_nome != "":
                print(f"Nome: {p1_nome}")
                print(f"Preço: R$ {p1_preco:.2f}")
                print(f"Estoque: {p1_estoque}")
                print(f"Validade: {p1_validade}")
                print(f"Descrição: {p1_descricao}")
                print("-" * 30)

            if p2_nome != "":
                print(f"Nome: {p2_nome}")
                print(f"Preço: R$ {p2_preco:.2f}")
                print(f"Estoque: {p2_estoque}")
                print(f"Validade: {p2_validade}")
                print(f"Descrição: {p2_descricao}")
                print("-" * 30)

            if p3_nome != "":
                print(f"Nome: {p3_nome}")
                print(f"Preço: R$ {p3_preco:.2f}")
                print(f"Estoque: {p3_estoque}")
                print(f"Validade: {p3_validade}")
                print(f"Descrição: {p3_descricao}")
                print("-" * 30)


    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("❌ Opção inválida!")

    print("\n" + "-" * 50)

    
    
    
    
    
    
    
    
    
    
    
   