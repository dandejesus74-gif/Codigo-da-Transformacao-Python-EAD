# 2. Calcule a média de alunos
def calcular_media(notas):
    if len(notas) == 0:
        return 0
    
    media = sum(notas) / len(notas)
    print(f"Média calculada: {media:.2f}")
    
    if media >= 6.0:
        print("Situação: Aprovado!")
    else:
        print("Situação: Reprovado!")

# Exemplo de uso da função
notas_aluno = [7.5, 8.0, 6.0]
print(f"Notas do aluno: {notas_aluno}")
calcular_media(notas_aluno)