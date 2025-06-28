# Atividade 3

# Crie um programa que verifique se uma senha é forte.
# Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. 
# O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.

while True:
    senha = input("Digite uma senha ou 'sair' para terminar: ").lower()

    if senha == "sair":
        break
    if len(senha) < 8:
        print("Sua senha deve ter pelo menos 8 caracteres.")
        continue
    if not any(c.isdigit() for c in senha):
        print("Essa senha é fraca. Deve conter pelo menos um número.")
        continue

    print("Senha forte!")
    break
