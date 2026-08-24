import random
import math


def jogar():
    limite_inferior = 1
    limite_superior = 24
    max_tentativas = 6
    
    # 🎲 Escolhe o número secreto dentro do limite
    numero_secreto = random.randint(limite_inferior, limite_superior)
    
    print("=== JOGO DA ADIVINHAÇÃO ===")
    print(f"Tente adivinhar o número entre {limite_inferior} e {limite_superior}.")
    print(f"Você tem {max_tentativas} tentativas!\n")

    tentativas = 0
    while tentativas < max_tentativas:
        # 🛡️ Tratamento para evitar erro se digitarem letras
        try:
            palpite = int(input(f"Tentativa {tentativas + 1}: Digite seu palpite: "))
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números inteiros.\n")
            continue

        # ⚠️ Validação para não aceitar números fora de 1 a 24
        if palpite < limite_inferior or palpite > limite_superior:
            print(f"❌ Palpite fora do limite! Digite entre {limite_inferior} e {limite_superior}.\n")
            continue

        tentativas += 1

        # 🏆 Verificação do palpite
        if palpite == numero_secreto:
            print(f"🎉 Parabéns! Você acertou em {tentativas} tentativa(s)!")
            break
        elif palpite < numero_secreto:
            print("💡 O número secreto é MAIOR.\n")
        else:
            print("💡 O número secreto é MENOR.\n")
    else:
        print(f"☠️ Fim de jogo! O número secreto era {numero_secreto}.")

if __name__ == "__main__":
    jogar()