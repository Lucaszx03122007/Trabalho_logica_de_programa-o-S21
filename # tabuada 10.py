# Solicita um número ao usuário
numero = int(input("Digite um número maior que 0: "))

# Verifica se o número é válido
if numero > 0:
    # Imprime a tabuada de 1 a 10
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Número inválido! Por favor, insira um número maior que 0.")
