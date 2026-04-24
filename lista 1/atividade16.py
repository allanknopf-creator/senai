qtd = int(input("Digite a quantidade de sanduíches: "))

# em gramas
queijo_g = qtd * 100
presunto_g = qtd * 50
carne_g = qtd * 100

# converter para kg
queijo_kg = queijo_g / 1000
presunto_kg = presunto_g / 1000
carne_kg = carne_g / 1000

print("\nQuantidade necessária:")
print("Queijo:", round(queijo_kg, 2), "kg")
print("Presunto:", round(presunto_kg, 2), "kg")
print("Carne:", round(carne_kg, 2), "kg")