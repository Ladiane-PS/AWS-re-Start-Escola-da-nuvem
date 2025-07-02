# Atividade 2

# Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente,
#  ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda "Não"
def is_palindromo(texto):
    # Remove espaços e pontuação, converte para minúsculas
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    # Compara o texto com sua versão invertida
    return texto_limpo == texto_limpo[::-1]

# Exemplo de uso
frase = "O lobo ama o bolo"
resultado = is_palindromo(frase)

resposta = "Sim" if resultado else "Não"

print(f"'{frase}' é um palíndromo? {resposta}")

