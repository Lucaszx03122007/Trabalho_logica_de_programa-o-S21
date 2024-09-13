# Programa de validação de senha
senha_correta = "segura123"

while True:
    senha = input("Digite a senha: ")
    
    if senha == senha_correta:
        print("Acesso permitido")
        break
    else:
        print("Senha incorreta")