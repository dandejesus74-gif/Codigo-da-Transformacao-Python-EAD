# Desafio Extra: Menu interativo de calculadora
while True:
    print("\n--- CALCULADORA ---")
    print("1. Soma")
    print("2. Subtração")
    print("3. Sair")
    
    opcao = input("Escolha uma opção (1, 2 ou 3): ")
    
    if opcao == '3':
        print("Saindo da calculadora. Até logo!")
        break
    
    if opcao in ('1', '2'):
        v1 = float(input("Digite o primeiro valor: "))
        v2 = float(input("Digite o segundo valor: "))
        
        if opcao == '1':
            resultado = v1 + v2
            print(f"Resultado da Soma: {v1} + {v2} = {resultado}")
        elif opcao == '2':
            resultado = v1 - v2
            print(f"Resultado da Subtração: {v1} - {v2} = {resultado}")
    else:
        print("Opção inválida! Por favor, escolha 1, 2 ou 3.")