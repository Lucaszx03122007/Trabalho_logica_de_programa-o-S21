import random

# Computador escolhe um número aleatório entre 1 e 50
numero_secreto = random.randint(1, 50)

tentativas = 5  # Número de tentativas permitidas

print("Bem-vindo ao jogo de adivinhação!")
print("Eu escolhi um número entre 1 e 50. Você tem 5 tentativas para adivinhar.")

# Laço de repetição para as 5 tentativas
for tentativa in range(1, tentativas + 1):
    palpite = int(input(f"Tentativa {tentativa}: Digite o seu palpite: "))
    
    # Verifica se o palpite está correto
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break
    elif palpite < numero_secreto:
        print("O número é maior que o seu palpite.")
    else:
        print("O número é menor que o seu palpite.")
    
    # Verifica se acabaram as tentativas
    if tentativa == tentativas:
        print(f"Suas tentativas acabaram. O número era {numero_secreto}.")
