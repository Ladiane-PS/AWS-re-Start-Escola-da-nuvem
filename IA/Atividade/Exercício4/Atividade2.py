# Atividade 2

# Crie um programa que permita a um professor registrar as notas de uma turma.
# O programa deve continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma. Notas = [] -> len(Notas)



notas = []

while True:
    try:
        nota = input("Digite a nota da turma ou 'fim' para terminar: ").lower()
        if nota == "fim":
            break

        valor = float(nota)
        if 0 <= valor <= 10:
            notas.append(valor)
        else:
            print("Nota fora do intervalo (0 a 10).")
    except ValueError:
        print("Entrada inválida. Digite um número ou 'fim'.")

if notas:
    resultado = sum(notas) / len(notas)
    print(f"Média da turma: {resultado:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")
