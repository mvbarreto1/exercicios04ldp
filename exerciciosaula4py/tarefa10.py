positivos = 0
negativos = 0

for i in range(10):
    numero = int(input("Digite um número: "))
    
    if numero == 0:
        break
    

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
