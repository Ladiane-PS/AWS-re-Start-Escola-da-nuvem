# Exercício 1

# Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais,
# possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória. ​

import random  # Importa módulo para gerar valores aleatórios
import string  # Importa módulo para usar conjuntos de caracteres prontos

def gerar_senha(comprimento):
    if comprimento <= 0:
        return "Digite um número positivo"  # Se tamanho inválido, retorna mensagem

    conjunto_caracteres = string.printable  # Todos caracteres imprimíveis (letras, números, símbolos, espaços...)

    # Gera a senha aleatória escolhendo 'comprimento' caracteres do conjunto
    senha_aleatoria = ''.join(random.choice(conjunto_caracteres) for _ in range(comprimento))

    return senha_aleatoria  # Retorna a senha gerada

try:
    # Solicita ao usuário o tamanho da senha e converte para inteiro
    tamanho_senha = int(input("Informe o tamanho da senha desejada (número inteiro): "))

    # Chama a função para gerar a senha com o tamanho informado
    resultado = gerar_senha(tamanho_senha)

    print(resultado)  # Mostra a senha gerada ou mensagem de erro
except ValueError:
    # Caso o usuário digite algo que não seja número inteiro
    print("Erro: por favor, informe um número inteiro válido.")
