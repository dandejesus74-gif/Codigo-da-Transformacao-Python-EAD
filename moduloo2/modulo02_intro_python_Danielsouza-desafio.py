


from datetime import datetime

# Solicita o nome do usuário
nome = input("Por favor, digite o seu nome: ")

# Obtém e formata a hora atual
agora = datetime.now()
hora_formatada = agora.strftime("%H:%M:%S")

# Exibe a mensagem
print(f"Olá, {nome}! Seja bem-vindo(a). Agora são {hora_formatada}.")