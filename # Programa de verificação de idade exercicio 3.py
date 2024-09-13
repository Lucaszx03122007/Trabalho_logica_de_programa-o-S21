# Programa de verificação de idade

while True:
    # Solicitar a idade da pessoa
    idade = int(input("Digite a idade da pessoa (ou -1 para parar): "))
    
    # Verifica se o usuário deseja encerrar
    if idade == -1:
        print("Encerrando o programa.")
        break
    
    # Estrutura de decisão composta para verificar a faixa etária
    if idade < 18:
        print("Menor de idade")
    elif idade < 60:
        print("Adulto")
    else:
        print("Idoso")
