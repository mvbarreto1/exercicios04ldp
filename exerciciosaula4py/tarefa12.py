total = 0


for i in range(1, 6):
    preco = float(input(f"Digite o preço do produto {i}: "))
    total += preco  
    
   
    if total > 100:
        total *= 0.9  
        print("Desconto de 10% aplicado!")
        break  

print(f"O total final é: R${total:.2f}")
