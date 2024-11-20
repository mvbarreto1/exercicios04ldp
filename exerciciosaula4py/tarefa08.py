soma_notas = 0

for i in range(1, 6):
    nota = float(input(f"Digite a nota {i}: "))
    soma_notas += nota  

media = soma_notas / 5

print(f"A média do aluno é: {media:.2f}")
if media >= 6:
    print("Classificação: Aprovado")
else:
    print("Classificação: Reprovado")
