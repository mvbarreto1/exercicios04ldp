for numero in range(1, 31):

    if numero > 20:
        break
    
    if numero % 5 == 0:
        print(f"{numero} é múltiplo de 5")
    else:
        print(numero)
