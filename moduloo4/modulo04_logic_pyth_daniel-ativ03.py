# 3. Separando pares e ímpares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 22]

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("--- NÚMEROS PARES E ÍMPARES ---")
print(f"Lista original: {numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")