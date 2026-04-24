salario_inicial = float(input("Digite o salário inicial: R$ "))

# aumento de 15%
salario_com_aumento = salario_inicial * 1.15

# desconto de 8% de imposto
salario_final = salario_com_aumento * 0.92

print("\nSalário inicial: R$ {:.2f}".format(salario_inicial))
print("Salário com aumento: R$ {:.2f}".format(salario_com_aumento))
print("Salário final: R$ {:.2f}".format(salario_final))
