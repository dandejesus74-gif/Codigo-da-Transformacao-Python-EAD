# 3. Encontre o maior e o menor
def maior_menor(lista):
    if len(lista) == 0:
        return "A lista está vazia."
    
    maior = max(lista)
    menor = min(lista)
    
    return maior, menor

# Exemplo de uso da função
numeros = [10, 5, 83, 2, 45, 19]
maior_valor, menor_valor = maior_menor(numeros)

print(f"Lista de números: {numeros}")
print(f"O maior valor é: {maior_valor}")
print(f"O menor valor é: {menor_valor}")