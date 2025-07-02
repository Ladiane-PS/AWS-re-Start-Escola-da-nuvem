# Exercício 2

# Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. 
# O programa deve exibir o nome, email e país do usuário gerado."​

from faker import Faker  # Importa a biblioteca Faker para gerar dados falsos

fake = Faker("pt_BR")  # Define o local para gerar dados brasileiros

def gerar_usuario():
    nome = fake.name()       # Gera um nome aleatório
    email = fake.email()     # Gera um email aleatório
    pais = fake.country()    # Gera um país aleatório (pode ser fora do Brasil)

    # Monta uma string formatada com os dados do usuário
    user = f"""
    nome: {nome}
    email: {email}
    país: {pais}
    """

    return user  # Retorna a string com o perfil do usuário

usuario = gerar_usuario()  # Chama a função para criar o usuário
print(usuario)             # Exibe os dados gerados na tela
