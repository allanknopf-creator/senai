peso = float(input("Digite o peso do prato pelo cliente (em kg): "))
if peso <= 0:
    break
print("valor invalido")

valor_a_pagar = peso_prato * 12.0
print("o valor a pagar é: R$: ", valor_a_pagar)
