# 4- Verificador de Ano Bissexto

# Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não. 
# Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.


pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim'): ").lower()
    if entrada == "fim":
        break
    try:
        num = int(entrada)
        if num % 2 == 0:
            print("Par")
            pares += 1
        else:
            print("Ímpar")
            impares += 1
    except ValueError:
        print("Erro: entrada não é um número inteiro.")

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
